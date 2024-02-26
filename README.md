# Webscraping-Project
My Webscraping Project takes a specific item from eBay and scrapes all the prices and sellers. Then it takes a user entered maximum to find an item within your price range and then shows all the prices you can buy your item from, as well as seller, number of reviews, and the rating the reviewers gave the product.
When entering the product you want, replace any spaces with + signs, and when entering the maximum price do not type in any $ signs or cents. If the price is not listed the program will tell you to click on the item in eBay to find the price. Any items that have a range in price will not be shown if the maximum of the price range is larger than the user entered maximum price. 
This works best when searching for a specific item within a specific price range in a short amount of time.
To use the code, you will need to install pip and requests in your terminal. This is so that the program can access eBay.

Note: This will only work on eBay and cannot work on amazon, as it will not allow the get command to work.
