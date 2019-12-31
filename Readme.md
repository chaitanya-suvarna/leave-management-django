I have created this project just to give Django a try.

I have used Crispy Forms in addition to Django and Python for this.

    pip install django-crispy-forms
    
The web application has a front end designed in Bootstrap and has a Home page which shows all the Resources for the present year. Each month is a Bootstrap Accordion. There is also an Add\Update Leave page that allows a user to Add a new leave of one of the leave types on a specific day and update an existing leave.
Resource addition/modification and LeaveType addition/modification can only be done through the admin page provided by django as default.

The Leave_Portal is a mini-app withing the LeaveManagementProject.

1. Pull the repositiory on your local machine.
2. Run the makemigrations command to check the migrations to be made and then migrate the changes
      
        python manage.py makemigrations
        pythong manage.py migrate
        
3. Run the server and the website will be up and running

        python manage.py runserver
      
I have tried to have a look and implement all the basic features that Django provides, and I must say that I enjoyed working with this framework. If I ever need to spin up a stand-alone website in a short duration, Django will be my go-to framework.
