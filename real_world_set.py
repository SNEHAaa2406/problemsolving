# Find:
# 14. Visitors who purchased.
# 15. Visitors who visited but didn't purchase.
# 16. Visitors who added to cart but didn't purchase.
# 17. Visitors who visited the website but neither purchased nor added to cart.
# 18. Total unique users across all three datasets.

website_visitors = {101, 102, 103, 104, 105, 106}
purchased = {102, 104, 106}
cart_added = {101, 102, 104, 107}
print("Visitors who purchase:",website_visitors - purchased)