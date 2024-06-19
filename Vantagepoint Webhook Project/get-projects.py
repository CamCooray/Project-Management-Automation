import requests
import json
import re

def getProjects():
    url = "https://2mnext.deltekfirst.com/2MNEXT/api/project"

    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer nZnZ_VoTKjH5tp0lso5a5eZa7Bo4e8p36u9C7BpIsCSQIHKLOWW2X8BpiNKFFirHWGk8pcjutHRaykcHzPyVZN4TFWQeLXfETR3xSzEkB2AOXreEzMTnZP1_yNT6TQz4DR3x4_aisbGaaDUrZZlzVLM_Vp66vAvILMLYrJZZy7DZe6K9DVbd20zal2YxdxDILCLrbrQUubRrCNThlxjSD7mKp4kf0fIUdGCMizcn0VugPzmw8ni_negHZg8EuJJsrGV_KaAtw-juoSXwhRbstmpSTLIHZfqTPr3SB5vJ0zy0jjAVoBWkSx0UaLW-zlJHr8xAv1LXBZGLydEWCtGVzYtFoJRHYMRU9J2mFKOOpScYWYAqGBvUbBfR2eLK8U8qh7sfLxD9n_6l91K3VlpaTw'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        projects_list = []

        pattern = re.compile(r'^\d{5}\.\d{2}$')

        for project in data:
            WBSNumber = project.get("WBSNumber", "")
            if pattern.match(WBSNumber):
                projects_list.append({
                    "WBSNumber": WBSNumber,
                    "Name": project.get("Name", "")
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

def sendToOneDrive():
    print("hello")

    
if __name__ == "__main__":
    projects = getProjects()
    file_path = 'C:/Users/CameronCooray/Documents/Vantagepoint Webhook Project/projects.json'
    save_projects_to_file(projects, file_path)
#add stage from vantagepoint
#two methods using reg ex: proposal and projects