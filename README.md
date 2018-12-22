# Catalog Web App
Catalog project for the Udacity Full Stack Developer Course @Udacity](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## About
This project is a RESTful web app.  It uses Flask and SQL to populate categories and their respective items. OAuth2 is used as well through Google Plus to provide authorization for CRUD process.

## Within this Repo
The main project file is labeled "project.py" and will run the Flask app.  The database can be stood up by running the "database_setup.py" file which will establish the database structure.  An additional file full of data is also provided and can be run following the database being setup to instantiate an initial store of data.  The html and css are located with folders labeled static (css and images) and templates.

## Skills Developed
1. Python
2. HTML
3. CSS
4. OAuth
5. Flask Framework

## Installation
In order to run this app several steps will need to be completed.  First we will need to check dependencies and install any not already installed.

## Dependencies
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

## How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into your Vagrant VM (`vagrant ssh`)
5. Navigate to `cd/vagrant` as instructed in terminal
6. Import the requests by running: sudo pip install requests
7. Setup application database `python /projectCatalog/database_setup.py`
8. Insert data by running lotsofitems.py`
9. Run application using `python /projectcatalog/project.py`
10. Access the application locally using http://localhost:8000

*Optional step(s)

## Using Google Login
To use Google login there are additional steps:

1. Go to [Google Dev Console](https://console.developers.google.com)
2. Sign up or Login if prompted
3. Go to Credentials
4. Select Create Crendentials > OAuth Client ID
5. Select Web application
6. Enter name 'Project Catalog'
7. Authorized JavaScript origins = 'http://localhost:8000'
8. Authorized redirect URIs = 'http://localhost:8000/login' && 'http://localhost:8000/gconnect'
9. Select Create
10. Copy the Client ID and paste it into the `data-clientid` in login.html
11. On the Dev Console Select Download JSON
12. Rename JSON file to client_secrets.json
13. Place JSON file in project catalog directory that you cloned from here
14. Run application using `python /projectCatalog/project.py`


## JSON Endpoints
Additionally the app provides API endpoints with JSON payloads:

Catalog JSON: `/catalog/JSON`
    - Displays all categories

Categories JSON: `/catalog/<int:category_id>/JSON`
    - Displays items for a specific category

Category Item JSON: `/catalog/<int:category_id>/<int:item_id>/JSON`
    - Displays a specific category item.