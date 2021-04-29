Feature: The Product store service back-end
    As a Product Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my Products

Background:
    Given the following Products
        | id | sku | name       | category | short_description | price | available | enabled |
        |  1 | 001 | iPhone     | phone    | Apple iphone      | 100   | true      | false   |
        |  2 | 002 | MacBook    | computer | Apple laptop      | 200   | true      | true    | 
        |  3 | 003 | Surface    | computer | Microsoft Laptop  | 300   | false     | true    |

Scenario: The server is running
    When I visit the "Home Page"
    Then I should see "Product Demo RESTful Service" in the title
    Then I should not see "404 Not Found"

Scenario: Create a Product Successfully
    When I visit the "Home Page"
    And I set the "Sku" to "004"
    And I set the "Name" to "Peloton Bike"
    And I set the "Category" to "Fitness"
    And I set the "Short Description" to "Exercise bike with digital display"
    And I set the "Price" to "1000"
    And I set the "Rating" to "5"
    # And I set the "Likes" to "10"
    And I select "True" in the "Available" dropdown
    And I select "True" in the "Enabled" dropdown
    And I press the "Create" button
    Then I should see the message "Success"

Scenario: List all Products
    When I visit the "Home Page"
    And I press the "Search" button
    Then I should see "iPhone" in the results
    And I should see "MacBook" in the results
    And I should not see "Airpods" in the results

Scenario: Retreive a Product by ID
    When I visit the "Home Page"
    And I set the "Sku" to "005"
    And I set the "Name" to "Peloton Bike"
    And I set the "Category" to "Fitness"
    And I set the "Short Description" to "Exercise bike with digital display"
    And I set the "Price" to "1000"
    And I set the "Rating" to "5"
    And I select "True" in the "Available" dropdown
    And I select "True" in the "Enabled" dropdown
    And I press the "Create" button
    Then I should see the message "Success"
    And I copy the "ID" field
    And I press the "Clear" button
    And I paste the "ID" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Peloton" in the "Name" field

Scenario: Search for iPhone
    When I visit the "Home Page"
    And I set the "Name" to "iPhone"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "iPhone" in the results

Scenario: Search for computer
    When I visit the "Home Page"
    And I set the "Category" to "computer"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "MacBook" in the results
    And I should see "Surface" in the results

Scenario: Search by available
    When I visit the "Home Page"
    And I select "True" in the "Available" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "iPhone" in the results
    And I should see "MacBook" in the results

Scenario: Search by rating
    When I visit the "Home Page"
    And I set the "Rating" to "4"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "MacBook" in the results

Scenario: Delete a Product
    When I visit the "Home Page"
    And I set the "Name" to "iPhone"
    And I press the "Search" button
    And I copy the "ID" field
    And I press the "Clear" button
    And I paste the "ID" field
    When I press the "Delete" button
    Then I should see the message "Deleted"

Scenario: Update a Product
    When I visit the "Home Page"
    And I set the "Name" to "iPhone"
    And I press the "Search" button
    And I copy the "ID" field
    And I press the "Clear" button
    And I paste the "ID" field
    And I set the "Short Description" to "iPhone 12"
    When I press the "Update" button
    Then I should see the message "Success"
    
Scenario: Like a Product
    When I visit the "Home Page"
    And I set the "Name" to "iPhone"
    And I press the "Search" button
    And I copy the "ID" field
    And I press the "Clear" button
    And I paste the "ID" field
    When I press the "Like" button
    Then I should see the message "Success"

Scenario: Disable a Product
    When I visit the "Home Page"
    And I set the "Name" to "iPhone"
    And I press the "Search" button
    And I copy the "ID" field
    And I press the "Clear" button
    And I paste the "ID" field
    When I press the "Disable" button
    Then I should see the message "Success"
    
Scenario: Create a Product Unsuccessfully
    When I visit the "Home Page"
    And I set the "Sku" to "005"
    And I set the "Name" to "Airpods Max"
    And I set the "Short Description" to "New Airpods over ear headphones"
    And I select "True" in the "Available" dropdown
    And I select "True" in the "Enabled" dropdown
    And I press the "Create" button
    Then I should see the message "Error"