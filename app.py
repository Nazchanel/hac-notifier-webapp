from flask import Flask, render_template, request, redirect
import functions
import json
from waitress import serve

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
def grades():
    value = functions.returnGrades(username, password, .1, quarter=None)
    functions.returnGradeTables(username = username, password = password, logged_in = False, quarter = None)
    class_names = value[0]
    class_grades = value[1]
    update_time = value[2]
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

@app.route('/1',  methods=['GET', 'POST'])
def quarterOne():
    quarter = 1
    value = functions.returnGrades(username, password, 0, quarter)
    functions.returnGradeTables(username=username, password=password,logged_in=True, quarter=quarter)

    class_names = value[0]
    class_grades = value[1]
    update_time = value[2]

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

@app.route('/2',  methods=['GET', 'POST'])
def quarterTwo():
    quarter = 2
    value = functions.returnGrades(username, password, 0, quarter)
    functions.returnGradeTables(username=username, password=password,logged_in=True, quarter=quarter)

    class_names = value[0]
    class_grades = value[1]
    update_time = value[2]
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

@app.route('/3',  methods=['GET', 'POST'])
def quarterThree():
    quarter = 3
    value = functions.returnGrades(username, password, 0, quarter)
    functions.returnGradeTables(username=username, password=password,logged_in=True, quarter=quarter)
    
    class_names = value[0]
    class_grades = value[1]
    update_time = value[2]

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

@app.route('/4',  methods=['GET', 'POST'])
def quarterFour():
    quarter = 4
    value = functions.returnGrades(username, password, 0, quarter)
    functions.returnGradeTables(username=username, password=password,logged_in=True, quarter=quarter)

    class_names = value[0]
    class_grades = value[1]
    update_time = value[2]

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
    # print("http://localhost:8080")
    # serve(app, port=8080)
    app.run(debug=True, port=8080)
    functions.clear_files()
