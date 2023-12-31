# Djangommerce

Djangommerce is an online market hub built using Django, designed to allow users to post items for sale, set prices, manage availability, and communicate with potential buyers through a built-in chat system. The primary aim of Djangommerce is to provide a platform for users to showcase their items.

![Djangommerce](https://i.postimg.cc/1t8619dx/merged-horizontally.png "Djangommerce demo")

## Application Architecture

Djangommerce follows the MVT (Model-View-Template) architecture of Django Web Framework:

- **Models**: Define the structure of the database including items, users, chat messages, etc.
- **Views**: Manage the business logic, process user input, and interact with the models.
- **Templates**: Handle the presentation logic, rendering templates, and passing data to frontend.

## Development Setup

### Prerequisites

- Python 3.10
- Pipenv. (To install pipenv, run `pip install pipenv`)

### Local setup

1. Clone the repo and move into the project's directory:
   ```
   git clone https://github.com/yeroldsan/djangommerce
   cd djangommerce
   ```

2. Follow the instructions in the _.env.example_ file.

3. Create a virtual environment, and install packages the required packages:
   ```
   pipenv shell
   pipenv install
   ```

4. Apply the database migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server (running by default on **http://localhost:8000**):
   ```
   python manage.py runserver
   ```
