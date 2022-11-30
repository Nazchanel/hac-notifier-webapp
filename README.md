# HAC Grade Update Notifier

This program runs in the background and let you know whenever your grades are updated. This should now work for anyone without limitations of what courses you take. Please report any issues in the issue section of this repository.

---
## Setup

To set this up, you must have the Python environment installed on your computer. You can download it here: https://www.python.org/downloads/. 
Make sure to select the option in the installer to 'Add to PATH'. This allows us to access the Python environment from anywhere. Once it is installed, open up terminal. A quick way to do this is typing `wt` into the Run window (Win + R). Once the terminal is open you must install the packages.

Here are statements you must type into the terminal:

- `pip install plyer`
- `pip install requests`
- `pip install time`
- `pip install datetime`
- `pip install lxml`
- `pip install sys`
- `pip install bs4`

The packages are now installed. Some might already be bundled with the Python environment, but just in case type all of them in. 

---
## Run in the Background
The first method is the method that includes User Input. It requires minimal intervention and is much superior to the other method that will be discussed. 

First, open terminal and navigate to the directory of `main.py`. Once that is done, type `python main.py`. Enter your input into the program. The program should now run in the background infinitely.  

The second method involves some minor intervention into the code. The upside to this method is that you do not need to enter user input and can save some time.

First, you must edit the variables in `input_values.py` in the *run_in_background* folder and change the values of the variables to the value that you need.

Here are the steps:
1. Open the terminal by typing `wt` into the Run window (Win + R)
2. Use the `cd` function to change the directory to the run_in_background folder
3. Run this command: `pythonw main_background.py`

Thats it! The program should run in the background. 

Use the included batch file,named `end_python.bat`, to end the program.  

Credit for this strategy goes to https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf

---------------------------------------------------------
## The Notification
Using the **Plyer** library, a notification is sent to the computer.  

There are two different types of notifications that can be sent to your computer:
1. Update Notification: A message that your grade has been updated
2. Check Alert: A message that your grade has stayed the same since the last time it checked 

The contents for the Update Notification are as follows: 
1. The current date and time

2. The class that the grade was updated

3. The changed grade

4. The old grade

The contents for the Alert Notification are as follows:

1. The current date and time

2. A message saying that there was no change detected
-----------------------------------------
Pictured below is the notification you would get for the Alert Notification:<br>


![image](https://user-images.githubusercontent.com/86535168/156908979-fdd74c80-0895-4d64-b023-716822c8f497.png)
-----------------------------------------
## The Code
The code is commented for the most part. The comments are in the `main.py` file. The code is also commented in the `input_values.py` file in the *run_in_background* folder. 

## Disclaimer
This code is not perfect. It is not guaranteed to work for everyone. If you have any issues, please report them. Also, this code has only been tested on Windows 10. It may not work on other platforms. 

## Final Notes
This is a project I made for fun. It is not meant to be used for malicious purposes. If you use this program for malicious purposes, you are responsible for your own actions. 

## Contact
If you have any questions, comments, or concerns, please contact me at [eshan_iyer@eshaniyer.tech](mailto:eshan_iyer@eshaniyer.tech)

-----------------------------------------
## Functions

There are five function in this project. They are all stored in `functions.py`. I will give a rundown on the code and purpose of these functions.

**`isUpdated(a,b)`**:<br>
This function returns a boolean value based on whether there is a change in the two given lists. It used list comprehension to do so. 

**`getTime()`**:<br>
Returns the current time and date using the datetime library. 

**`initializeClasses(a, b)`**:<br>
This function initializes all the classes and grades. It takes the two scraped HTMLs for the class names and the class grades. It removes any unessesary text and isolates
the name. It returns two lists: one with class names and another with class grades

**`login(session_requests, login_url, password, username)`**:<br>
Using the returned values from the input function, the `login()` function gets into the HAC website and logs in. It then gets the HTML from `Assignment.aspx`, the file
that is recieved by the HAC servers, that contains the classes. It returns the class and class name HTMLs, so initializeClasses can parse through them. 

**`userInput()`**:<br>
This function prompts the user to input their Student ID, password, and delay. The delay is the amount of minutes between each check. It is **NOT** recommended that you
set it as ZERO. It may overload your computer and the servers. It also prints out many lines to act as a primitive method for clearing the console or hiding the inputted
credentials for privacy. 
