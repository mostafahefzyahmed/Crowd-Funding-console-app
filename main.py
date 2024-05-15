import json
import authentication
import projects

try:
    with open(authentication.USERS_FILE, 'r') as users_file:
        registered_users = json.load(users_file)
except FileNotFoundError:
    registered_users = []

try:
    with open(projects.PROJECTS_FILE, 'r') as projects_file:
        projects.projects = json.load(projects_file)
except FileNotFoundError:
    projects.projects = []

def main():
    while True:
        print("\nCrowdfunding Console App:")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            authentication.register()
        elif choice == '2':
            user = authentication.login()
            if user:
                while True:
                    print("\nMenu:")
                    print("1. Create Project")
                    print("2. View Projects")
                    print("3. Edit Projects")
                    print("4. Delete Projects")
                    print("5. Search Projects by Date")
                    print("6. Logout")
                    option = input("Enter your option: ")
                    if option == '1':
                        projects.create_project(user)
                    elif option == '2':
                        projects.view_projects()
                    elif option == '3':
                        projects.edit_project(user)
                    elif option == '4':
                        projects.delete_project(user)
                    elif option == '5':
                        projects.search_projects_by_date()
                    elif option == '6':
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
