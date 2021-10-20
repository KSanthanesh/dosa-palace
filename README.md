# Dosa Palace

## Types of Content
- [Introduction](#introduction "Goto Indroduction")
    - [Home](#home "Goto Home section")
  - [Meals](#meals "Goto Meals")
    - [Meal-details](#meal-details "Goto Meal-detail")
  - [Reservation](#reservation "Goto Reservation")
    - [Reserve](#reserve "Goto Reserve")
    - [View](#view "Goto View")
    - [SignUp](#signup "Goto Signup")
    - [Login](#login "Goto Login")
    - [Logout](#logout "Goto Logout")
  - [Contact-Us](#contact-us "Goto Contact-Us")
    - [Thanks-Msg](#thanks-msg "Goto Thanks-Msg")
- [Strategy](#strategy "Goto Strategy")   
  - [UX](#ux "Goto UX")
    
  - [Business Vision](#business-vision "Goto Business Vision")
  - [Purpose of Website](#purpose-of-website)
- [Scope](#scope "Goto Scope")
   - [Features](#features)
   - [Future Features](#future-features)
- [Structure](#structure "Goto Structure")
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Features Testing](#features-testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Acknowledgement](#acknowledgement)

## Introduction
- This project will cover about the Restaurant,Meal list,Meal details, Reserve the table,Edit and delete the reservation options and contact the restaurant.

- The webpage is categorised into four main section, such us Home, Meals, Restaurant and ContactUs.
- Finally Thanks message is displayed after submitting the Enquiry form.

- The website covers all the screen types, such as Pc,Laptop,Tablet and Mobile.

### Home
The Home Page covers the foloowing sections:
- Header, Logo and Navigation Menu.
- Hero-image
- About us
- Gallery
- Contact details - Address, Email and Phone Number.
- Footer

### Meals
Meals Page covers the following sections:
- Header, footer, contact details and Hero image same like Home page.
- Meal list 
- Meal details button.
### Meal details
Meal details page covers the following sections:
- Image of the Meal
- Meal Name
- Meal description
- Meal price in Euros
- Preparation time in Minutes.

### Reservation



#### Reserve


#### View


#### Signup

#### Login

#### Logout


### Contact-Us


#### Thanks-Msg

## Strategy
The website covers all the screen types, such as Pc, Laptop, Tablet and Mobile. The website is easily navigate to all the sections.

### UX

#### UserStory using Kanban feature in Agile Methodology
These are the steps for UX<br>
1. Click Projects in the dosa palace repositary and Create a Project name.
2. Then select, Project Template => Basic Kanban => create Project.
3. In the ToDo column, there will be three cards, delete those cards.
4. In the Todo column click three dots, then click =>  manage automation => click newly added box => update automation.
5. Then click => issues => new issues => Get started.
6. Then start to write Title and UX.<br>

- As a Site User I can view the service options available in the Restaurant's Home page so that I can select the service that is required.
- As a Site User I can click the Contact option so that I can view the Contact information of the restaurant.
- As a Site User I can view all the meals provided in the Restaurant so that I know what the meals are available in the Restaurant.
- As a Site User I can click the Meal option so that I can view the details of the meal.
- As a Site User I can click the Back to Meals option so that i can return back to the Meals list.
- As a Site User I can click the Reservation option so that I can reserve the Table for dining.
- As a Site User I can register my details so that I can Login.
- As a Site User I can select the Login option so that i can reserve the table for dining.
- As a Site User I can select the Logout the option so that I can logout safely from the website.
- As a Site User I can click the view Reservation option so that I can view the reservation for dining.
- As a Site User I can select the Edit option so that i can edit information provided earlier.
- As a Site User I can select the Delete option so that I can Delete the Reservation.
- As a Site User I can use the contact option so that I can make enquiries regarding my dining requirements.



### Business Vision



### Purpose of Website

## Technologies Used
### Language
- HTML - used for to create the website.

- CSS - used for style the website.

- Python - used for Reserve a table. and allows users to interact with web pages.

### Libraries & Frameworks
- Django Web Application Framework
- Bootstrap
- Font Awesome - icons used throughout the site. Responsive design - To generate the mockup image.
- Google font -used for the website looks more beautiful,fast and great typography

#### Tools
- Gitpod - is an open source platform for automated and ready-to-code.
- Github - to save the project code and host the live project.
- Python Tutor - to check how the Java Script code behaves in each line.
Dev tools -For inspecting and editing the web code.
- Heroku - To Deploy the Project.
- allauth - for site user Signup, login and logout of account.
- Cloudinary - To save images from admin page.
- favicon - for generating 32x32 favicon.
- Am I responsive - to check  the responsive pages.
- Balsamiq - to create wireframes.

## Deployment
First we need to go to github website the create a new repositary using code Institute Template. Followed by giving a new name of the website.Then need to click the create repositary button. After click the button it will bring us to go to another page, which contains the green button labelled as Gitpod.Click the Gitpod button will bring us to the Gitpod Workspace for coding screen.

### gitpod
Used Gitpod Workspace for coding. To preview the browser window need to type "python3 manage.py runserver" in the terminal window at the bottom.Afterthat, have to do git add for add files or remove files and do git commit for reasoning and do the git push for git hub repositary website.

### Procedure for First empty Deployment
1. First install the Django and gunicorn in the terminal => pip3 install django gunicorn  (Gunicon is the server that we're  going to use to run Django on Heroku.)
2. next install supporting libraries:
- pip3 install dj_database_url psycopg2
- pip3 install dj3-cloudinary-storage
3. Requirement.txt file 
- pip3 freeze --local > requirements.txt
4. Create a new project name:
- django-admin startproject dosaproject .
5. Create a new app name:
- python3 manage.py startapp meals
6. Then enter the app name("meals",) in to the INSTALLED_APPS in settings.py
7. Then in the terminal run Migrate changes:
- python3 manage.py migrate
8. Then run the server:
- python3 manage.py runserver (we can see the installation work successfully in the browser).

### Heroku
1. Create new app name and select europe.
2. Then Click => Resources Tab => Addons  enter=> Postgres, then select => Heroku postgres => Hobby dev.
3. Then select the settings tab, click Reveal Config Vars and then copy the Database Value.
### Then again in the workspace
1. Create env.py file in the root directory.
Inside the env.py file
- import os
- then enter os.environ["DATABASE_URL"] = PASTE THE URL FROM HEROKU CONFIG VAR DATABASE_URL WITH STRING.
- then os.environ["SECRET_KEY"] = "SECRET_KEY"
- then copy the secret key value and paste this in  Heroku Reveal config var section in settings tab  without string.

2. Then settings.py
- import os
- import dj_database_url
- if os.path.isfile("env.py"):<br>
	import env
- In SECRET_KEY section remove the value is placed then add like this:<br>
SECRET_KEY = os.environ.get('SECRET_KEY')
- then DATABASES COMMENT OUT ALL (just highlight all of it.
And then, comment out the entire section. 
Press control forward slash on a PC or command forward slash on a Mac to do that.)
- ADD new section like this:<br>
DATABASES = {
		'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
3. Then again enter migration command in the terminal  ==> python3 manage.py migrate
4. Create the Cloudinary Account and then copy the Cloudinary Api, Paste in the env.py file and heroku Reveal config vars. After this  add 'cloudinary_storage',
'cloudinary', in to the INSTALLED_APPS in settings.py.
5. Then add templates in TEMPLATES_DIR in settings.py.
6. Then ALLOWED_HOST needs to be:
- ALLOWED_HOSTS = ['dosa-palace.herokuapp.com', 'localhost']
7. Then Create Procfile, inside the Procfile just enter
- web: gunicorn dosaproject.wsgi:application
8. Then in the terminal:
- git add .
- git commit -m "Deploy Commit"
- git push
9. Then Go heroku app select deploy tab connect the Github and then select Manual deploy. it will create the app run successfully.








