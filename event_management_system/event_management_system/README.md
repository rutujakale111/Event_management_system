### Event Management System with Attendee Invitations

### Description
This project is a web application designed to manage events, allowing users to create events, invite attendees, and track RSVPs. It includes functionalities for creating, reading, updating, and deleting events, along with email notifications for invitations.

### Features
Create, read, update, and delete events.
Invite attendees via email.
Track RSVPs for events.
Prevent users from RSVPing to overlapping events.
User-friendly interface with Django admin panel.

### Technologies Used
Django: Web framework for building the application.
Django REST Framework: For building APIs.
SQLite: Database used for data storage (default in Django).
HTML/: For front-end templates.

### Project Structure
event_management_system/
│
├── events/                          
│   ├── migrations/                 
│   ├── templates/                   
│   │   └── events/                  
│   │       ├── event_list.html      
│   │       ├── event_form.html      
│   │       └── event_confirm_delete.html 
│   ├── __init__.py                  
│   ├── admin.py                     
│   ├── apps.py                      
│   ├── forms.py                     
│   ├── models.py                    
│   ├── tests.py                     
│   ├── urls.py                      
│   └── views.py                     
│
├── event_management_system/         
│   ├── __init__.py                 
│   ├── settings.py                  
│   ├── urls.py                      
│   └── wsgi.py                      
│
├── manage.py                        
├── db.sqlite3                      
└── requirements.txt 

### Installation
### Clone the repository:

git clone https://github.com/rutujakale111/Event_management_system
cd event_management_system
Set up a virtual environment (optional but recommended):

python -m venv venv

### Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Install dependencies:
pip install django djangorestframework

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Run the development server:
python manage.py runserver

Access the application:
Open your web browser and go to:

http://127.0.0.1:8000/

Access the admin panel at:

http://127.0.0.1:8000/admin/

### Usage
Navigate to the event list to create, update, and delete events.
Invite attendees and track their RSVPs through the application.
Use the Django admin panel for backend management.