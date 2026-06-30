'''
-------------------------------------------------Shopping Cart Billing System----------------------------------------
Problem Statement
A supermarket allows a customer to purchase multiple products.
The customer first enters the number of products.
For each product, enter:
• Product Name
• Quantity
• Price per Unit
Finally display:
• Individual Product Cost
• Total Bill Amount
• Most Expensive Product
• Cheapest Product
• Average Product Cost
----------------------------------------------------------------
Sample Output
Enter the number of products: 3
Enter product name: Apple
Enter quantity: 5
Enter price per unit: 50
Enter product name: Banana
Enter quantity: 10
Enter price per unit: 20
Enter product name: Orange
Enter quantity: 8
Enter price per unit: 30
-------------------------------------------------
Individual Product Cost:
Apple: 250
Banana: 200
Orange: 240
-------------------------------------------------
Total Bill Amount: 690
Most Expensive Product: Apple
Cheapest Product: Banana
Average Product Cost: 230.0
-------------------------------------------------
------------------------------------------Coding----------------------------------------
'''
# Input number of products
n = int(input("Enter the number of products: "))

# Initialize variables
product_names = []
product_costs = []
total_bill = 0

# Input product details
for i in range(1, n + 1):
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price_per_unit = int(input("Enter price per unit: "))
    
    # Calculate individual product cost
    product_cost = quantity * price_per_unit
    
    # Store product information
    product_names.append(product_name)
    product_costs.append(product_cost)
    total_bill = total_bill + product_cost

print("-------------------------------------------------")

# Display individual product costs
print("Individual Product Cost:")
for i in range(n):
    print(f"{product_names[i]}: {product_costs[i]}")

print("-------------------------------------------------")

# Find most expensive and cheapest product
max_cost = max(product_costs)
min_cost = min(product_costs)
most_expensive_index = product_costs.index(max_cost)
cheapest_index = product_costs.index(min_cost)
most_expensive_product = product_names[most_expensive_index]
cheapest_product = product_names[cheapest_index]

# Calculate average product cost
average_product_cost = total_bill / n

# Display results
print("Total Bill Amount:", total_bill)
print("Most Expensive Product:", most_expensive_product)
print("Cheapest Product:", cheapest_product)
print("Average Product Cost:", average_product_cost)
print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------