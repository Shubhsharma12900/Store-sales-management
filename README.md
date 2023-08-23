Setting Up the Project

Fetching the Project Repository
To start, clone the "Store-sales-management" repository from GitHub. Launch a terminal and navigate to your chosen project directory. Then, run this 

$ git clone https://github.com/Shubhsharma12900/Store-sales-management.git
This will create a new "Store-sales-management" directory containing all project files.

Creating an Isolated Environment
Go into the "Store-sales-management" directory and create a virtual environment for the project. Use these commands:

$ cd Store-sales-management
$ python3 -m venv venv
$ source venv/bin/activate

This will establish a new virtual environment and activate it.

Installing Necessary Dependencies
With the virtual environment active, install the required dependencies:

$ pip install -r requirements.txt
This installs the essential packages listed in "requirements.txt."

Setting Up the Database
The "Jodhpur Handloom" project relies on MySQL as its database. Before running the application, set up a MySQL database and configure the project:
a. Creating a MySQL Database

Using your MySQL client, create a new database for the project:

CREATE DATABASE dbname;
b. Configuring Database Connection

In the project directory, open "config.py" and update these variables with your MySQL database credentials:


DB_HOST = 'localhost'
DB_USER = 'your_mysql_username'
DB_PASSWORD = 'your_mysql_password'
DB_NAME = 'dbname'
Running the Application
You can now run the "dbname" application with the configured database. In the terminal, execute:

$ python app.py
This starts the Flask development server, and you'll see:

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Open your web browser, visit http://127.0.0.1:5000/, and you'll find the "Jodhpur handloom" homepage.
