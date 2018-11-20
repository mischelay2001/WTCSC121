__author__ = 'Michele Johnson'

""" 1.  read_price_list

The price list is stored in the text file “price_list.txt”.  
Each line in this file contains a 4-digit product code and unit price of an item.  
Write a read_price_list function to read the price list into the program.  
Store the data in a dictionary with product codes as keys and prices as values. Return the dictionary.   """

# Import Statements
from CSC121FinalProject_WakeMartUpgrade import formatting


class ProductList:

    """ Class reads product list file, displays full list and specific item """

    def __init__(self):

        """ Creates instance variables """

        # Create price list dictionary
        self.__products = {}
        self.__item_code = ""

        # Create item data list
        self.__item_data = []
        self.__item_price = 0.00
        self.__item_name = ""

    def GenerateProductList(self):

        """ Read data in for products and returns information as dictionary """

        input_file = open('list_price.txt', 'r')
        for line in input_file:
            line = line.split(",")
            # key for dictionary
            self.__item_code = line[0]
            # list data for price and name
            self.__item_price = float(line[1])
            self.__item_name = line[2].strip()
            # associate list data to appropriate key
            self.__products[self.__item_code] = self.__item_price, self.__item_name

        return self.__products

    def ShowProductList(self):

        """ Display full product list """

        # Print price list heading
        heading_price_list = "WAKE-MART ITEM PRICE LIST"
        formatting.headings(heading_price_list)

        # Display full price list
        print("Item Code\t\t\tPrice\t\t\t\tItem Name")
        for key in self.__products:
            self.__item_data = self.__products[key]
            self.__item_price = format(self.__item_data[0], ',.2f')
            self.__item_name = self.__item_data[1]
            print(" ", key, "\t\t\t\t$" + str(self.__item_price), "\t\t\t", self.__item_name)
        print()

    def ShowProduct(self, key):

        """ Returns a specific product from list; returns item price and name"""

        self.__item_data = self.__products[key]
        self.__item_price = format(self.__item_data[0], ',.2f')
        self.__item_name = self.__item_data[1]
        # print(" ", key, "\t\t\t\t$" + str(self.__item_price), "\t\t\t", self.__item_name)

        return self.__item_price, self.__item_name
