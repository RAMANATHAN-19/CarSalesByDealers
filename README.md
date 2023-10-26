# Car Sales By Dealers

Car Sales and Service System is a web-based application developed using Django, designed to manage car sales and api operations.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)

## Features

- **User Authentication**: Secure user authentication and management system.
- **Product Management**: Add and manage car products, with real-time updates.
- **Sales Management**: Record and manage sales transactions.
- **Dynamic Dashboard**: Provides an overview of key statistics and actions for users.
- **Responsive Design**: The web interface is responsive for various screen sizes.
- **Customization**: Easily customize the application to your specific needs.

## Getting Started

### Prerequisites

- Python 3.8.10
- Django 4.2.6

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RAMANATHAN-19/CarSalesByDealers.git


## Deployment

To deploy this project run

```Create a virtual environment (optional but recommended):

python3 -m venv venv

source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Apply the database migrations:

python manage.py migrate

Create a superuser account for initial access to the admin panel:

python manage.py createsuperuser

OR use this
USERNAME : admin
PASSOWRD : admin123

Collect the static files:

python manage.py collectstatic

Start the development server:

python manage.py runserver

You should now be able to access the application by opening your web browser and navigating to http://localhost:8000/.


```


## Acknowledgements

 Usage
Access the admin panel by navigating to http://localhost:8000/admin/ and log in with the superuser account.
To access the user interface, visit http://localhost:8000/.
Configuration
The project's settings can be configured in the settings.py file, including database settings, static and media file settings, and more.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request to the main repository.

## Running Tests

To run tests, run the following command

  TO RUN THE UI
```
  http://127.0.0.1:8000/
```

TO RUN THE DJANGO ADMIN
```
http://127.0.0.1:8000/admin/
```

  TO RUN THE API
```
http://127.0.0.1:8000/api/v1/
```
## API Endpoints:

### Customer Details API

- **Endpoint:** `/api/customer_details/`
- **Description:** Get a list of customer details.
- **Methods:** GET, POST

### Products API

- **Endpoint:** `/api/products/`
- **Description:** Get a list of products.
- **Methods:** GET, POST

### Sales API

- **Endpoint:** `/api/sales/`
- **Description:** Get a list of sales records.
- **Methods:** GET, POST

https://github.com/RAMANATHAN-19/CarSalesByDealers/assets/148554695/62473593-531e-411a-bdd8-f6c4bcc1b9b1
