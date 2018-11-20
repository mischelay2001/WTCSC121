__author__ = 'Michele Johnson'

""" 2.	read_coupon_list

The coupon list is stored in the text file “coupon_list.txt”.  
Each line in this file contains a 4-digit code and monetary value of a coupon.  
Write a read_coupon_list function to read the coupon list into the program.  
Store the data in a dictionary with the 4-digit codes as keys and monetary values as values.  
Return the dictionary.  """

# Import Statements
from CSC121FinalProject_WakeMartUpgrade import formatting

class CouponList:

    """ Class reads coupon list file, displays full list and specific item """

    def __init__(self):

        """ constructor """

        # Create value list dictionary
        self.__coupons = {}
        self.__item_code = ""

        # Create item data list
        self.__item_data = []
        self.__item_value = 0.00
        self.__item_name = ""

    def GenerateCouponList(self):

        """ Read data in for coupons and returns information as dictionary """

        input_file = open('list_coupon.txt', 'r')
        for line in input_file:
            line = line.split(",")
            # key for dictionary
            self.__item_code = line[0]
            # list data for value and name
            self.__item_value = float(line[1])
            self.__item_name = line[2].strip()
            # associate list data to appropriate key
            self.__coupons[self.__item_code] = self.__item_value, self.__item_name

        return self.__coupons

    def ShowCouponList(self):

        """ Display full coupon list """

        # Print coupon list heading
        heading_coupon_list = "WAKE-MART COUPON LIST"
        formatting.headings(heading_coupon_list)

        # Display full price list
        print("Coupon Code\t\t\tValue\t\t\tManufacturer")
        for key in self.__coupons:
            self.__item_data = self.__coupons[key]
            self.__item_value = format(self.__item_data[0], ',.2f')
            self.__item_name = self.__item_data[1]
            print(" ", key, "\t\t\t\t$" + str(self.__item_value), "\t\t\t", self.__item_name)
        print()

    def ShowCoupon(self, key):

        """ Returns a specific coupon from list; returns coupon value and name"""

        self.__item_data = self.__coupons[key]
        self.__item_value = format(self.__item_data[0], ',.2f')
        self.__item_name = self.__item_data[1]
        # print(" ", key, "\t\t\t\t$" + str(self.__item_value), "\t\t\t", self.__item_name)

        return self.__item_value, self.__item_name
