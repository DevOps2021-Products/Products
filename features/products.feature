Feature: The Product store service back-end
    As a Product Store Owner
    I need a RESTful catalog service
    So that I can keep track of all my Products

Background:
    Given the following Products
        | sku | name       | category | short_description | price | stock_status | enabled |
        | 001 | iPhone     | phone    | Apple iphone      | 100   | true         | false   |
        | 002 | MacBook    | computer | Apple laptop      | 200   | true         | true    |
        | 003 | Surface    | computer | Microsoft Laptop  | 300   | false        | true    |

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
    And I set the "Likes" to "10"
    And I select "True" in the "Available" dropdown
    And I select "True" in the "Enabled" dropdown
    And I press the "Create" button
    Then I should see the message "Success"
    # When I copy the "Id" field
    # And I press the "Clear" button
    # Then the "Id" field should be empty
    # And the "Sku" field should be empty
    # And the "Name" field should be empty
    # And the "Category" field should be empty
    # And the "Short Description" field should be empty
    # And the "Price" field should be empty
    # And the "Stock Status" field should be empty
    # And the "Enabled" field should be empty 
    # When I paste the "Id" field
    # And I press the "Retrieve" button
    # Then I should see "004" in the "Sku" field
    # And I should see "Peloton Bike" in the "Name" field
    # And I should see "Fitness" in the "Category" field
    # And I should see "Exercise bike with digital display" in the "Short Description" field
    # And I should see "1000" in the "Price" field
    # And I should see "True" in the "Stock Status" dropdown
    # And I should see "True" in the "Enabled" dropdown

    Scenario: Create a Product Unsuccessfully
    When I visit the "Home Page"
    And I set the "Sku" to "004"
    And I set the "Name" to "Peloton Bike"
    And I set the "Short Description" to "Exercise bike with digital display"
    And I set the "Price" to "1000"
    And I select "True" in the "Available" dropdown
    And I select "True" in the "Enabled" dropdown
    And I press the "Create" button
    Then I should see the message "Error"

Scenario: Delete a Product
    When I visit the "Home Page"
    And I set the "Name" to "Surface"
    And I press the "Search" button
    Then I should see "003" in the "Sku" field
    And I should see "Surface" in the "Name" field
    When I copy the "Id" field                    
    And I press the "Clear" button               
    And I paste the "Id" field  
    When I press the "Delete" button
    Then I should see the message "Deleted"
  #  And I should see "kitty" in the results
  #  And I should not see "leo" in the results  When I visit the "Home Page"
  #  And I press the "Search" button
  #  Then I should see "fido" in the results
  #  And I should see "kitty" in the results
  #  And I should not see "leo" in the results

Scenario: List all Products
    When I visit the "Home Page"
    And I press the "Search" button
    Then I should see "fido" in the results
    And I should see "kitty" in the results
    And I should not see "leo" in the results

Scenario: List all dogs
    When I visit the "Home Page"
    And I set the "Category" to "dog"
    And I press the "Search" button
    Then I should see "fido" in the results
    And I should not see "kitty" in the results
    And I should not see "leo" in the results

Scenario: Update a Product
    When I visit the "Home Page"
    And I set the "Name" to "fido"
    And I press the "Search" button
    Then I should see "fido" in the "Name" field
    And I should see "dog" in the "Category" field
    When I change "Name" to "Boxer"
    And I press the "Update" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see "Boxer" in the "Name" field
    When I press the "Clear" button
    And I press the "Search" button
    Then I should see "Boxer" in the results
    Then I should not see "fido" in the results

