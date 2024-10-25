# Shivakumar_BesantTech_API_Project
Placement Project from  Shivakumar R (Besant Tech) 





#Engagement API
Overview
Purpose: The Engagement API is designed to manage engagement data related to posts and products stored in a PostgreSQL database. It provides endpoints for creating posts, products, collections, mapping products to posts, and retrieving top posts and products based on views and total view duration.




#Prerequisites
1. Python 3.12: Ensure you have Python version 3.12 installed on your machine.
2. PostgreSQL: You need to have PostgreSQL installed and running. You should also create a database named engagement (or update the code to reflect your database name).
3. Required Libraries: Install the necessary Python libraries, specifically Flask for creating the web API and psycopg2 for PostgreSQL database connectivity.




#Database Setup
1. Drop Existing Tables: If you have previously created tables that you want to refresh, run the provided SQL commands to drop the old tables. This ensures there are no conflicts with existing data.

2. Create Tables: After dropping the old tables, run the SQL commands to create new ones. The tables defined are:

    a. engagement_post: Stores posts with fields for ID, tenant ID, title, content URL, views, and creation timestamp.
    b. engagement_post_product: Stores product details including ID, product name, image, and SKU number.
    c. engagement_post_product_mapping: Maps posts to products, containing IDs for both and a creation timestamp.
    d. collection: Contains collections with IDs and names.
    e. engagement_post_collection: Links posts to collections, including IDs for both, duration of views in seconds, and a creation timestamp.



#API Endpoints

1.  POST /posts:
      Purpose: Create a new post.
      Input: Requires a JSON body with tenant_id, title, and content_url.
      Response: Returns a message confirming successful creation and the ID of the new post.


2. POST /products:
      Purpose: Add a new product to the database.
      Input: Requires a JSON body with product_name, product_image, and sku_number.
      Response: Returns a message confirming successful creation and the ID of the new product.



3. POST /collections:
      Purpose: Create a new collection.
      Input: Requires a JSON body with collection_name.
      Response: Returns a message confirming successful creation and the ID of the new collection.


4. POST /map_product:
      Purpose: Link a specific product to a specific post.
      Input: Requires a JSON body with post_id and product_id.
      Response: Returns a message confirming successful mapping and the ID of the new mapping.


5. GET /top_posts/<tenant_id>:
      Purpose: Retrieve the top 5 posts for a specific tenant, ordered by views.
      Input: The tenant ID is passed as a URL parameter.
      Response: Returns a JSON array of the top 5 posts.


6. GET /top_products/<tenant_id>:
      Purpose: Retrieve the top 5 products by total view duration for a specific tenant.
      Input: The tenant ID is passed as a URL parameter.
      Response: Returns a JSON array of the top 5 products along with their total watched duration.


# Using Postman

  1. Open Postman: Launch the application on your computer.

  2. Create a New Request: Select the appropriate HTTP method (GET or POST) based on the action you want to perform.

  3. Enter the API Endpoint URL: For example, to create a post, you would enter http://localhost:5000/posts in the request URL field.

# For POST Requests:
Click on the Body tab.
Choose the raw option and set the format to JSON.
Enter the JSON data required for the request (e.g., {"tenant_id": 1, "title": "My Post", "content_url": "http://example.com"}).
Send the Request: Click the Send button to execute the request. You will see the server’s response in the lower pane, which should indicate the success of the operation or provide error messages if applicable.
Running the Application
Start the Flask Application:
Open a terminal or command prompt.
Navigate to the directory containing your Flask application file (e.g., app.py).
Run the command python app.py to start the server.



#Access the API:
Open your web browser or Postman and go to http://localhost:5000 to interact with the API endpoints.
