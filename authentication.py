import json
import re
import datetime

USERS_FILE = 'users.json'

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

try:
    with open(USERS_FILE, 'r') as users_file:
        registered_users = json.load(users_file)
except FileNotFoundError:
    registered_users = []

def save_users_data():
    with open(USERS_FILE, 'w') as users_file:
        json.dump(registered_users, users_file, cls=DateTimeEncoder)

def validate_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

def validate_phone(phone):
    return re.match(r'^01[0-2]\d{8}$', phone)

def register():
    print("Registration:")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    if not validate_email(email):
        print("Invalid email format. Please enter a valid email.")
        return
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    mobile_phone = input("Enter your mobile phone number: ")
    if not validate_phone(mobile_phone):
        print("Invalid phone number format. Please enter a valid Egyptian phone number.")
        return
    registered_users[email] = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password, 'mobile_phone': mobile_phone, 'projects': []}
    save_users_data()
    print("Registration successful!")

def login():
    print("Login:")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user = registered_users.get(email)
    if user and user['password'] == password:
        print(f"Welcome, {user['first_name']} {user['last_name']}!")
        return user
    else:
        print("Invalid email or password. Please try again.")
        return None
