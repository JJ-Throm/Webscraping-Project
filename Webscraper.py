import requests
from bs4 import BeautifulSoup

def scrape_ebay_data(search_query, max_price=None):
    # Base URL for eBay search results
    base_url = 'https://www.ebay.com/sch/i.html'

    # Constructing the query parameters
    params = {'_nkw': search_query}

    if max_price is not None:
        params['_udhi'] = max_price

    # Send an HTTP GET request to the URL with the parameters
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements containing item details
        items = soup.find_all('div', class_='s-item__info')

        # Print the prices and sellers' names
        for item in items:
            # Extract the price
            price_element = item.find('span', class_='s-item__price')
            if price_element:
                # Grabs the integer value of the cost
                price = price_element.text.strip()
                x = price.replace(',', '').replace('$', '')
                y = x.replace('ap item to see current priceSee price', '0')
                if 'to' in y:
                    z = '0'
                else:
                    z = y

                    # Extract the seller's name
                    seller_element = item.find('span', class_='s-item__seller-info-text')
                    if seller_element:
                        seller = seller_element.text.strip()

                      # Print the price and seller if they are within the specified price range
                        if (max_price is None or float(z[1:]) <= max_price):
                            print("Price:", price)
                            print("Seller:", seller)
                            print('-' * 50)

    else:
        print("Failed to retrieve the page.")
# User inputs
search_query = input("Enter the item you want to search for: ")
max_price = float(input("Enter the maximum price (or press Enter to skip): ").strip() or float('inf'))

# Call the function to scrape eBay data
scrape_ebay_data(search_query, max_price)
