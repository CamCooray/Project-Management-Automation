# - done - add stage from vantagepoint
#two methods using reg ex: proposal and projects
# - done -  method to determine if new project has been created

import os
import requests
import json
import re
import pandas as pd

def get_projects():
    url = "https://companyname.deltekfirst.com/companyname/api/project"

    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer sCqXknUIW1yFs-LZe7pcbLsEgkvLtjj-fuSf1uXxZvQOtSO6XeOedi3B4sgh3MXX6_3syimqs16kBDpdikcTnMc-VI_7OfdBVVnfG3Ggp3vYjKZqlZLU9e7gLA-aNDn5gKhKzOG93mQTq5kwwld48-7yLh2_OjDYWtVjX2NpWyeTqVfVPlidFTPUkIX5y4Zg9yCxspI3By3gfCDeKWcPj5foKHH1oZ84CT4LYl26HgAJFZ6D0kD01BMDvj_8GitqXN1Z--Y6OrU0o6gaJVL6tmkiOhWOv6juDHxS6VL7RIKwrGJKu9qL5UuoSm91FvLKkeyP-rNsnEQYjjJj8L0CYChQG_qUhVH39bvofCj8WBGaMm4iKbd-THbQN1XuRd4DltNHhAVGJuHCkKBVI8EwGQ'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        projects_list = []

        WBSpattern = re.compile(r'^\d{5}\.\d{2}$')

        for project in data:
            WBSNumber = project.get("WBSNumber", "")
            if WBSpattern.match(WBSNumber):
                projects_list.append({
                    "WBSNumber": WBSNumber,
                    "Name": project.get("Name", ""),
                    "Stage": project.get("Stage", "")
                })
        
        return projects_list
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.text)
        return []

def save_projects_to_file(projects, file_path):
    with open(file_path, 'w') as file:
        json.dump(projects, file, indent=2)
    print(f"Projects saved to {file_path}")

def save_projects_to_excel(projects, file_path):
    df = pd.DataFrame(projects)
    df.to_excel(file_path, index=False)
    print(f"Successfully Projects saved to {file_path}")

def compare_with_saved_data(new_projects, saved_projects):
    saved_project_numbers = set(project['WBSNumber'] for project in saved_projects)
    new_Projects_numbers = [project for project in new_projects if project['WBSNumber'] not in saved_project_numbers]
    return new_Projects_numbers

def read_projects_JSON(file_path):
    projects = []
    try:
        with open(file_path, 'r') as file:
            projects = json.load(file)
    except Exception as e:
        print(f"Failed to read projects from {file_path}: {e}")
    return projects

def main():
    projects = get_projects()

    # Get the user's home directory
    home_directory = os.path.expanduser('~')
    
    # Define the file path within the user's home directory
    file_path = os.path.join(home_directory, 'projects.json')

    if not os.path.exists(file_path):
        save_projects_to_file(projects, file_path)
        print("Initial projects saved to file.")
        save_projects_to_excel(projects, file_path)
    else:
        saved_projects = read_projects_JSON(file_path)
        #print("Saved Projects:")
        #for project in saved_projects:
        #    print(project)

        new_projects = compare_with_saved_data(projects, saved_projects)

        if new_projects:
            print("New Projects:")
            for project in new_projects:
                print(project)
        else:
            print("No new projects found.")

if __name__ == "__main__":
    main()
