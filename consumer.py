"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
import time


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.kwargs = kwargs
        self.cart_id = marketplace.new_cart()

    def run(self):
        with self.marketplace.lock:
            self.marketplace.no_consumers += 1

        for orders in self.carts:
            for cart_command in orders:
                for index in range(cart_command["quantity"]):
                    if cart_command["type"] == "add":
                        is_added = False
                        while not is_added:
                            is_added = self.marketplace.add_to_cart(self.cart_id,
                                                            cart_command["product"])
                            if not is_added:
                                time.sleep(self.retry_wait_time)

                    if cart_command["type"] == "remove":
                        self.marketplace.remove_from_cart(self.cart_id, cart_command["product"])
        self.marketplace.place_order(self.cart_id, self.kwargs["name"])

        with self.marketplace.lock:
            self.marketplace.no_consumers -= 1

        if self.marketplace.no_consumers == 0:
            self.marketplace.is_running = False
