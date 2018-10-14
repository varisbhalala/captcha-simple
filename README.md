# captcha-simple for Django 2.0
Captcha simple is a library available publicly for Django 2.0. Using this library one can create captchas( alphanumeric).It has refresh utility to change the captcha through ajax call and get the captcha without refreshing the page.The login page and the redirect page are customizable and can be changed according to the requirement.

## Requirements and Dependencies
### -> all these requirements can be downloaded by *pip install*
* Django 2.0
* Pillow

## Installation 
* Install the package by moving to your project folder
```python
pip3 install captcha-varis-main
```
* Run the server after installing all the dependencies
 ```python
puthon3 manage.py runserver
```
* Open the brower window and hit the url to get to the demo page.

## Special Notes
* Currently the library doesn't use any database to access and verify user credentials, but you can customize and put database settings in *settings.py* file in the **root** directory of the project.

* The login and welcome templates can be changed from the templates folder in the project directory. The files are named **login.html** and **welcome.html** 

* Dynamic database settings for database during installation would be the new update from our side.

