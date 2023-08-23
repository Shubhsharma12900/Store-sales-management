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
![Screenshot (250)](https://github.com/Shubhsharma12900/Store-sales-management/assets/72346489/8aea0466-6810-42a6-bcbd-42a9da2a1117)
![Screenshot (244)](https://github.com/Shubhsharma12900/Store-sales-management/assets/72346489/a9e40e99-0dd0-4de2-a327-d38ecd44fa29)
![Screenshot (245)](https://github.com/Shubhsharma12900/Store-sales-management/assets/72346489/1a3fec81-f78f-48f8-93f2-f30a4d9460cc)
![Screenshot (246)](https://github.com/Shubhsharma12900/Store-sales-management/assets/72346489/abc8e049-7a53-4b31-8710-b25632f218f9)
![Screenshot (247)](https://github.com/Shubhsharma12900/Store-sales-management/assets/72346489/263f44db-2e2d-4083-bf14-d29158ee50bd)
![Screenshot (248)](https://github.com/Shubhsharma12900/Store-sales-management/assets/72346489/bc4a9a06-3d40-490e-b0d2-8f655f07f9dd)
![Screenshot (249)](https://github.com/Shubhsharma12900/Store-sales-management/assets/72346489/9cdd1886-bbd1-4262-9d81-4792004664bd)
