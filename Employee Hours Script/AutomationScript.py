import requests
import json

# Set your API credentials
vantagepoint_api_url = "https://api.your-vantagepoint-domain.com"
vantagepoint_api_key = "your_vantagepoint_api_key"
paycor_api_url = "https://api.paycor.com"
paycor_api_key = "your_paycor_api_key"

# Function to get employee hours from Deltek Vantagepoint
def get_employee_hours():
    url = f"{vantagepoint_api_url}/employee/hours"
    headers = {
        "Authorization": f"Bearer {vantagepoint_api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch employee hours from Vantagepoint:", response.text)
        return None

# Function to input employee hours into Paycor
def input_hours_to_paycor(employee_hours):
    url = f"{paycor_api_url}/employee/hours"
    headers = {
        "Authorization": f"Bearer {paycor_api_key}",
        "Content-Type": "application/json"
    }
    for hours in employee_hours:
        data = {
            "employeeId": hours["employeeId"],
            "hoursWorked": hours["hoursWorked"],
            "date": hours["date"]
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 201:
            print(f"Successfully input hours for employee {hours['employeeId']}")
        else:
            print(f"Failed to input hours for employee {hours['employeeId']}:", response.text)

# Main function to automate the task
def automate_hours_input():
    employee_hours = get_employee_hours()
    if employee_hours:
        input_hours_to_paycor(employee_hours)

# Run the automation
if __name__ == "__main__":
    automate_hours_input()
