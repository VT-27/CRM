**Django CRM Application**

This project is a basic Customer Relationship Management (CRM) system built using Django and MySQL. It includes essential features like user authentication (login, logout, and registration), and the ability to manage user records.

**Features**
	•	User Authentication:
	•	Login
	•	Logout
	•	User Registration
	•	User Management:
	  •	Add new users/records
	  •	Delete existing users/records
	  •	Update user/record information

**Prerequisites**

Ensure you have the following installed:

	•	Python 3.x
	•	Django
	•	MySQL

 1.	Clone the repository:
    	• git clone <repository-url>
    	• cd <repository-folder>
 2.	Setup MySQL Database
	• Create a MySQL database.
	• Update the settings.py file with your database credentials.
3. Apply Migrations
	• python3 manage.py makemigrations
  	• python3 manage.py migrate
4.	Run the development server:.
  	• python3 manage.py runserver

**Useful Python Django Commands**

  # Run the development server
  python3 manage.py runserver

  # Create migration files based on model changes
  python3 manage.py makemigrations

  # Apply the migrations to the database
  python3 manage.py migrate

  **Useful Git Commands**

  # Navigate to your project folder
cd folder

# Initialize a new Git repository
git init

# Add all files to staging
git add .

# Commit changes
git commit -m "First commit"

# Add the remote repository
git remote add origin <repository-url.git>

# Verify the new remote URL
git remote -v

# Push changes to the remote repository
git push --set-upstream origin master
