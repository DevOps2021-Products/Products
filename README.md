[![Build Status](https://travis-ci.org/DevOps2021-Products/products.svg?branch=main)](https://travis-ci.org/DevOps2021-Products/products)
[![codecov](https://codecov.io/gh/DevOps2021-Products/products/branch/main/graph/badge.svg?token=2QKL57K87B)](https://codecov.io/gh/DevOps2021-Products/products)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Products Service


This is the repo for the products functionality. 

This endpoint will allow you to create, query, update and delete a product from the database. You can query products by ID, Name or Category.

All responses are in JSON format.

## Installation Instructions

This service uses **Vagrant** and **VirtualBox**. Please download and install if it is not already installed on your machine.

[VirtualBox](https://www.virtualbox.org/)

[Vagrant](https://www.vagrantup.com/)

After you clone the repo, spin up a vagrant instance:

```bash
git clone https://github.com/DevOps2021-Products/products.git
cd products
vagrant up
vagrant ssh
cd /vagrant
FLASK_APP=service:app flask run -h 0.0.0.0
```

Shutting down vagrant
``` bash
exit
vagrant halt
```

You can set the environment variable FLASK_APP using a `.env` file. An example environment is located in the file `dot-env-example`.

### Database Schema

Database Used: PostgreSQL

### Product Data Model:

|  Column  |  Type  | Constraints  |
| :---------: | :---------: | :------------: | 
| id | Integer | Primary Key |
| sku | Integer | |
| name | String | |
| category | String | |
| short_description | String | |
| long_description | String | |
| price | Double | |
| rating | Integer | |
| stock_status | Boolean | |

### Testing
Run the tests using nosetests
```bash
nosetests
```
If your bash shell supports colors, you will see passing tests in green and failing tests in red.
Running Nose automatically runs a coverage tool and presents a coverage report. This report indicates the percentage of the code that was tested and will appear once the tests have finished. Lines of code that were untested will appear next to the percentage of coverage.

## Supported Methods

### GET /products/<product_id>
Retrieves Products from the database
- Product ID must be an integer.
- If no Product ID is supplied, will return all products.
- Supplying a Product ID will return the associated product.

Response Body:
```
{
    "id": 123,
    "sku": 12345,
    "name": "Chocolate Bar",
    "category": "Food",
    "short_description": "Dark Chocolate",
    "long_description": "The most delicious chocolate bar you've ever had",
    "price": 2.50,
    "rating": 5,
    "stock_status": true
}
```
### POST /products/
Creates a new Product and adds it to the database
- Content Type: application/json
  
Request Body:
```
{
    "id": 123,
    "sku": 12345,
    "name": "Chocolate Bar",
    "category": "Food",
    "short_description": "Dark Chocolate",
    "long_description": "The most delicious chocolate bar you've ever had",
    "price": 2.50,
    "rating": 5,
    "stock_status": true
}
```

### PUT /products/<product_id>
Updates an existing Product in the database
- Content Type: application/json
- Product ID must be an integer
- Will return the Product object after updating
- If no Product ID is supplied or does not match an existing record an error will return a 404 error

Response Body:
```
{
    "id": 123,
    "sku": 12345,
    "name": "Chocolate Bar",
    "category": "Food",
    "short_description": "Dark Chocolate",
    "long_description": "The most delicious chocolate bar you've ever had",
    "price": 2.50,
    "rating": 5,
    "stock_status": true
}
```

### DELETE /products/<product_id>
Deletes an existing Product in the database
- Product ID must be an integer
- Will return a 204 error if the deletion is successful
