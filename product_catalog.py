from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
# for product in products:
#     print(product)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
response = ""
customer_preferences = []
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)
    response = input("Do you want to add another preference? (Y/N): ").upper()

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)

# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({'name': product['name'], 'tags':set(product['tags'])})

# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    match_count = len(product_tags.intersection(customer_tags))

    return match_count

# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    for product in products:
        product['matches'] = count_matches(product['tags'], customer_tags)
    
    return products



# TODO: Step 7 - Call your function and print the results
matching_products = []
for product in recommend_products(converted_products, customer_preferences):
    if product['matches'] > 0:
        matching_products.append(product)

matching_products = sorted(matching_products, key=lambda x: x['matches'], reverse=True)

print("Recommended Products:")
for product in matching_products:
    print(f'- {product['name']} ({product['matches']} match(es))')


# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
# 2. How might this code change if you had 1000+ products?
"""

"""