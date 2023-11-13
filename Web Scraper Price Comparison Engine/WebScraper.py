import requests  # Import the requests library for making HTTP requests
import pandas as pd  # Import the pandas library for data manipulation and analysis
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing
import time  # Import the time module for introducing delays

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
# Define headers with a user-agent to mimic a browser request

def scrape_amazon(product_name):
    amazon_results=[]
    amazon_url=f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
    time.sleep(2)  # Introduce a 2-second delay to avoid rate-limiting or IP blocking
    response_1=requests.get(amazon_url, headers=headers)  # Make a GET request to Amazon
    response_1.raise_for_status()  # Raise an exception if the HTTP request was unsuccessful

    soup = BeautifulSoup(response_1.text,"html.parser")  # Create a BeautifulSoup object for HTML parsing

    products=soup.find_all("div",class_="s-include-content-margin")  # Extract product details from HTML
    for product in products:
        title1=product.find("span",class_="a-text-normal").text.strip()  # Extract product title
        price1=product.find("span",class_="a-offscreen").text.strip()  # Extract product price

        price1=price1.replace('$','').replace(',','')  # Clean up price formatting
        price_rupees=f"₹{float(price1) * 83:.2f}"  # Convert price to Indian Rupees

        link1=product.find("a",class_="a-link-normal")["href"]  # Extract product link
        amazon_results.append([title1,price_rupees,link1])  # Append product details to the list

    return amazon_results

def scrape_flipkart(product_name):
    flipkart_results=[]
    flipkart_url=f"https://www.flipkart.com/search?q={product_name.replace(' ', '+')}"
    time.sleep(2)  # Introduce a 2-second delay to avoid rate-limiting or IP blocking
    response_2=requests.get(flipkart_url, headers=headers)  # Make a GET request to Flipkart
    response_2.raise_for_status()  # Raise an exception if the HTTP request was unsuccessful

    soup = BeautifulSoup(response_2.text,"html.parser")  # Create a BeautifulSoup object for HTML parsing

    products=soup.find_all("div",class_="_2kHMtA")  # Extract product details from HTML
    for product in products:
        title2=product.find("a",class_="IRpwTa").text.strip()  # Extract product title
        price2=product.find("div",class_="_30jeq3").text.strip()  # Extract product price

        price2 = price2.replace('₹', '').replace(',', '')  # Clean up price formatting
        price_in_rupees = f"₹{price2}"  # Format price in Indian Rupees

        link2="https://www.flipkart.com" + product.find("a", class_="_1fQZEK")["href"]  # Extract product link
        flipkart_results.append([title2,price2,link2])  # Append product details to the list

    return flipkart_results

def lowest_price(amazon_data,flipkart_data):
    amazon_df=pd.DataFrame(amazon_data,columns=["Title","Price","Link"])  # Create a DataFrame for Amazon data
    flipkart_df=pd.DataFrame(flipkart_data,columns=["Title","Price","Link"])  # Create a DataFrame for Flipkart data

    amazon_df["Price"] = amazon_df["Price"].str.replace('₹', '').astype(float)  # Convert Amazon prices to float
    flipkart_df["Price"] = flipkart_df["Price"].str.replace('₹', '').astype(float)  # Convert Flipkart prices to float

    lowest_amazon=amazon_df.loc[amazon_df["Price"].idxmin()]  # Find the lowest-priced item on Amazon
    lowest_flipkart=flipkart_df.loc[flipkart_df["Price"].idxmin()]  # Find the lowest-priced item on Flipkart

    return lowest_amazon,lowest_flipkart

# Input product name , if none provided , default product "Iphone" chosen
product_name=input("Enter Product Name: ") or "iphone"

amazon_data=scrape_amazon(product_name)  # Scrape Amazon for product information
flipkart_data=scrape_flipkart(product_name)  # Scrape Flipkart for product information

lowest_amazon, lowest_flipkart=lowest_price(amazon_data,flipkart_data)  # Find the lowest-priced item

combined_data=amazon_data+flipkart_data  # Combine data from both Amazon and Flipkart

combined_df=pd.DataFrame(combined_data,columns=["Title","Price","Link"])  # Create a DataFrame for combined data

csv_file="product_prices.csv"  # Define the CSV file name
combined_df.to_csv(csv_file,index=False)  # Save combined data to a CSV file

lowest=lowest_amazon if lowest_amazon["Price"]<lowest_flipkart["Price"] else lowest_flipkart  # Determine the overall lowest-priced item

# Display lowest price details
print(f"Lowest price at {lowest['Link']} for {lowest['Title']} at {lowest['Price']}")
print("PRODUCT DETAILS: ")
print(lowest)
