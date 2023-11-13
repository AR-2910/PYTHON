# **Project Name: Web Scraper for Product Price Comparison**

**Project Description:**

The Web Scraper for Product Price Comparison is a Python program that extracts and compares product prices from Amazon and Flipkart. The script utilizes web scraping techniques to gather information and presents the user with the lowest-priced option. It incorporates the `requests`, `pandas`, and `BeautifulSoup` libraries for web interaction, data manipulation, and HTML parsing.

**Key Features:**

**1. Amazon Scraper:**
   - Scrapes Amazon for product details, including title, price, and link.
   - Converts prices to Indian Rupees and incorporates a 2-second delay between requests.

**2. Flipkart Scraper:**
   - Scrapes Flipkart for product details, including title, price, and link.
   - Formats prices in Indian Rupees and introduces a 2-second delay to avoid potential issues.

**3. Price Comparison:**
   - Creates DataFrames for Amazon and Flipkart data.
   - Determines the lowest-priced item between the two platforms.

**How It Works:**

1. The program defines a user-agent for headers to mimic a browser request.

2. Two functions, `scrape_amazon` and `scrape_flipkart`, are created to extract product information from Amazon and Flipkart, respectively.

3. The `lowest_price` function calculates and returns the lowest-priced item between Amazon and Flipkart.

4. The script takes input product name from the user, defaulting to "iphone" if none is provided.

5. Amazon and Flipkart are scraped for product details using the defined functions.

6. The lowest-priced item is determined and displayed, along with the product details.

7. The collected data is combined into a DataFrame and saved to a CSV file named "product_prices.csv."

**Usage:**

- Run the program.
- View the console output for the lowest-priced item and its details.
- Check the generated CSV file ("product_prices.csv") for a comprehensive list of product details.

**Project Benefits:**

- **Product Price Comparison:** Enables users to compare prices of a specific product on Amazon and Flipkart.
- **Data Manipulation:** Utilizes pandas for creating, manipulating, and saving data in a structured format.
- **Web Scraping Techniques:** Demonstrates practical use of web scraping with BeautifulSoup and requests.
- **User-Agent Simulation:** Includes headers to mimic a browser request for web scraping.

**Limitations and Notes:**

- **503 Errors from Amazon:** The scraper is currently experiencing 503 errors from Amazon, limiting its functionality. As a result, it may not run smoothly as-is.

- **Troubleshooting Attempts:** Attempts to address the 503 issue include introducing delays between requests. However, further solutions such as proxies, user-agent headers, and IP address rotation techniques might be explored.

- **Next Steps for Troubleshooting:** If you encounter issues, consider trying a proxy service, adjusting user-agent headers, or implementing IP address rotation techniques.

- **Disclaimer:** The purpose of this project is to showcase web scraping skills and is not intended to promote scraping Amazon/Flipkart against their Terms of Service.
