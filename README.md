# products


This is the repo for the products functionality. 

This endpoint will allow you to create, query, update and delete a product from the database. You can query products by ID, Name or Category.

All responses are in JSON format.

## URL
https://products/

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