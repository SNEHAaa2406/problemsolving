# Find:
# 1. Customers who came in both months
# 2. Customers who came only in January
# 3. Customers who came only in February
# 4. All unique customers
# 5. Customers who came in exactly one month
# Don't use loops initially.
# Use set operations.
january_customers = {
    101, 102, 103, 104, 105, 106
}
february_customers = {
    104, 105, 106, 107, 108, 109
}
print("customers who came in both months is :",january_customers & february_customers )
print("Customers who only came in january is :",january_customers - february_customers)
print("Customers who only came in feb is :",february_customers - january_customers)
print("Union i s:",january_customers | february_customers)
print("Who only in one month:",january_customers ^ february_customers)