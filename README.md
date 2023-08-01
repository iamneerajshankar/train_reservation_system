## Seat Reservation System Documentation
### Author - Neeraj Shankar
### Email - neeraj.shankar@outlook.com

## Project description 
#### This project enable user to send Cabin detail and number of family members to reverse the seats for. The seat
#### is reserved only when a given cabin has required number of seats available for family member
### Note --> 
#### 1. This is sample project and no data is being saved in database. Except the Cabin Class Data which is which is prepopulated for testing purpose
#### 2. Only POST is implemented to demonstrate the logic for seat reservation.
#### 3. Admin User Details and Environment file are given in project_data.env(root dir)

## Pre-requisite :heavy_check_mark:
## Please ensure python is installed the on system 

## Required Packages
### The following packages required
1. djangorestframework==3.14.0
2. Markdown==3.4.3
3. django-filter==23.2
4. Django~=4.2.3
5. django-environ==0.10.0
6. pytest~=7.4.0
7. django-dynamic-fixture==3.1.2
8. pytest-cov==4.0.0
9. pytest-django==4.5.2
10. requests==2.28.1
11. requests-mock==1.10.0

### Installing the required packages:
#### It is recommended to create a virtual environment. Please open the project folder in any 
#### IDE(VS Code/Pyharm). Create Virtual Environment

#### Create virtual environment on windows
    python -m venv "rest-framework" 

#### Create virtual environment on windows
    python3 -m venv "rest-framework" 

#### To activate on windows
    rest-framework\Scripts\activate

#### To activate on mac or linux
    source pytest-automation/bin/activate

### Install the required packages using requirements.txt (from project root dir)
    pip install -r requirements.txt

#### Running the app
    python manage.py runserver 

#### The app can be accessed at on local server
    http://127.0.0.1:8000/

### Payload to send --> There is file root project directory named payload_data 

### Running The test file 
#### Navigate to the project root directory and the below command (make sure virtual env is activated)
    pytest --cov=reservation_app/

### End of document
