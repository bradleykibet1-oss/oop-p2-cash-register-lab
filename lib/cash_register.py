#!/usr/bin/env python3

class CashRegister:
    """
    A cash register system that manages items, totals, discounts, and transactions.
    
    Attributes:
        discount (int): Percentage discount to apply to total (0-100)
        total (float): Current total of all items in the register
        items (list): List of all items added to the register
        previous_transactions (list): History of all transactions
    """
    
    def __init__(self, discount=0):
        """
        Initialize a cash register with optional discount.
        
        Args:
            discount (int, optional): Percentage discount for this register. Defaults to 0.
                                      Must be between 0-100 inclusive.
        """
        self._discount = None  # Use private attribute for property validation
        self.discount = discount  # Use property setter for validation
        self.total = 0
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        """Get the discount percentage."""
        return self._discount
    
    @discount.setter
    def discount(self, value):
        """
        Set the discount percentage with validation.
        
        Args:
            value (int): Discount percentage (must be integer between 0-100)
            
        Raises:
            Prints error message if discount is not valid
        """
        # Ensure discount is an integer
        if not isinstance(value, int):
            print("Not valid discount")
            self._discount = 0
            return
        
        # Ensure discount is between 0-100 inclusive
        if value < 0 or value > 100:
            print("Not valid discount")
            self._discount = 0
            return
        
        self._discount = value
    
    def add_item(self, item, price, quantity=1):
        """
        Add an item to the cash register.
        
        Args:
            item (str): Name of the item
            price (float): Price of the item
            quantity (int, optional): Quantity of items. Defaults to 1.
        """
        # Add price multiplied by quantity to total
        self.total += price * quantity
        
        # Add item to items list (repeated quantity times)
        for _ in range(quantity):
            self.items.append(item)
        
        # Track transaction in previous_transactions
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)
    
    def apply_discount(self):
        """
        Apply the discount percentage to the current total.
        Prints success message with updated total or error if no discount exists.
        """
        # Check if there's a discount to apply
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        
        # Calculate and apply discount to total
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        
        # Print success message with updated total
        print(f"After the discount, the total comes to ${int(self.total)}.")
    
    def void_last_transaction(self):
        """
        Remove the last transaction from the register.
        Updates total and items list accordingly.
        """
        # Check if there are transactions to void
        if not self.previous_transactions:
            return
        
        # Get and remove the last transaction
        last_transaction = self.previous_transactions.pop()
        
        # Subtract the transaction amount from total
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        
        # Remove the item(s) from the items list
        for _ in range(last_transaction["quantity"]):
            self.items.remove(last_transaction["item"])
