# GateKeeper 🔐

**GateKeeper** is a simple Python-based password manager designed to help you securely manage your passwords. It uses encryption to protect your stored data and requires a master password to access the entries.

> **Warning:** This script may contain bugs and should **not** be used as a secure password management solution for storing sensitive information. Use at your own risk!

## Features 🌟

- **Add New Entries** ➕: Store passwords along with usernames, emails, or phone numbers.

- **Retrieve Entries** 🔍: Access stored passwords using entry titles.

- **Remove Entries** 🗑️: Delete unwanted or outdated entries.

- **Print All Entries** 📋: View all stored entries at once.

- **Reset Master Password** 🔑: Change the master password for accessing the database.

## Requirements 📋

- Python 3.6 or higher

- `cryptography` library for encryption and decryption

- `bcrypt` library for password hashing

## Installation 🛠️

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/gatekeeper.git

cd gatekeeper
```

2. **Install Required Libraries**

```bash
pip install cryptography bcrypt
```

3. **Run the Script**

```bash
python gatekeeper.py
```


# How to Use 📖

## Initial Setup

1. **Run the Script**: Start the script by running python gatekeeper.py.

2. **Set Your Master Password**: When prompted, set a strong master password. It should be at least **12 characters** long and include upper case, lower case, numbers, and special characters.

## Main Menu

The main menu provides the following options:

1. **Add Entry ➕**

    - Entry Title *(mandatory)*
    - Username/Email/Phone Number
    - Password
    - URL *(optional)*

2. **Retrieve Entry 🔍**

    - Enter the entry title to retrieve the stored data.

3. **Remove Entry 🗑️**

    - Enter the entry title to remove an entry from the database.

4. **Print All Entries 📋**

    - View all stored entries, including titles, usernames, and decrypted passwords.

5. **Reset Master Password 🔑**

    - Enter the current master password.
Set a new master password (must meet complexity requirements).

6. **Exit 🚪**

    - Exit the script.

## Example Usage

**1. Adding an entry**

```plaintext
➕ Adding a New Entry

📜 Entry Title (mandatory): MyEmail
📧 Username/Email/Phone Number: user@example.com
🔐 Password: mySecureP@ssw0rd
🌐 URL (optional): https://example.com

✅ Entry added successfully.
```

**2. Retrieving an Entry**

```plaintext
🔍 Retrieving an Entry

🔍 Enter the entry title you want to retrieve: MyEmail

============================================================
👤 Username/Email/Phone Number: user@example.com
🔑 Password: mySecureP@ssw0rd
🌐 URL: https://example.com
============================================================
```

**3. Reseting Master Password**

```plaintext
🔑 Resetting Master Password

🔐 Enter current master password: 

🔑 Enter new master password (min 12 characters, must include upper, lower, number, special char): 
```

# Security Notes 🔒

- **Encryption**: Uses the cryptography library for encrypting stored passwords.

- **Password Hashing**: Master passwords are hashed using bcrypt.

- **Complexity Requirements**: The master password must be strong and meet complexity requirements.

> **Disclaimer**: This script is for educational purposes and may contain bugs. It should not be used for storing sensitive or critical information. Always use professionally developed and maintained password management solutions for your critical needs. 

# Contributing 🤝

If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add new feature`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Create a new Pull Request.

# License 📝

This project is licensed under the MIT License - see the [LICENSE](https://raw.githubusercontent.com/ByteBendr/gatekeeper_password_manager/main/LICENSE) file for details.


# Summary

- **Setup and Installation**: Instructions to clone the repository, install dependencies, and run the script.

- **Usage**: Detailed instructions on how to use each feature of the script.

- **Security Notes**: Clear warnings about the script’s security limitations.

- **Contributing**: Guidelines for contributing to the project.

- **License**: Licensing information.

