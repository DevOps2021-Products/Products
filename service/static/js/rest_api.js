$(function () {

    // ****************************************
    //  U T I L I T Y   F U N C T I O N S
    // ****************************************

    // Updates the form with data from the response
    function update_form_data(res) {
        $("#product_id").val(res.id);
        $("#product_name").val(res.name);
        $("#product_category").val(res.category);
        if (res.available == true) {
            $("#product_available").val("true");
        } else {
            $("#product_available").val("false");
        }
        if (res.enabled == true) {
            $("#product_enabled").val("true");
        } else {
            $("#product_enabled").val("false");
        }
        $("#product_sku").val(res.sku);
        $("#product_short_description").val(res.short_description);
        $("#product_available").val(res.available);
        $("#product_price").val(res.price);
        $("#product_rating").val(res.rating);
        $("#product_long_description").val(res.long_description);
        $("#product_likes").val(res.likes);
    }

    /// Clears all form fields
    function clear_form_data() {
        $("#product_id").val(0);
        $("#product_name").val("");
        $("#product_category").val("");
        $("#product_available").val("");
        $("#product_sku").val("");
        $("#product_short_description").val("");
        $("#product_long_description").val("");
        $("#product_price").val("");
        $("#product_rating").val(0);
        $("#product_available").val("");
        $("#product_enabled").val("");
        $("#product_likes").val(0);
    }

    // Updates the flash message area
    function flash_message(message) {
        $("#flash_message").empty();
        $("#flash_message").append(message);
    }

    // ****************************************
    // Create a product
    // ****************************************

    $("#create-btn").click(function () {

        var sku = $("#product_sku").val();
        var name = $("#product_name").val();
        var category = $("#product_category").val();
        var short_description = $("#product_short_description").val();
        // var long_description = $("#product_long_description").val();
        var price = $("#product_price").val();
        var rating = $("#product_rating").val();
        var available = $("#product_available").val() == "true";
        var enabled = $("#product_enabled").val() == "true";
        // var likes = $("#product_likes").val();

        var data = {
            "sku": sku,
            "name": name,
            "category": category,
            "short_description": short_description,
            // "long_description": long_description,
            "price": price,
            "rating": rating,
            "available": available,
            "enabled": enabled,
            // "likes": likes
        };

        var ajax = $.ajax({
            type: "POST",
            url: "/products",
            contentType: "application/json",
            data: JSON.stringify(data),
        });

        ajax.done(function(res){
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            flash_message(res.responseJSON.message)
        });
    });


    // ****************************************
    // Update a product
    // ****************************************

    $("#update-btn").click(function () {

        var name = $("#product_name").val();
        var sku = $("#product_sku").val();
        var category = $("#product_category").val();
        var price = $("#product_price").val();
        var available = $("#product_available").val() == "true";
        var rating = $("#product_rating").val();
        var short_description = $("$product_short_description").val;
        var enabled = $("#product_enabled").val() == "true";

        var data = {
            "name": name,
            "sku": sku,
            "category": category,
            "price": price,
            "available": available,
            "rating": rating,
            "short_description": short_description,
            "enabled": enabled
        };

        var ajax = $.ajax({
                type: "PUT",
                url: "/products/" + product_id,
                contentType: "application/json",
                data: JSON.stringify(data)
            })

        ajax.done(function(res){
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            flash_message(res.responseJSON.message)
        });

    });

    // ****************************************
    // Retrieve a product
    // ****************************************

    $("#retrieve-btn").click(function () {

        var product_id = $("#product_id").val();

        var ajax = $.ajax({
            type: "GET",
            url: "/products/" + product_id,
            contentType: "application/json",
            data: ''
        })

        ajax.done(function(res){
            //alert(res.toSource())
            update_form_data(res)
            flash_message("Success")
        });

        ajax.fail(function(res){
            clear_form_data()
            flash_message(res.responseJSON.message)
        });

    });

    // ****************************************
    // Delete a product
    // ****************************************

    $("#delete-btn").click(function () {

        var product_id = $("#product_id").val();

        var ajax = $.ajax({
            type: "DELETE",
            url: "/products/" + product_id,
            contentType: "application/json",
            data: '',
        })

        ajax.done(function(res){
            clear_form_data()
            flash_message("product has been Deleted!")
        });

        ajax.fail(function(res){
            flash_message("Server error!")
        });
    });

    // ****************************************
    // Like a product
    // ****************************************

    $("#like-btn").click(function () {

        var product_id = $("#product_id").val();
        var name = $("#product_name").val();
        var sku = $("#product_sku").val();
        var category = $("#product_category").val();
        var price = $("#product_price").val();
        var available = $("#product_available").val() == "true";
        var rating = $("#product_rating").val();
        var short_description = $("$product_short_description").val;
        var enabled = $("#product_enabled").val() == "true";

        var data = {
            "name": name,
            "sku": sku,
            "category": category,
            "price": price,
            "available": available,
            "rating": rating,
            "short_description": short_description,
            "enabled": enabled
        };

        var ajax = $.ajax({
            type: "PUT",
            url: "/products/" + product_id + "/like",
            contentType: "application/json",
            data: JSON.stringify(data)
        })

        ajax.done(function(res){
            clear_form_data()
            flash_message("product has been Liked!")
        });

        ajax.fail(function(res){
            flash_message("Server error!")
        });
    });

    // ****************************************
    // Disable a product
    // ****************************************

    $("#disable-btn").click(function () {

        var product_id = $("#product_id").val();
        var name = $("#product_name").val();
        var sku = $("#product_sku").val();
        var category = $("#product_category").val();
        var price = $("#product_price").val();
        var available = $("#product_available").val() == "true";
        var rating = $("#product_rating").val();
        var short_description = $("$product_short_description").val;
        var enabled = $("#product_enabled").val() == "true";

        var data = {
            "name": name,
            "sku": sku,
            "category": category,
            "price": price,
            "available": available,
            "rating": rating,
            "short_description": short_description,
            "enabled": enabled
        };

        var ajax = $.ajax({
            type: "PUT",
            url: "/products/" + product_id + "/disable",
            contentType: "application/json",
            data: JSON.stringify(data)
        })

        ajax.done(function(res){
            clear_form_data()
            flash_message("product has been Disabled!")
        });

        ajax.fail(function(res){
            flash_message("Server error!")
        });
    });

    // ****************************************
    // Clear the form
    // ****************************************

    $("#clear-btn").click(function () {
        $("#product_id").val("");
        clear_form_data()
    });

    // ****************************************
    // Search for a product
    // ****************************************

    $("#search-btn").click(function () {

        var name = $("#product_name").val();
        var category = $("#product_category").val();
        var available = $("#product_available").val();
        var rating = $("#product_rating").val();

        var queryString = ""

        if (name) {
            queryString += 'name=' + name
        }
        if (category) {
            if (queryString.length > 0) {
                queryString += '&category=' + category
            } else {
                queryString += 'category=' + category
            }
        }
        if (available) {
            if (queryString.length > 0) {
                queryString += '&available=' + available
            } else {
                queryString += 'available=' + available
            }
        }
        if (rating) {
            if (queryString.length > 0) {
                queryString += '&rating=' + rating
            } else {
                queryString += 'rating=' + rating
            }
        }

        var ajax = $.ajax({
            type: "GET",
            url: "/products?" + queryString,
            contentType: "application/json",
            data: ''
        })

        ajax.done(function(res){
            //alert(res.toSource())
            $("#search_results").empty();
            $("#search_results").append('<table class="table-striped" cellpadding="10">');
            var header = '<tr>'
            header += '<th style="width:10%">ID</th>'
            header += '<th style="width:40%">Name</th>'
            header += '<th style="width:40%">Category</th>'
            header += '<th style="width:10%">Available</th></tr>'
            $("#search_results").append(header);
            var firstProduct = "";
            for(var i = 0; i < res.length; i++) {
                var product = res[i];
                var row = "<tr><td>"+product.id+"</td><td>"+product.name+"</td><td>"+product.category+"</td><td>"+product.available+"</td></tr>";
                $("#search_results").append(row);
                if (i == 0) {
                    firstProduct = product;
                }
            }

            $("#search_results").append('</table>');

            // copy the first result to the form
            if (firstProduct != "") {
                update_form_data(firstProduct)
            }

            flash_message("Success")
        });

        ajax.fail(function(res){
            flash_message(res.responseJSON.message)
        });

    });

})
