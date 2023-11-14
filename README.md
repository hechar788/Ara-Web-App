# Ara-Web-App
1st web app creation

Demerit Point Calculator

Version 1 

- Web app created with Python Flask.
- HTML templates contained in templates directory.
- Blueprint rendered and app runs via python_app.py.
  
- Calculation tools created in relation to demerit point calculations,
  and user displayed messages stored in demerit_calculation.py.

Views.py
imports flask for web application tools
imports demerit_calculation.py for calculations regarding user input

- Contains blueprint structure for website with the only accessible route being '/'
- 404 page not found error, redirects users back to @views.home('/')
- Renders html template displaying successful calculation information if users input valid arguments

HTML Templates
very basic html design (CURRENT)


TO WORK ON:
  - Updated validation function in demerit_calculation.py
  - Update views.py to follow logically + Displaying information to the succesful calculation html template.
  - Use Bootstrap for better front end design 
