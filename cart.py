"""
This module represents the Cart.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

class Cart():
    """
    Class that represents a cart.
    """
    def __init__(self, _id):
        """
        Constructor.

        :type id: int
        :param id: id of the cart
        """
        self._id = _id
        self.products = list()

    def add(self, product):
        """
        Adds product to cart.

        :type product: Product
        :param product: product to be added
        """
        self.products.append(product)

    def delete(self, product):
        """
        Deletes product from cart.

        :type product: Product
        :param product: product to be deleted
        """
        self.products.remove(product)
