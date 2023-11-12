# **Project Name: Inventory Analysis and Management System**

**Project Description:**

The Inventory Analysis and Management System is a Python program designed to analyze and manage product inventory stored in an Excel spreadsheet. It utilizes the openpyxl library for Excel interaction. This system provides insightful information about inventory, including total value per supplier, the number of products with inventory under 10 units, and the number of suppliers per company.

**Key Features:**

**1. Total Inventory Value per Company:**
   - Calculates and displays the total inventory value for each supplier/company.
   
**2. Products with Inventory Under 10:**
   - Identifies and alerts the user about products with inventory levels falling below 10 units.
   - Recommends reordering for products with low stock.
   
**3. Number of Suppliers per Company:**
   - Counts and displays the number of suppliers for each company.
   - Dynamically updates as new suppliers are encountered.

**How It Works:**

1. The program loads an Excel file containing inventory information into the `product_list` variable.

2. Iterates through each row in the spreadsheet, extracting relevant data such as supplier name, inventory, price, and product number.

3. Updates the `products_per_supplier` dictionary to keep track of the number of products each supplier provides.

4. Calculates the total inventory value for each supplier and updates the `total_value_per_supplier` dictionary. 

5. Identifies products with inventory levels under 10 units, prompting a reorder recommendation.

6. Creates a new column in the Excel file, storing the calculated inventory value for each product.

7. Outputs the number of suppliers per company, total inventory value per supplier, and products requiring attention.

8. Saves the updated Excel file with a new name, preventing data loss.

**Usage:**

- Ensure that the Excel file with inventory data is in the specified location.
- Run the program. 
- View the console output for information on suppliers, total inventory value, and products requiring attention.
- Check the `updated_excel.xlsx` file for the added inventory value column.

**Project Benefits:**

- **Inventory Insight:** Provides a comprehensive overview of inventory, facilitating informed decision-making.
- **Supplier Management:** Dynamically tracks and manages the number of suppliers associated with each company.
- **Reorder Recommendations:** Alerts users about products with low stock, prompting timely reordering.
- **Excel Interaction:** Demonstrates practical use of the openpyxl library for Excel data manipulation.
