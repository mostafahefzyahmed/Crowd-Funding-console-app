import json
import datetime
import authentication

PROJECTS_FILE = 'projects.json'

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

try:
    with open(PROJECTS_FILE, 'r') as projects_file:
        projects = json.load(projects_file)
except FileNotFoundError:
    projects = []

def save_projects_data():
    with open(PROJECTS_FILE, 'w') as projects_file:
        json.dump(projects, projects_file, cls=DateTimeEncoder)

def create_project(user):
    print("Create a Project Fundraise Campaign:")
    title = input("Enter project title: ")
    details = input("Enter project details: ")
    total_target = float(input("Enter total target amount: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    try:
        start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        if start_date >= end_date:
            print("End date should be after start date.")
            return
    except ValueError:
        print("Invalid date format.")
        return
    project_data = {'title': title, 'details': details, 'total_target': total_target, 'start_time': start_date, 'end_time': end_date}
    projects.append(project_data)
    user['projects'].append(project_data)
    authentication.save_users_data()
    save_projects_data()
    print("Project created successfully!")

def edit_project(user):
    print("Edit Your Projects:")
    for idx, project in enumerate(user['projects']):
        print(f"{idx + 1}. {project['title']}")
    if not user['projects']:
        print("You have no projects to edit.")
        return
    choice = int(input("Enter the project number to edit: "))
    if 1 <= choice <= len(user['projects']):
        project = user['projects'][choice - 1]
        print("Editing project:", project['title'])
        new_title = input("Enter new title (leave empty to keep current): ")
        new_details = input("Enter new details (leave empty to keep current): ")
        new_total_target = input("Enter new total target amount (leave empty to keep current): ")
        new_start_date = input("Enter new start date (YYYY-MM-DD) (leave empty to keep current): ")
        new_end_date = input("Enter new end date (YYYY-MM-DD) (leave empty to keep current): ")
        if new_title:
            project['title'] = new_title
        if new_details:
            project['details'] = new_details
        if new_total_target:
            project['total_target'] = float(new_total_target)
        if new_start_date:
            try:
                new_start_date = datetime.datetime.strptime(new_start_date, "%Y-%m-%d")
                if new_start_date < project['end_time']:
                    project['start_time'] = new_start_date
                else:
                    print("Start date should be before end date.")
            except ValueError:
                print("Invalid date format.")
        if new_end_date:
            try:
                new_end_date = datetime.datetime.strptime(new_end_date, "%Y-%m-%d")
                if new_end_date > project['start_time']:
                    project['end_time'] = new_end_date
                else:
                    print("End date should be after start date.")
            except ValueError:
                print("Invalid date format.")
        authentication.save_users_data()
        save_projects_data()
        print("Project updated successfully!")
    else:
        print("Invalid choice.")

def delete_project(user):
    print("Delete Your Projects:")
    for idx, project in enumerate(user['projects']):
        print(f"{idx + 1}. {project['title']}")
    if not user['projects']:
        print("You have no projects to delete.")
        return
    choice = int(input("Enter the project number to delete: "))
    if 1 <= choice <= len(user['projects']):
        del user['projects'][choice - 1]
        save_projects_data()
        authentication.save_users_data()
        print("Project deleted successfully!")
    else:
        print("Invalid choice.")

def view_projects():
    print("All Projects:")
    for project in projects:
        print("Title:", project['title'])
        print("Details:", project['details'])
        print("Total Target:", project['total_target'])
        print("Start Time:", project['start_time'])
        print("End Time:", project['end_time'])
        print()

