# Flask Class Attendance System!

This is a Class Attendance System made with Python, Flask, HTML, CSS, BOOTSTRAP 4 and SQLITE to make the queries. I wanted to make a system to help teachers like me to write what happend in a class, what student came to the class, write notes, and so on.
For a teacher who works in a more simple school, like me in Brazil, as a Math Teacher, it becomes a pain in the knee to write all the class details in a notebook, so the idea to a simple system came.

# Files

Some files are easier to change than others. I personally recomend you to look on the **models.py** before changing the templates.
**main.py** pretty much generates the **classes** and **index** pages.
**auth** generate the authentication pages. I'll add some comments to the functions telling what they do.

## How to open the project
As you can see, the files already came with a **venv** folder, that already have flask, jinja, flask-login, flask-sqlalchemy and other packages to run the code.
Here is a step by step for you to open the project.

 - Make sure you make a folder tree like this, it can be on your desktop area: **attendanceSystem/project/** and then put the files inside project
 - Open a terminal, i personally use git bash, in the folder **attendanceSystem**
 - type: **source project/venv/Scripts/activate**
 - type: **export FLASK_APP=project**
 - type: **flask run**

