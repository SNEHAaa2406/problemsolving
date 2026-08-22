# Problem 3: Search a Product
# A shopping app stores product IDs:
products = [101, 205, 302, 405, 501]
# Ask the user for a product ID.
# Print:
# Product Found
# or
# Product Not Found
id=int(input("Enter product id :"))
if id in products:
    print("Product found")
else:
    print("Product not found")