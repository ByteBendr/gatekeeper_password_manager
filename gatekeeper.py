import os
import json
import bcrypt
from cryptography.fernet import Fernet
from getpass import getpass
import re
import time

# Gatekeeper Password Manager Version 1.0.1 (Author: Lucian)

# Constants
DB_FILE = 'passwords.db'
MASTER_PASS_FILE = 'master_pass.key'
MASTER_PASS_HASH_FILE = 'master_pass_hash.txt'

# Encryption and decryption utilities
def generate_key():
    return Fernet.generate_key()

def load_key():
    if os.path.exists(MASTER_PASS_FILE):
        with open(MASTER_PASS_FILE, 'rb') as key_file:
            return key_file.read()
    else:
        return None

def save_key(key):
    with open(MASTER_PASS_FILE, 'wb') as key_file:
        key_file.write(key)

def encrypt_data(key, data):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(key, data):
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(hashed_password, password):
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def validate_password(password):
    """Validate password strength."""
    if len(password) < 12:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# Initialization
def initialize():
    print("🔒 Setting up your password manager 🔒\n")
    while True:
        master_pass = getpass("🔑 Set your master password (min 12 characters, must include upper, lower, number, special char): ")
        if not validate_password(master_pass):
            print("\n❗ Password does not meet the complexity requirements. Please try again.")
            continue
        hashed_master_pass = hash_password(master_pass)
        key = generate_key()
        save_key(key)
        with open(MASTER_PASS_HASH_FILE, 'w') as hash_file:
            hash_file.write(hashed_master_pass)
        print("\n✅ Master password set. Please remember it and keep it safe.\n")
        break

def check_master_password():
    if not os.path.exists(MASTER_PASS_HASH_FILE):
        initialize()
        return None
    with open(MASTER_PASS_HASH_FILE, 'r') as hash_file:
        hashed_master_pass = hash_file.read()
    return hashed_master_pass

def create_db(key):
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as db_file:
            json.dump({}, db_file)
    return key

def add_entry(key):
    print("\n➕ Adding a New Entry\n")
    title = input("📜 Entry Title (mandatory): ")
    if not title:
        print("\n❗ Entry Title is mandatory.\n")
        return

    username = input("📧 Username/Email/Phone Number: ")
    password = getpass("🔐 Password: ")
    url = input("🌐 URL (optional): ")

    encrypted_password = encrypt_data(key, password)
    entry = {
        'username': username,
        'password': encrypted_password,
        'url': url
    }

    with open(DB_FILE, 'r') as db_file:
        data = json.load(db_file)
    
    data[title] = entry

    with open(DB_FILE, 'w') as db_file:
        json.dump(data, db_file)

    print("\n✅ Entry added successfully.\n")
    input("Press Enter to return to the main menu...")

def retrieve_entry(key):
    print("\n🔍 Retrieving an Entry\n")
    title = input("🔍 Enter the entry title you want to retrieve: ")

    with open(DB_FILE, 'r') as db_file:
        data = json.load(db_file)
    
    entry = data.get(title)
    if entry:
        decrypted_password = decrypt_data(key, entry['password'])
        print("\n============================================================")
        print(f"👤 Username/Email/Phone Number: {entry['username']}")
        print(f"🔑 Password: {decrypted_password}")
        print(f"🌐 URL: {entry.get('url', 'N/A')}")
        print("============================================================\n")
    else:
        print("\n🚫 Entry not found.\n")
    input("Press Enter to return to the main menu...")

def remove_entry():
    print("\n🗑️ Removing an Entry\n")
    title = input("🗑️ Enter the entry title you want to remove: ")

    with open(DB_FILE, 'r') as db_file:
        data = json.load(db_file)
    
    if title in data:
        del data[title]
        with open(DB_FILE, 'w') as db_file:
            json.dump(data, db_file)
        print("\n✅ Entry removed successfully.\n")
    else:
        print("\n🚫 Entry not found.\n")
    input("Press Enter to return to the main menu...")

def print_all_entries(key):
    print("\n📋 Printing All Entries\n")
    with open(DB_FILE, 'r') as db_file:
        data = json.load(db_file)
    
    if data:
        for title, entry in data.items():
            decrypted_password = decrypt_data(key, entry['password'])
            print("\n============================================================")
            print(f"📄 Title: {title}")
            print(f"📧 Username/Email/Phone Number: {entry['username']}")
            print(f"🔑 Password: {decrypted_password}")
            print(f"🌐 URL: {entry.get('url', 'N/A')}")
            print("============================================================\n")
    else:
        print("\n🚫 No entries found.\n")
    input("Press Enter to return to the main menu...")

def reset_master_pass():
    print("\n🔑 Resetting Master Password\n")
    hashed_master_pass = check_master_password()
    if not hashed_master_pass:
        print("\n⚠️ No master password set. Initialize first.\n")
        return

    current_pass = getpass("🔑 Enter current master password: ")
    if not check_password(hashed_master_pass, current_pass):
        print("\n❌ Invalid master password.\n")
        return

    while True:
        new_pass = getpass("🔑 Enter new master password (min 12 characters, must include upper, lower, number, special char): ")
        if not validate_password(new_pass):
            print("\n❗ New password does not meet the complexity requirements. Please try again.")
            continue
        hashed_new_pass = hash_password(new_pass)
        new_key = generate_key()
        
        save_key(new_key)
        with open(MASTER_PASS_HASH_FILE, 'w') as hash_file:
            hash_file.write(hashed_new_pass)
        
        print("\n✅ Master password has been reset successfully.\n")
        input("Press Enter to return to the main menu...")
        break

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("┌─────────────────────────────┐")
    print("│       GateKeeper Menu       │")
    print("│                             │")
    print("│ [1] ➕ Add Entry            │")
    print("│ [2] 🔍 Retrieve Entry       │")
    print("│ [3] 🗑️  Remove Entry        │")
    print("│ [4] 📋 Print All Entries    │")
    print("│ [5] 🔑 Reset Master Pass    │")
    print("│ [6] 🚪 Exit                 │")
    print("│                             │")
    print("└─────────────────────────────┘")

def main():
    hashed_master_pass = check_master_password()
    if hashed_master_pass is None:
        return

    key = load_key()
    create_db(key)

    while True:
        display_menu()
        choice = input("\n> Select an option: ")
        if choice == '1':
            add_entry(key)
        elif choice == '2':
            retrieve_entry(key)
        elif choice == '3':
            remove_entry()
        elif choice == '4':
            print_all_entries(key)
        elif choice == '5':
            reset_master_pass()
        elif choice == '6':
            print("\nGoodbye! 👋\n")
            time.sleep(2)
            break
        else:
            print("\n❗ Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
