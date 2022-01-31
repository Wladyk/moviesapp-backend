# moviesapp-backend
# Backend module of movie managment app developed for entry test.

Note: this app is for elementary development stage only. Several issues would be addressed if the app were to enter into prod stage. 
Among them, user login persistency. All important tokens have been stored in volatile state (Redux). This is highly secure, but the user will lose login after closing the page. In prod, we would likely work with HTTP-only cookies to deal with such data. 


#How to run (Linux environment)
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
