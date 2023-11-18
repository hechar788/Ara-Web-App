# Ara-Web-App
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



Version 2

- Updated validity function to return flashed message string for a layer of abstraction - cleaner to read in views.py

- Added docstrings to demerit_calculation.py functions

- Added 'Home' button to base template to satisfy requirements
  - Appears on all html pages except bad_url_path


TO WORK ON:
  - Use Bootstrap for better front end design 
