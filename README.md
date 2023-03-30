# school_management
 Basic school management system using the Django Rest Framework
This is a basic school management system built using Django Rest Framework. It allows schools to sign up, add students for grades 1-12 in bulk, and manage student accounts. Admins can view schools onboarded, filter students based on school and grade, and add grades.

Installation and Setup
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/school-management-system.git
Navigate to the project directory:
bash
Copy code
cd school-management-system
Create a virtual environment:
bash
Copy code
python -m venv env
Activate the virtual environment:
bash
Copy code
source env/bin/activate (for Linux/MacOS) or env\Scripts\activate (for Windows)
Install the required packages:
Copy code
pip install -r requirements.txt
Set up the database:
Copy code
python manage.py migrate
Run the server:
Copy code
python manage.py runserver
The server will start running at http://127.0.0.1:8000/.

API Documentation
The API documentation is available in the Postman collection school-management-system.postman_collection.json in the root directory of the project.

Technologies Used
Django
Django Rest Framework
SQLite
Contributors
Your name (@your-username) - email@example.com
