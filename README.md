# Django registration with confirmation email and two factor authentication using the google authenticator app 

This is a django application created using Django 1.10 and python 3.6. The project has 
extended django authentication and I have implemented the ability for user to register, 
after a given user register in our web app, we send an email for user
to click a link and confirm they control the email used during registration. The project has 
also implemented the ability to enable two factor authentication using [Google Authenticator App](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en)


### Test The Project

1. Clone the project using ***git clone https://github.com/henrymbuguak/django-email-confirmation-and-two-factor-authentication-using-the-google-authenticator-app.git***
2. Create a python virtual environment using: ***mkvirtualenv --python=/usr/bin/python3.4 mysite-virtualenv*** this 
command will create a virtual environment name mysite-virtualenv and activate it. [Learn more about python virtualenv](https://docs.python-guide.org/dev/virtualenvs/)
3. Navigate to the project root directory on your terminal, **This where manage.py file is located** in this folder your 
see a file named ***requirements.txt*** This file holds the dependency of this project.
4. To install the project dependency use this command on your terminal: ***pip install -r requirements.txt***
5. The next step is to run the migrations, for simplicity we are going to use sqlite database that comes with python.
6. On your terminal run this command: ***python manage.py makemigrations***. Learn more about [django migration system](https://docs.djangoproject.com/en/2.1/topics/migrations/)
7. The next step is to apply the migrations by using: ***python manage.py migrate***
8. In order for django to send emails, you need to configure email configurations in **settings.py** file. In settings.py 
there is this section:

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'youremail@mail.com'

EMAIL_HOST_PASSWORD = 'password'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

9. After filling the email configuration, run the development server using: **python manage.py runserver**


### Demo site

To test the functionality of this project, visit [HenryLab demo site](http://henrymbuguak.pythonanywhere.com/)


1. Register using a valid email address
2. After registering, the system will send you a confirmation email.
3. Login into email account an click on confirmation link.
4. The system will automatically log you in and you will be in your dashboard.
5. Inside your dashboard you will see the button named **Enable or Disable two factor authentication**
6. Click on the button and follow the instruction on how to enable two factor authentication.
7. After enabling two factor authentication logout and login again to test the functionality.


**NB** Remember you need [Google Authenticator App](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en)
app on your phone to scan QR code.