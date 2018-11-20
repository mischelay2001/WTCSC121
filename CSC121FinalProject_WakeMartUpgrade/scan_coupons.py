__author__ = 'Michele Johnson'

""" 4.	scan_coupons

Write a scan_coupons function for the customer to enter coupons.  
This function is very similar to the scan_prices function.  
It calls the read_coupon_list function to read the coupon list from a text file.  
Display all items in the coupon dictionary.  
Then use a loop for the customer to enter 4-digit code of each coupon she has.  
Every time a 4-digit code is entered, check to see whether the code is in the dictionary.  
If it is not, display “Coupon not found.”  If the code is in the dictionary, 
display “Coupon found” and the value of the coupon.  When the customer has no more coupons to enter, 
she types ‘9999’ to exit the loop.  
The scan_coupons function will calculate, display and return the total value of all the coupons entered.  """

# Import Statements
from CSC121FinalProject_WakeMartUpgrade.show_list_coupons import CouponList
from CSC121FinalProject_WakeMartUpgrade import valid_entry
from CSC121FinalProject_WakeMartUpgrade import formatting


def scan_and_total_coupons(generated, coupons):
    """ This function gets the value of each coupon entered by the customer.
        The customer enters the coupon values one by one with a loop. When there is no more coupons to enter,
        -1 is entered to exit the loop.  The function calculates and returns the total value of all coupons. """

    # Continue to add coupons to order until user stops
    order = {}
    total = 0
    count = 0
    
    # Enter Coupons?
    done_enter_coupons = False
    while done_enter_coupons is False:
        
        # get valid number of coupons, keep running total of coupons
        request_num_of_coupons = "Enter the number of coupons to be entered"
        num_of_coupons = valid_entry.integer_entry(request_num_of_coupons)
        if num_of_coupons > 0:

            # loop to capture coupon value for each coupon
            for i in range(num_of_coupons):        
        
                # repeat until done is true
                # Get coupon to be entered
                request_text = "\n\t\t\t\t\t\tEnter coupon code:"
                coupon = valid_entry.clean_string_digits(request_text, 4)
        
                # Check coupon code
                # look for coupon as a key
                if coupon in generated:
                    coupon_price, coupon_name = CouponList.ShowCoupon(coupons, coupon)
                    print("\t\t\t\t\t\t\t Coupon Found:\t" + coupon_name + "\t$" + coupon_price)
        
                    # Running tally of coupons entered
                    count += 1
        
                    # If coupon number is valid, continue
                    # add coupon to coupon list
                    coupon_price = float(coupon_price)
                    order[count] = coupon, coupon_price, coupon_name
        
                    # Running tally of coupon total
                    total = total + float(coupon_price)
        
                # If coupon number is not valid, error
                else:
                    print("\nCoupon Not Found")

            # get input from user to end while loop or continue
            is_done = input("\nEnter -1 to stop coupon entry:\t")
            if is_done == '-1':
                done_enter_coupons = True
                
        else:
            print("The number of coupons must be greater than 0.\n")

    return order, count, total


def show_coupon_list(a_order):
    # Function displays the list of items ordered by customer
    # Customer order heading
    print()
    heading_coupons_ordered = "YOUR REQUESTED COUPONS"
    formatting.headings(heading_coupons_ordered)
    print("Item Number\t\t\tCoupon Code\t\t\tValue\t\tManufacturer")
    for key in a_order:
        coupon_data = a_order[key]
        coupon_code = coupon_data[0]
        coupon_price = format(float(coupon_data[1]), ',.2f')
        coupon_name = coupon_data[2]
        print(" ", key, "\t\t\t\t", coupon_code, "\t\t\t\t$" + str(coupon_price), "\t\t", coupon_name)
