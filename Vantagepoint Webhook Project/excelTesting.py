import requests
import pandas as pd

def getProjects():
    url = "https://2mnext.deltekfirst.com/2MNEXT/api/project?limit=5"

    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer VDiP0rkPqi1zlC80NcCQQdrtljSNqz1EP1cbiV0zIE8SnvxwvPL0cbl-1lxpf4z45i7BZE1EOKGL4ZH3bP1LFSbVsZD5geXTtc_xmbHs0s4dQb7Tf-9jkipD4QfsxQlgTkBBt1lv92fB5QmCXxKZRZWDEfSZTnN1Doehlma4FSLamlBcgW1iBn9pXVEhnHxUGFo5gE0QZwiPXUpZrcMslpqzIKNqOu6TtE4GJiRImxoP3OOYYuPZax3qM9uL1PAL0tHdcG7lTXmPu7pspsMHKq0zm1EaQggDHn4Lt3mawStYK_XPqVxac-YK8YkkAOXeya3us75RuGU3b_BXCdrqSPjMrRf7ZZTaBK0di-EGWCTTCZ__UW_4WVOm5MIrYbFTfmuE5a9t5ETLUkzGhZ1YLA'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        projects_list = []

        for project in data:
            projects = {
                "Project Name": project.get("Name", "")
            }
            projects_list.append(projects)
        
        return projects_list
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.text)
        return []

def save_projects_to_excel(projects, file_path):
    df = pd.DataFrame(projects)
    df.to_excel(file_path, index=False)
    print(f"Successfully Projects saved to {file_path}")

if __name__ == "__main__":
    projects = getProjects()
    file_path = 'C:/Users/CameronCooray/Documents/Vantagepoint Webhook Project/projects.xlsx'
    save_projects_to_excel(projects, file_path)
