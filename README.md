# moviesapp-backend

# Back-end technologies used

Django, DRF, djoser, PgSQL, djangocorsheaders and whitenoise.

# Note

This app is designed for elementary development stage only. Several issues would be addressed if the app were to enter into prod stage. 
Among them, user login persistency. All important tokens have been stored in volatile front end state (Redux). This is highly secure, but the user will lose login after closing the page. In prod, we would likely work with HTTP-only cookies to deal with such data.    


# Requirements detail

The required functionalities of the app are completely satisfied.
Due to time constrains, the admin backoffice was implemented simply by using Django admin panel, which by the way is a very powerful tool and in my opinion should be used whenever possible in prod stage.

The very same methods I used for user authentication, rating creation, movie adding to watchlist, etc. would be used to build a react-based admin side if it were necessary.

# How to run (Linux environment)

Clone repo in new folder.
If they are not already installed, we must install Python3, venv and PgSQL system-wide.
Create virtual environment with the terminal command "virtualenv venv" .
Activate said environment by terminal command "source /venv/bin/activate"
Navigate to the folder where the cloned project resides.
Run pip install -r requirements.txt
Navigate to the dir where manage.py resides and run:
"manage.py makemigrations"
"manage.py migrate"
"manage.py createsuperuser"

Enjoy :)
