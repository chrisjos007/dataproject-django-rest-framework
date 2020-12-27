# DataProject django rest framework

Django Rest Framework version of the data project

## Objective

1. To load data from csv file using django admin custom command.
2. To configure django admin to add/delete/modify data.
3. To create Web API and plot graphs based on parameters specified in userstories.

## Data and Requirements

1. The csv file required for populating database has been provided in the csvdata directory within the app 'dataloader'.
2. Requierments for running the application has been provided in the requirements.txt file.

## Running the application

1. Create the role and database in postgres using creator.sql file in the SQL directory
2. Create a virtual environment and activate it.
3. install the package requirements specified in *requirements.txt*
4. Go into the project directory -> unpopulation in terminal and run the following commands

        python manage.py makemigrations
        python manage.py migrate
        python manage.py dbloader
5. Create super user for admin access by running
        
        python manage.py createsuperuser
6. To start the application run

        python manage.py runserver
7. To view the problem statements open browser and got to [http://127.0.0.1:8000](http://127.0.0.1:8000)
8. Browse through the problem statements as specified in the user stories.