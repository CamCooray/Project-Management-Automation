import requests
import json

def getEmployeeInfo():
    url = "https://2mnext.deltekfirst.com/2MNEXT/api/employee"

    payload = ''
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer lSWvWoKAzUzV4XdWfHK9EHfVrFCDZ32jjqiQjOwUEyvu_yxUHko2FaXYQ0Gx-ItF16hFSYf95eQlyWJnMilmT1_lwT6kJ_IawVTjkhkrKA2e87VKeP_BeQwGN8QPeFiLsbOybeVRK47ws0AYw2z73oOshc-10Jdj8oun6IudSy2qvPQDKCCx6DfFz32U-BH2CKEqMsF7HuNGZEYP-K-9Rs98ZjsF_72Oegd3DhiVO2CvvDlZ8hSaxLh8vqKUjqEj68_bFpqelMkVO36ZtASde5sJ9JVfa9Q4Rx9JPrDa_HreCzQE9AiO9R-7FPBsnyGZ2gZvAtC-OOTn_zbPsfvJjitKFpOHrPzJuOwzyLyvqSRPuCbKPwoY0uxd2ApZG0u8jruvLvliY_edh0eaEjPlkQ'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        employee_hours_list = []

        for employee in data:
            employee_hours = {
                "EmployeeFirstName": employee.get("FirstName",""),
                "EmployeeLastName": employee.get("LastName",""),
                "EmployeeID": employee.get("Employee", ""),
                "HoursPerDay": employee.get("HoursPerDay", 0.0),
            }
            employee_hours_list.append(employee_hours)
        
        print(json.dumps(employee_hours_list, indent=4))
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        print(response.text)

getEmployeeInfo()

