# Interactive Chat Application
A Django-powered chat application allowing users to create asynchronous chat rooms. Each room is accessible to all users, providing a platform to archive their conversations. Registration and login are mandatory for using the chat application.

Django's channels were utilized to handle asynchronous operations, enabling bidirectional communication between the client and server. This implementation guaranteed smooth message delivery. By leveraging Django's channels, the application facilitated seamless message transmission, greatly enhancing the overall user experience.

Before accessing the chat application's features and engaging in real-time communication, user registration is a necessary initial step.

## 🚀 Features
- Image upload functionality
- Asynchronous chat rooms makes Instant message loading and real time communication without the need of page reload using websockets
- Chat rooms/spaces with seperate chat style for current user and other users
- Dashboard with list of rooms to join

## 📚 What I've learned
- Focused a lot on learning websockets and django hannels
- Learnt the MongoDB integration in python using pymongo
- Asynchronous bi-directional communication
- And much more...


## ⚡ Main Technologies
<code>Python</code> <code>Django</code> <code>HTML</code> <code>CSS</code> <code>Postgresql</code> <code>Websockets</code> <code>Django Channels</code> <code>MongoDB</code>
## ⚙️ Installation
```bash
# Clone the repository to your local machine.
git clone https://github.com/VishnuKumarSS/Interactive-Chat-App-Websockets.git
```
**Create & Activate the Virtual Environment:**
```bash
# Create the virtual environment
$ python -m venv venv

# Activate the virtual environment in Windows (In git bash)
$ source venv/Scripts/activate
# Activate the virtual environment in Linux/Mac
$ source venv/bin/activate
```
**Install the required python packages:**
```bash
$ pip install -r requirements.txt
```
## Run the application:
```bash
# Create and Apply migrations
$ python manage.py makemigrations
$ python manage.py migrate

# Create superuser to help managing for the first time
$ python manage.py createsuperuser

# To start the Django server
$ python manage.py runserver
```
**View the app:**
> Open http://127.0.0.1:8000/ (or the address shown in your console) in your web browser to view the app.

## 🖼️ Demo Images
![thumbnail](https://github.com/VishnuKumarSS/Interactive-Chat-App-Websockets/assets/90044424/b5a162b3-b7d8-4bbd-98ec-3b664654f696)