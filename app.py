from flask import Flask, render_template, request, redirect, session
from return_grades import main

username = ""
password = ""

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def login():
    global username
    global password
        
    username = ""
    password = ""

    if request.method == 'POST':
        
        user_details = request.form
        username = user_details['student_id']
        password = user_details['password']
        return redirect("/grades")
        
        
    return render_template('login.html')

@app.route('/grades',  methods=['GET', 'POST'])
def index():
    print(f"Student ID: {username}\nPassword: {password}")
    value = main(username, password, .1)
    
    class_names = value[0]
    class_grades = value[1]
    update_time = value[2]
    print(class_names)
    return render_template('grades.html',
                            grade1=class_grades[0],
                           grade2=class_grades[1], grade3=class_grades[2],
                           grade4=class_grades[3], grade5=class_grades[4],
                           grade6=class_grades[5], grade7=class_grades[6],
                           grade8=class_grades[7], class1=class_names[0],
                           class2=class_names[1],class3=class_names[2],
                           class4=class_names[3], class5=class_names[4],
                           class6=class_names[5], class7=class_names[6],
                           class8=class_names[7], time=update_time)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
