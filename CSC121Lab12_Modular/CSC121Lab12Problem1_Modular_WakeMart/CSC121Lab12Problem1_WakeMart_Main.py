__author__ = 'Michele Johnson'

# Program requirements:

# This problem is about modular design.
# We are writing a program to simulate a self-checkout system of a store named Wake-Mart.
#
# This program has three tasks at the top level: input prices of items, input coupons and process payment.
# Processing of payment is further divided into two subtasks.
# The customer can choose either to pay by cash or by debit card.

# import modules
from CSC121Lab12_Modular.CSC121Lab12Problem1_Modular_WakeMart import scan_coupons
from CSC121Lab12_Modular.CSC121Lab12Problem1_Modular_WakeMart import scan_prices
from CSC121Lab12_Modular.CSC121Lab12Problem1_Modular_WakeMart import make_payment


def main():
    """ This function calls the scanPrices function to input item prices,
        calls the scanCoupons function to input coupon values.
        Calculates customer’s balance and pass it to the makePayment function. """

    # Introduce program
    print("WAKE-MART SELF-CHECKOUT\n")
    print("This program will\n"
          "\t- obtain the number of items and the price for each;\n"
          "\t- calculate the total price for all items;\n"
          "\t- obtain the number of coupons;\n"
          "\t- calculate the total value of coupons to subtract from the total price;\n"
          "\t- process either cash or debit payment\n")

    # Obtain item count, price for each, calculate and display the total price
    items_count, items_total = scan_prices.scan_and_total_prices()
    print("Total items:\t", items_count)
    print('Total price:\t $' + (format(items_total, ',.2f')), "\n")

    # Obtain coupon count, value of each, calculate and display the total value of the coupons
    coupon_count, coupon_total = scan_coupons.coupon_values()
    print("Total coupons:\t", coupon_count)
    print('Total coupon value:\t $' + (format(coupon_total, ',.2f')), "\n")

    # Process payment or determine if a refund is owed
    # Payments
    if items_total >= coupon_total:
        # Calculate final bill
        bill_total = items_total - coupon_total
        print("Total cost:\t $" + (format(bill_total, ',.2f')))

        # Determine customer's payment preference
        payment_balance, payment_choice = make_payment.payment_type(bill_total)
        print("Selected payment type:\t", payment_choice)

        # Process cash payments
        if payment_choice == "Cash":
            payment_cash, payment_difference = make_payment.payment_cash(payment_balance)
            print('\nTotal cash payment:\t $' + (format(payment_cash, ',.2f')))
            print('Cash back:\t $' + (format(payment_difference, ',.2f')))

        # Process debit card payments
        elif payment_choice == "Debit":
            payment_debit, payment_back = make_payment.payment_debit(payment_balance)
            print('\nTotal debit payment:\t $' + (format(payment_debit, ',.2f')))
            print('Cash back:\t $' + (format(payment_back, ',.2f')))
    # Refunds
    else:
        refund_amount = coupon_total - items_total
        print('\nRefund amount:\t $' + (format(refund_amount, ',.2f')), "\n")

    # Thank you
    print("\nThank you for shopping at Wake-Mart")


main()
