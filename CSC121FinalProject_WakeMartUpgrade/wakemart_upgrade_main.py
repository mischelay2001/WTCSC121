__author__ = 'Michele Johnson'

# Program Requirements
"""

CSC121 Python Programing Final Project:

Create a Python project for the following problem. Zip the Python project into a zip file.  
Submit the zip file to Blackboard for credit.

In Lab 12 you wrote a program for Wake-Mart customers to check out grocery items.  
Now Wake-Mart wants an upgrade of the system.  First, they want the customer to register before ordering items.  
They only accept payment by credit card or debit card.  
The customer must enter card information during the registration process.  
Second, instead of asking the customer to enter the price of each item and the value of each coupon, 
now they want the customer to enter a 4-digit code for each item and each coupon, 
and the program will look up the price from a price list or the value of the coupon from a coupon list.  
The following lists the requirements of this project.

Define a Customer class.  

INSTRUCTIONS – MAIN MODULE (FINAL-EXAM.PY)

The main module of the project must have the following six functions.
1.	read_price_list
2.	read_coupon_list
3.	scan_prices
4.	scan_coupons
5.	make_payment
6.	main – In the main function:
    a.	Ask the customer to enter her name.  Use it to create a Customer object.  
    b.	Call the input_card_info method of the object to input credit card and debit card information.
    c.	Call the scan_prices function.
    d.	Call the scan_coupons function.
    e.	Use the scan_prices and scan_coupons return values to calculate how much the customer needs to pay.
    f.	Display this amount on the screen.
    g.	Call the make_payment method to process payment. 
        Pass the Customer object and the total amount to pay as two arguments.

"""

# Import Statements
from CSC121FinalProject_WakeMartUpgrade import formatting
from CSC121FinalProject_WakeMartUpgrade.register_customer import RegisterCustomer
from CSC121FinalProject_WakeMartUpgrade.show_list_prices import ProductList
from CSC121FinalProject_WakeMartUpgrade import scan_items
from CSC121FinalProject_WakeMartUpgrade.show_list_coupons import CouponList
from CSC121FinalProject_WakeMartUpgrade import scan_coupons
from CSC121FinalProject_WakeMartUpgrade import make_payment


# Program
def main():

    # Print Program Heading
    heading_title = "WAKE-MART SELF-CHECKOUT II"
    formatting.headings(heading_title)

    # Program Introduction
    print("This program will process a customer's order via the following steps:\n"
          "- Register Customer;\n"
          "- Item Lookup;\n"
          "- Coupon Lookup;\n"
          "- Confirm Order;\n"
          "- Total Order;\n"
          "- Payment\n")

    # Register Customer: name, debit card, and credit card information
    # Initiate Class: RegisterCustomer
    a_customer = RegisterCustomer()

    # Print Customer Registration Heading, register name, and display welcome message
    RegisterCustomer.CustomerName(a_customer)

    # Print Card Registration Heading, register cards, and display confirmation
    RegisterCustomer.RegisterCards(a_customer)
    RegisterCustomer.DisplayRegistration(a_customer)

    # Generate Product List
    # Initiate Class: ProductList
    product_list = ProductList()

    # Processes product list as a dictionary
    generate_list_items = ProductList.GenerateProductList(product_list)

    # Displays product list data
    ProductList.ShowProductList(product_list)

    # Capture and process items ordered, item count, order total
    order, item_count, order_total = scan_items.scan_and_total_items(generate_list_items, product_list)

    # Display customer's total items order and order total
    scan_items.show_order_list(order)
    print("\n\nTotal Items Ordered:\t", item_count)
    print('Order Total:\t\t\t $' + (format(order_total, ',.2f')) + '\n')

    # Generate Coupon List
    # Initiate Class: CouponList
    coupon_list = CouponList()

    # Processes coupon list as a dictionary
    generate_list_coupons = CouponList.GenerateCouponList(coupon_list)

    # Displays coupon list data
    CouponList.ShowCouponList(coupon_list)

    # Capture and process coupons entered, coupon count, coupon total value
    coupon, coupon_count, coupon_total = scan_coupons.scan_and_total_coupons(generate_list_coupons, coupon_list)

    # Display customer's total coupons entered and value
    scan_coupons.show_coupon_list(coupon)
    print("\nTotal Coupons Entered:\t", coupon_count)
    print('Coupon Total:\t\t\t $' + (format(coupon_total, ',.2f')) + '\n')

    # Order Confirmation Summary heading
    heading_order_summary = "ORDER SUMMARY"
    formatting.headings(heading_order_summary)

    # Item Summary
    print("Total Items Ordered:\t", item_count)
    print('Order Total:\t\t\t $' + (format(order_total, ',.2f')) + '\n')

    # Coupon Summary
    print("Total Coupons Entered:\t", coupon_count)
    print('Coupon Total:\t\t\t $' + (format(coupon_total, ',.2f')) + '\n')

    # Grand Total
    # If order total is greater than coupon total
    if order_total <= coupon_total:
        coupon_total = order_total
    grand_total = order_total - coupon_total
    print('TOTAL ORDER..........\t $' + (format(grand_total, ',.2f')) + '\n')

    # Payment Method
    # If grand total is greater than 0
    if grand_total > 0:
        # Get user's payment choice
        payment_card = make_payment.payment_choice()

        # Get debit card pin on file
        debit_pin_filed = RegisterCustomer.GetSecurityPin(a_customer)
        # Get credit card security code on file
        credit_code_filed = RegisterCustomer.GetSecurityCode(a_customer)

        # If Debit Card
        if payment_card == 1:
            make_payment.payment_debit(grand_total, debit_pin_filed)
        # If Credit Card
        if payment_card == 2:
            make_payment.payment_credit(grand_total, credit_code_filed)

    # Thank Customer
    print()
    heading_thanks = "THANK YOU FOR SHOPPING WAKE-MART!!!" \
                     "\nPLEASE COME AGAIN!"
    formatting.headings(heading_thanks)


main()
