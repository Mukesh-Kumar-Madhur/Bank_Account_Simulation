# Bank Account Simulation

## Overview
This project is a comprehensive Bank Account Simulation developed using Python and Tkinter. It simulates basic banking operations, allowing users to create and manage their bank accounts. The application provides a graphical user interface (GUI) for an intuitive user experience and uses an SQLite database for data persistence.

## Features
- **User Authentication**: Secure login functionality to ensure user-specific access.
- **Account Management**: Users can create new accounts, recover forgotten passwords, and manage their personal information.
- **Transaction Operations**: 
  - **Check Balance**: View current account balance and account details.
  - **Deposit Funds**: Add money to the account.
  - **Withdraw Funds**: Remove money from the account, with balance checks to prevent overdrafts.
  - **Transfer Funds**: Transfer money between accounts, with validation to ensure the target account exists and sufficient balance is available.
- **Profile Management**: Users can update their profile picture, which is stored and managed locally.

## Technologies Used
- **Python**: Core programming language used for application logic.
- **Tkinter**: Library used to create the graphical user interface.
- **SQLite**: Database used to store user data, including account information and transaction details.
- **Pillow (PIL)**: Library used for image processing, allowing users to upload and change profile pictures.

## Project Structure
- **main.py**: Contains the main application logic and GUI setup.
- **database/**: Folder containing the SQLite database file (`banking.sqlite`).
- **images/**: Directory for storing profile pictures and other GUI-related images.

## Installation and Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/Mukesh-Kumar-Madhur/bank-account-simulation.git
    cd bank-account-simulation
    ```

2. Install the required libraries:
    ```sh
    pip install tkinter pillow sqlite3
    ```

3. Run the application:
    ```sh
    python main.py
    ```

## Usage
Upon running the application, users are greeted with a login screen. New users can create an account, while existing users can log in with their credentials. Once logged in, users can view their account details, perform transactions, and update their profile information.

## Contributions
Contributions are welcome! Please fork the repository and submit pull requests for any improvements or bug fixes.
