__author__ = 'Michele Johnson'

""" 3.  scan_prices

Write a scan_prices function for the customer to order items.  
First call the read_price_list function to read the price list from a text file.  
Display all items in the price dictionary.  
Then use a loop for the customer to enter product code of each item he wants.  
Every time a product code is entered, check to see whether the code is in the dictionary.  
If it is not, display “Item not found”.  If the code is in the dictionary, 
display “Item found” and the price of the item.  When the customer has no more product code to enter, 
she types ‘9999’ to exit the loop.  The scan_prices function will calculate, 
display and return the total price of all the items ordered. """

# Import Statements
from CSC121FinalProject_WakeMartUpgrade.show_list_prices import ProductList
from CSC121FinalProject_WakeMartUpgrade import valid_entry
from CSC121FinalProject_WakeMartUpgrade import formatting


def request_num():
    # Function validates the number of items user request to be purchased

    # Initialize Variables
    request_entry = 0
    confirm_entry = 0

    # # Loop: Item Requests
    is_request_valid = False
    while is_request_valid is False:

        # Number of requests: User enters number of items to be purchased
        entry = "\nEnter the number of items to be purchased"
        # Current number of requests
        request_entry = valid_entry.integer_entry(entry)

        # Request count less than 1
        if request_entry <= 0:
            entry_test1 = False
            print("\tThe number of items must be greater than 0.")

        # Greater than 10 without confirmation
        elif request_entry > 10:
            entry = "\tPlease confirm the number of items to be purchased"
            confirm_entry = valid_entry.integer_entry(entry)

            # If quantities not equal, display message and try again
            if request_entry != confirm_entry:
                print("\tThe number of items to be purchased was not confirmed.")
            else:
                is_request_valid = True

        else:
            is_request_valid = True

    return request_entry


def scan_and_total_items(generated, products):
    """ This function collects, counts, and total price of  items ordered by user.
        The customer enters the prices one by one with a loop until they desire to quit.
        Function also checks each item against the product list to verify the item is listed.
        The function returns items ordered as a dictionary, item count, and total price of all items ordered. """

    # Continue to add items to order until user stops
    order = {}
    total = 0
    item_count = 0
    request_count = 0

    # Order Items
    # Loop until user confirms to end ordering items
    is_order_done = False
    while is_order_done is False:

        # Loop: Item Requests
        is_request_valid = False
        while is_request_valid is False:

            # Get valid number of requests
            request_entry = request_num()
            # Request tally of all requests
            request_count = request_count + request_entry

            # Loop processes item; repeats to equal number of requests
            for i in range(request_entry):

                # Loop: Look up item number
                is_item_valid = False
                while is_item_valid is False:

                    # User enters item number
                    request_text = "\n\t\t\t\t\tEnter item code:"
                    item = valid_entry.clean_string_digits(request_text, 4)

                    # Look for item as a key
                    # If item is valid
                    if item in generated:
                        # Get item price and name; display item
                        item_price, item_name = ProductList.ShowProduct(products, item)
                        print("\t\t\t\t\t\t Item Found:\t" + item_name + "\t$" + item_price)

                        # Running tally of items ordered
                        item_count += 1

                        # add item to order list
                        item_price = float(item_price)
                        order[item_count] = item, item_price, item_name

                        # Running tally of order total
                        total = total + float(item_price)

                        # Loop ends
                        is_item_valid = True

                    # If item number is not valid, error
                    else:
                        print("\nItem Not Found")

            # Loop ends: all requests processed
            if item_count == request_count:
                is_request_valid = True

        # Loop ends; input from user to end ordering items
        stop_order = input("\nEnter -1 to stop order entry:\t")
        if stop_order == '-1':
            is_order_done = True

    return order, item_count, total


def show_order_list(a_order):
    # Function displays the list of items ordered by customer
    # Customer order heading
    print()
    heading_customer_order = "YOUR ORDERED ITEMS"
    formatting.headings(heading_customer_order)
    print("Item Number\t\t\tItem Code\t\t\tPrice\t\t\tItem Name")
    for key in a_order:
        item_data = a_order[key]
        item_code = item_data[0]
        item_price = format(float(item_data[1]), ',.2f')
        item_name = item_data[2]
        print(" ", key, "\t\t\t\t", item_code, "\t\t\t\t$" + str(item_price), "\t\t\t", item_name)
