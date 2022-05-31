# Project Name

The Ultimate Gallery

## Description

The Ultimate Gallery is  a personal gallery application that allows a person to display their photos for others to see.

## Core Features

<ul>
<li>An admin can upload new photos through an admin panel</li>
<li>An admin can update a photos details</li>
<li>A user can copy an image's link</li>
<li>A user can view images by category and location</li>
<li>A user can view a photo's details</li>
<li>Search for different categories of photos</li>
</ul>


## Prerequisites

<ul>
<li>Python3</li>
<li>Virtual Environment</li>
<li>Django </li>
</ul>

## Technologies and Tools Used

<ul>
<li>Html and Css(bootsrap) </li>
<li>Git Version Control</li>
<li>Javascript </li>
<li>Django</li>
</ul>

## Installation and Setup

Clone the repository below

```
git clone https://github.com/{username}/{repo_name}.git
```

Create and activate a virtual environment. 

  ```
  virtualenv venv --python=python3.9
  source venv/bin/activate
  ```

Install required Dependencies.

  ```
  pip install -r requirements.txt
  Ensure that the virtual  environment is active before making any instalations
  ```

Setup a local database.

  ```
  CREATE DATABASE <your-database-name>
  ```

Create a .env file and add the following.

  ```
  SECRET_KEY='<random_string'
  DEBUG=True
  DB_NAME='<your_database_name'
  DB_USER='<your_database_user>'
  DB_PASSWORD='<your_database_password>'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.127.0.0.1'
  ```

Make a migrations file and migrate.

  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

Run the application

```
python manage.py server.
```

## Live Link

View the deployed site <a href="https://mysterious-depths-66849.herokuapp.com/">here</a>

## License

 MIT
