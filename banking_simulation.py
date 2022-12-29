from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox,filedialog
import sqlite3 as sql
import shutil
import os

con=sql.connect(database="banking.sqlite")
cur=con.cursor()
try:
    cur.execute("create table users(acn integer primary key autoincrement,name text,pass text,email text,mob text,bal int)")
    con.commit()
    print("table created")
except:
    pass
con.close()



win=Tk()
win.state("zoomed")
win.configure(bg="powder blue")

title=Label(win,text="Bank Account Simulation",bg='powder blue',font=('Arial',50,'bold','underline'))
title.pack()

back_img=Image.open("images/back.png").resize((100,50))
back_imgtk=ImageTk.PhotoImage(back_img,master=win)

head_img=Image.open("images/acn.png").resize((200,100))
head_imgtk=ImageTk.PhotoImage(head_img,master=win)

profile_img=Image.open("images/profilepic.jpg").resize((200,150))
profile_imgtk=ImageTk.PhotoImage(profile_img,master=win)

lbl_head_img=Label(win,image=head_imgtk)
lbl_head_img.place(relx=0,rely=0)

def login_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def openaccount():
        frm.destroy()
        openaccount_screen()
    
    def forgot():
        frm.destroy()
        forgot_screen()
    
    def welcome():
        a=e_acn.get()
        p=e_pass.get()
        if(len(a)==0 or len(p)==0):
            messagebox.showerror("validation","Acn/Pass can't be empty")
            return
        elif(a.isdigit()==False):
            messagebox.showerror("validation","Acn must contain only digits")
            return
        else:
            con=sql.connect(database="banking.sqlite")
            cur=con.cursor()
            cur.execute("select * from users where acn=? and pass=?",(a,p))
            global loggedin_user
            loggedin_user=cur.fetchone()
            if(loggedin_user==None):
                messagebox.showerror("validation","Invalid ACN/PASS")
                return
            else:
                frm.destroy()
                welcome_screen()
     
    def reset():
        e_acn.delete(0,"end")
        e_pass.delete(0,"end")
        e_acn.focus()
        
    lbl_acn=Label(frm,text="Account No",font=("Arail",20,'bold'),bg='pink')
    lbl_acn.place(relx=.3,rely=.2)
    
    lbl_pass=Label(frm,text="Password",font=("Arail",20,'bold'),bg='pink')
    lbl_pass.place(relx=.3,rely=.3)
    
    e_acn=Entry(frm,font=("Arail",20,'bold'),bd=7)
    e_acn.place(relx=.45,rely=.2)
    e_acn.focus()
    
    e_pass=Entry(frm,font=("Arail",20,'bold'),bd=7,show="*")
    e_pass.place(relx=.45,rely=.3)
    
    btn_login=Button(frm,command=welcome,text='login',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
    btn_login.place(relx=.4,rely=.42)
    
    btn_reset=Button(frm,command=reset,text='reset',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
    btn_reset.place(relx=.52,rely=.42)
    
    btn_fp=Button(frm,command=forgot,text='forgot password',font=("Arail",20,'bold'),bd=7,width=15,bg='powder blue')
    btn_fp.place(relx=.3,rely=.6)
    
    btn_open=Button(frm,command=openaccount,text='open account',font=("Arail",20,'bold'),bd=7,width=15,bg='powder blue')
    btn_open.place(relx=.52,rely=.6)
    
 
def openaccount_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back(event):
        frm.destroy()
        login_screen()
    
    def reset():
        e_name.delete(0,"end")
        e_pass.delete(0,"end")
        e_email.delete(0,"end")
        e_mob.delete(0,"end")
        e_name.focus()
        
    def open():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        bal=1000
        
        con=sql.connect(database="banking.sqlite")
        cur=con.cursor()
        cur.execute("insert into users(name,pass,email,mob,bal) values(?,?,?,?,?)",(name,pwd,email,mob,bal))
        con.commit()
        con.close()
        
        con=sql.connect(database="banking.sqlite")
        cur=con.cursor()
        cur.execute("select max(acn) from users")
        row=cur.fetchone()
        messagebox.showinfo("Open Account",f"Account created with ACN:{row[0]}")
        con.close()
        frm.destroy()
        login_screen()
        
    lbl_back=Label(frm,image=back_imgtk,bd=7,bg='pink')
    lbl_back.bind("<Button>",back)
    lbl_back.place(relx=0,rely=0)
    
    lbl_name=Label(frm,text="Name",font=("Arail",20,'bold'),bg='pink')
    lbl_name.place(relx=.3,rely=.2)
    
    lbl_pass=Label(frm,text="Password",font=("Arail",20,'bold'),bg='pink')
    lbl_pass.place(relx=.3,rely=.3)
    
    lbl_email=Label(frm,text="Email",font=("Arail",20,'bold'),bg='pink')
    lbl_email.place(relx=.3,rely=.4)
    
    lbl_mob=Label(frm,text="Mob",font=("Arail",20,'bold'),bg='pink')
    lbl_mob.place(relx=.3,rely=.5)
    
    e_name=Entry(frm,font=("Arail",20,'bold'),bd=7)
    e_name.place(relx=.45,rely=.2)
    e_name.focus()
    
    e_pass=Entry(frm,font=("Arail",20,'bold'),bd=7,show="*")
    e_pass.place(relx=.45,rely=.3)
    
    e_email=Entry(frm,font=("Arail",20,'bold'),bd=7)
    e_email.place(relx=.45,rely=.4)
    
    e_mob=Entry(frm,font=("Arail",20,'bold'),bd=7)
    e_mob.place(relx=.45,rely=.5)
    
    btn_open=Button(frm,command=open,text='open',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
    btn_open.place(relx=.4,rely=.62)
    
    btn_reset=Button(frm,command=reset,text='reset',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
    btn_reset.place(relx=.52,rely=.62)
    
    
def forgot_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def back(event):
        frm.destroy()
        login_screen()
    
    def reset():
        e_acn.delete(0,"end")
        e_mob.delete(0,"end")
        e_acn.focus()
    
    def get():
        acn=e_acn.get()
        mob=e_mob.get()
        con=sql.connect(database="banking.sqlite")
        cur=con.cursor() 
        cur.execute("select pass from users where acn=? and mob=?",(acn,mob))
        row=cur.fetchone()
        if(row==None):
            messagebox.showerror("Paswword Recovery","ACN does not exist")
        else:
            messagebox.showinfo("Paswword Recovery",f"Your password:{row[0]}")
        frm.destroy()
        login_screen()
        
    lbl_back=Label(frm,image=back_imgtk,bd=7,bg='pink')
    lbl_back.bind("<Button>",back)
    lbl_back.place(relx=0,rely=0)
    
    lbl_acn=Label(frm,text="Account No",font=("Arail",20,'bold'),bg='pink')
    lbl_acn.place(relx=.3,rely=.2)
    
    lbl_mob=Label(frm,text="Mob",font=("Arail",20,'bold'),bg='pink')
    lbl_mob.place(relx=.3,rely=.3)
    
    e_acn=Entry(frm,font=("Arail",20,'bold'),bd=7)
    e_acn.place(relx=.45,rely=.2)
    e_acn.focus()
    
    e_mob=Entry(frm,font=("Arail",20,'bold'),bd=7)
    e_mob.place(relx=.45,rely=.3)
    
    btn_get=Button(frm,command=get,text='recover',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
    btn_get.place(relx=.4,rely=.42)
    
    btn_reset=Button(frm,command=reset,text='reset',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
    btn_reset.place(relx=.52,rely=.42)
    
def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    

    def change_pic():
        filepath=filedialog.askopenfilename()
        dest_path=f"images/{loggedin_user[0]}.png"
        shutil.copy(filepath,dest_path)
        profile_img=Image.open(dest_path).resize((200,150))
        profile_imgtk=ImageTk.PhotoImage(profile_img,master=win)
        profile_pic_lbl.image=profile_imgtk
        profile_pic_lbl['image']=profile_imgtk
        
    profile_pic_lbl=Label(frm,image=profile_imgtk)
    profile_pic_lbl.place(relx=.85,rely=.01)
    
    if(os.path.exists(f"images/{loggedin_user[0]}.png")):
        profile_img1=Image.open(f"images/{loggedin_user[0]}.png").resize((200,150))
        profile_imgtk1=ImageTk.PhotoImage(profile_img1,master=win)
        profile_pic_lbl.image=profile_imgtk1
        profile_pic_lbl['image']=profile_imgtk1
    
    btn_chg_pic=Button(frm,command=change_pic,text='change picture',font=("Arail",15,'bold'),bd=7,bg='powder blue')
    btn_chg_pic.place(relx=.87,rely=.28)

    def logout():
        frm.destroy()
        login_screen()

    def checkbal():
        inr_frm=Frame(frm)
        inr_frm.configure(bg='pink')
        inr_frm.place(relx=.3,rely=.25,relwidth=.5,relheight=.4)
        
        con=sql.connect(database='banking.sqlite')
        cur=con.cursor()
        cur.execute("select bal from users where acn=?",(loggedin_user[0],))
        update_bal=cur.fetchone()[0]
        con.close()
        lbl_bal=Label(inr_frm,text=f"Balance:\t\t{update_bal}",bg='pink',font=("Arail",15,'bold'))
        lbl_bal.place(relx=.1,rely=.1)
        
        lbl_acn=Label(inr_frm,text=f"Acn:\t\t{loggedin_user[0]}",bg='pink',font=("Arail",15,'bold'))
        lbl_acn.place(relx=.1,rely=.3)
        
        lbl_mob=Label(inr_frm,text=f"Mob:\t\t{loggedin_user[4]}",bg='pink',font=("Arail",15,'bold'))
        lbl_mob.place(relx=.1,rely=.5)
        
        lbl_email=Label(inr_frm,text=f"Email:\t\t{loggedin_user[3]}",bg='pink',font=("Arail",15,'bold'))
        lbl_email.place(relx=.1,rely=.7)
     
    def deposit():
        inr_frm=Frame(frm)
        inr_frm.configure(bg='pink')
        inr_frm.place(relx=.3,rely=.25,relwidth=.5,relheight=.4) 
        
        def deposit_db():
            amt=int(e_amt.get())
            con=sql.connect(database='banking.sqlite')
            cur=con.cursor()
            cur.execute("update users set bal=bal+? where acn=?",(amt,loggedin_user[0]))
            con.commit()
            con.close()
            messagebox.showinfo("Deposit","Done")
            e_amt.delete(0,"end")
            
        lbl_amt=Label(inr_frm,text="Amount",bg='pink',font=("Arail",20,'bold'))
        lbl_amt.place(relx=.1,rely=.2)
        
        e_amt=Entry(inr_frm,font=("Arail",20,'bold'),bd=7)
        e_amt.place(relx=.3,rely=.2)
        
        btn_dep=Button(inr_frm,command=deposit_db,text='deposit',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
        btn_dep.place(relx=.2,rely=.5)
    
    
    def withdraw():
        inr_frm=Frame(frm)
        inr_frm.configure(bg='pink')
        inr_frm.place(relx=.3,rely=.25,relwidth=.5,relheight=.4) 
        
        def withdraw_db():
            amt=int(e_amt.get())
            con=sql.connect(database='banking.sqlite')
            cur=con.cursor()
            cur.execute("select bal from users where acn=?",(loggedin_user[0],))
            update_bal=cur.fetchone()[0]
            con.close()
            
            if(update_bal>=amt):
                con=sql.connect(database='banking.sqlite')
                cur=con.cursor()
                cur.execute("update users set bal=bal-? where acn=?",(amt,loggedin_user[0]))
                con.commit()
                con.close()
                messagebox.showinfo("Withdraw","Done")
                e_amt.delete(0,"end")
            else:
                messagebox.showwarning("Withdraw","Insufficient bal")
                e_amt.delete(0,"end")

        lbl_amt=Label(inr_frm,text="Amount",bg='pink',font=("Arail",20,'bold'))
        lbl_amt.place(relx=.1,rely=.2)
        
        e_amt=Entry(inr_frm,font=("Arail",20,'bold'),bd=7)
        e_amt.place(relx=.3,rely=.2)
        
        btn_withdraw=Button(inr_frm,command=withdraw_db,text='withdraw',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
        btn_withdraw.place(relx=.2,rely=.5)
    
    
    def transfer():
        inr_frm=Frame(frm)
        inr_frm.configure(bg='pink')
        inr_frm.place(relx=.3,rely=.25,relwidth=.5,relheight=.4) 
        
        def transfer_db():
            amt=int(e_amt.get())
            toacn=int(e_toacn.get())
            
            con=sql.connect(database='banking.sqlite')
            cur=con.cursor()
            cur.execute("select bal from users where acn=?",(loggedin_user[0],))
            update_bal=cur.fetchone()[0]
            con.close()
            
            con=sql.connect(database='banking.sqlite')
            cur=con.cursor()
            cur.execute("select acn from users where acn=?",(toacn,))
            toacn_frm_db=cur.fetchone()
            con.close()
            if(toacn_frm_db==None):
                messagebox.showwarning("Withdraw","Invalid To Acn")
                e_amt.delete(0,"end")
                e_toacn.delete(0,"end")
            else:
                if(update_bal>=amt):
                    con=sql.connect(database='banking.sqlite')
                    cur=con.cursor()
                    cur.execute("update users set bal=bal-? where acn=?",(amt,loggedin_user[0]))
                    cur.execute("update users set bal=bal+? where acn=?",(amt,toacn))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Transaction","Done")
                    e_amt.delete(0,"end")
                else:
                    messagebox.showwarning("Withdraw","Insufficient bal")
                    e_amt.delete(0,"end")
                    e_toacn.delete(0,"end")

            
        lbl_amt=Label(inr_frm,text="Amount",bg='pink',font=("Arail",20,'bold'))
        lbl_amt.place(relx=.1,rely=.2)
        
        e_amt=Entry(inr_frm,font=("Arail",20,'bold'),bd=7)
        e_amt.place(relx=.3,rely=.2)
        
        lbl_toacn=Label(inr_frm,text="To Acn",bg='pink',font=("Arail",20,'bold'))
        lbl_toacn.place(relx=.1,rely=.45)
        
        e_toacn=Entry(inr_frm,font=("Arail",20,'bold'),bd=7)
        e_toacn.place(relx=.3,rely=.45)
        
        btn_transfer=Button(inr_frm,command=transfer_db,text='transfer',font=("Arail",20,'bold'),bd=7,width=7,bg='powder blue')
        btn_transfer.place(relx=.25,rely=.75)
    
    
    
    lbl_wel=Label(frm,text=f"Welcome,{loggedin_user[1]}",bg='pink',font=("Arail",15,'bold'))
    lbl_wel.place(relx=0,rely=0)
    
    btn_logout=Button(frm,command=logout,text='logout',font=("Arail",15,'bold'),bd=7,width=10,bg='powder blue')
    btn_logout.place(relx=.01,rely=.85)
    
    btn_check=Button(frm,command=checkbal,width=10,text='Details',font=("Arail",20,'bold'),bd=7,bg='powder blue')
    btn_check.place(relx=.01,rely=.1)
    
    btn_deposit=Button(frm,command=deposit,width=10,text='Deposit',font=("Arail",20,'bold'),bd=7,bg='powder blue')
    btn_deposit.place(relx=.01,rely=.3)
    
    btn_withdraw=Button(frm,command=withdraw,width=10,text='Withdraw',font=("Arail",20,'bold'),bd=7,bg='powder blue')
    btn_withdraw.place(relx=.01,rely=.5)
    
    btn_transfer=Button(frm,command=transfer,width=10,text='Transfer',font=("Arail",20,'bold'),bd=7,bg='powder blue')
    btn_transfer.place(relx=.01,rely=.7)
    
login_screen()
win.mainloop()





