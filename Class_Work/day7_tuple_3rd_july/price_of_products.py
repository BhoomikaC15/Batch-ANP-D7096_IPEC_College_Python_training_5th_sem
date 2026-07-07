'''
----------------------------------------------Price of Products----------------------------------------------
Write a program to create a tuple of prices of 10 products and display the lowest price, highest price with the name of the product.
Also display the number of products whose price is higher than ₹4000.
---------------------------------------------------------------------
Sample input
Enter the name of the product: Product 1
Enter the price of the product: 2000
Enter the name of the product: Product 2
Enter the price of the product: 5000
-------------------------------------
Sample Output
Lowest Price: ₹2000 (Product 1)
Highest Price: ₹5000 (Product 2)
Number of products with price higher than ₹4000: 1
------------------------------------------------------------------------------------------------
---------------------------------Coding------------------------------------------
'''
products = []
prices = []
# Create a tuple of prices of 10 products 
for i in range(10):
    name = input("Enter the name of the product: ")
    price = float(input("Enter the price of the product: "))
    products.append(name)
    prices.append(price)
products = tuple(products)  
prices = tuple(prices)

# Find the lowest and highest price with the name of the product
min_price = min(prices)
min_price_product = products[prices.index(min_price)]
max_price = max(prices)
max_price_product = products[prices.index(max_price)]
print("-------------------------------------------------")
print("Lowest Price: ", min_price, "(", min_price_product, ")")
print("Highest Price: ", max_price, "(", max_price_product, ")")
print("-------------------------------------------------")

# Count the number of products whose price is higher than ₹4000
count = 0
for i in prices:
    if i > 4000:
        count += 1  
print("Number of products with price higher than ₹4000: ", count)
print("-------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------

