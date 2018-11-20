from CSC121Lab12_Modular.CSC121Lab12Problem1_Modular_WakeMart import valid_entry


def coupon_values():
    """ This function gets the value of each coupon entered by the customer.
        The customer enters the coupon values one by one with a loop. When there is no more coupons to enter,
        -1 is entered to exit the loop.  The function calculates and returns the total value of all coupons. """

    # initialize variables
    done = False
    coupon_count = 0
    total_price = 0.0

    # loop until user stops by entering -1
    while done is False:
        # get valid number of coupons, keep running total of coupons
        request_num_of_coupons = "Enter the number of coupons to be entered"
        num_of_coupons = valid_entry.integer_entry(request_num_of_coupons)
        if num_of_coupons >= 0:
            coupon_count += num_of_coupons
            # loop to capture coupon price for each coupon
            for i in range(num_of_coupons):
                # get valid price
                request_a_price = "\tEnter the value of the coupon"
                a_price = valid_entry.float_entry(request_a_price)
                total_price += a_price
            # get input from user to end while loop or continue
            is_done = input("Enter -1 if there are no more coupon values to capture:\t")
            if is_done == '-1':
                done = True
        else:
            print("The number of coupons must be greater than or equal to 0.\n")

    return coupon_count, total_price
