'''
-----------------------------------------------Inventory Management---------------------------------------------
Problem Statement: 
Create a dictionary to maintain the stock of products in a shop. 
Example: 
{ 
'Laptop': 15, 
'Mouse': 40, 
'Keyboard': 25, 
'Monitor': 10 
} 
Implement the following: 
• Add a new product.  
• Update the stock of an existing product.  
• Remove a product from inventory.  
{ 
'Rahul': {'Math': 85, 'Science': 90, 'English': 88}, 
• Display products having stock less than 20.  
• Display the total number of items available in the inventory.  
----------------------------------------------------------------------------------------------------------------
--------------------------------------------------Coding---------------------------------------------------
'''

# Initial inventory stock
inventory = {
	'Laptop': 15,
	'Mouse': 40,
	'Keyboard': 25,
	'Monitor': 10
}

print("-------------------------------------------------")
print("Current Inventory:")
for product, stock in inventory.items():
	print(product, ":", stock)

# Add a new product
new_product = input("Enter new product name to add: ")
new_stock = int(input(f"Enter stock for {new_product}: "))
inventory[new_product] = new_stock

# Update the stock of an existing product
update_product = input("Enter product name to update: ")
if update_product in inventory:
	updated_stock = int(input(f"Enter new stock for {update_product}: "))
	inventory[update_product] = updated_stock
else:
	print("Product not found for update.")

# Remove a product from inventory
remove_product = input("Enter product name to remove: ")
if remove_product in inventory:
	del inventory[remove_product]
else:
	print("Product not found for removal.")

print("-------------------------------------------------")
print("Updated Inventory:")
for product, stock in inventory.items():
	print(product, ":", stock)

print("-------------------------------------------------")
print("Products having stock less than 20:")
for product, stock in inventory.items():
	if stock < 20:
		print(product, ":", stock)

total_items = sum(inventory.values())
print("-------------------------------------------------")
print("Total Number of Items Available:", total_items)
print("-------------------------------------------------")
#----------------------------------------------------------------------------------------------------------