import requests
import functions

def main(usr, pswd, dly):
    # Creates a session to maintain credentials
    session_requests = requests.session()

    current_time = functions.getTime()

    username = usr
    password = pswd

    # Will be in use for checking
    delay = dly

    login_url = 'https://hac.friscoisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess%2f'

    html = functions.login(session_requests, login_url, password, username)
    grades_html = html[0]
    name_html = html[1]
    classes = functions.initializeClasses(grades_html, name_html)

    class_names = classes[0]
    class_grades = classes[1]
    print("LOOK HERE --> ")
    print(class_names, class_grades)
    try:
        class_grades_ = [i.replace("%", "") for i in class_grades]
    except:
        class_grades_ = 0
        print("FAILIURE")
    
    class_grades = [float(i) for i in class_grades_]
    
    names_ = []
    grades_ = []

    for i in range(len(class_names)):

        names_.append(class_names[i])
        grades_.append(class_grades[i])

    return (names_, grades_, current_time)