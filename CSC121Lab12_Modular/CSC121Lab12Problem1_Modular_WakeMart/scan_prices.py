from CSC121Lab12_Modular.CSC121Lab12Problem1_Modular_WakeMart import valid_entry


def scan_and_total_prices():
    """ This function gets the price of each item purchased.
        The customer enters the prices one by one with a loop. When there is no more prices to enter,
        -1 is entered to exit the loop.  The function calculates and returns the total price of all items. """

    # initialize variables
    done = False
    item_count = 0
    total_price = 0.0

    # loop until user stops by entering -1
    while done is False:
        # get valid number of items, keep running total of items
        request_num_of_items = "Enter the number of items to be purchased"
        num_of_items = valid_entry.integer_entry(request_num_of_items)
        if num_of_items > 0:
            item_count += num_of_items
            # loop to capture item price for each item
            for i in range(num_of_items):
                # get valid price
                request_a_price = "\tEnter the item price"
                a_price = valid_entry.float_entry(request_a_price)
                total_price += a_price
            # get input from user to end while loop or continue
            is_done = input("Enter -1 if there are no more items prices to capture:\t")
            if is_done == '-1':
                done = True
        else:
            print("The number of items must be greater than 0.\n")

    return item_count, total_price
