# django-ecommerce
# Django eCommerce Platform

Welcome to Django-based eCommerce platform! This platform is designed to provide a robust foundation for building and managing your online store.

## Project Overview

ECommerce platform is built on Django, a high-level Python web framework, and includes comprehensive authentication features, making it easy for you to set up a secure and customizable online store.

## Getting Started

Follow these steps to set up the project locally on your machine.

### Prerequisites

Make sure you have the following installed on your system:

- Python (>=3.6)
- Pip (package installer for Python)
- Virtualenv (recommended for isolating project dependencies)

### Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/ecommerce-platform.git
   ```

2. Navigate to the Project Directory:
   ```bash
   cd django-ecommerce
   ```

3. Create and Activate a Virtual Environment (Optional):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use: .\venv\Scripts\activate
   ```

4. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply Database Migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a Superuser Account:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up your admin account.


## Configuration

1. Copy the Example Environment File and Configure Settings:
   ```bash
   cp .env.example .env
   ```
  Open the .env file and update the variables as needed.

2. Configure Static and Media Files:
  ```bash
  python manage.py collectstatic
  ```

## Running the Server

Start the development server:
  ```bash
  python manage.py runserver
  ```

Visit http://127.0.0.1:8000/ in your browser to access the platform.

## Accessing the Admin Panel
To access the Django admin panel, go to http://127.0.0.1:8000/admin/ and log in with the superuser credentials you created earlier.









   
