class Customer:
    # Class attribute to track all Customer instances
    _all_customers = []

    def __init__(self, name):
       # Initizes a new Customer with a name and an empty list of orders.
    
        self.name = name
         # Initialize the list of orders
        self._orders = [] 

         # Add the customer to the list of all customers
        Customer._all_customers.append(self)   
    def name(self):
        
        #Property that returns the customer's name.
        
        return self._name

    @name.setter
    def name(self, value):
        
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value  # Set the name if validation passes
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        
        #Returns a list of all orders associated with this customer.
        return self._orders

    def coffees(self):

        #Returns a unique list of all Coffee instances this customer has ordered.
        return list(set(order.coffee for order in self._orders)) 

    def create_order(self, coffee, price):
    
       #Creates a new order for the given coffee and price.
    
        
        if isinstance(coffee, Coffee):

             # Creating a new order
            order = Order(self, coffee, price)  

             # Add the order to the customer's order list
            self._orders.append(order)  

             # Add the order to the coffee's order list
            coffee._orders.append(order)

             # Return the created order
            return order  
        else:
             # Raises ValueError if the coffee is not a valid Coffee object.
            raise ValueError("Invalid coffee object.")

    
    def most_aficionado(cls, coffee):

        #Returns the customer who has spent the most money on the given coffee.

        if isinstance(coffee, Coffee):
             # Dictionary to store customer spendings
            customer_spendings = {} 
            # Looping  through the orders of the coffee
            for order in coffee.orders():
                if order.customer in customer_spendings:
                    # Add the price of the order to the customer's total spend
                    customer_spendings[order.customer] += order.price
                else:
                    # Add the price of the order to the customer's total spend
                    customer_spendings[order.customer] = order.price
            if not customer_spendings:
                return None  # No customers if the spendings dictionary is empty
            # Return the customer who spent the most (max by value)
            return max(customer_spendings, key=customer_spendings.get)
        else:
            raise ValueError("Invalid coffee object.")


class Coffee:
    def __init__(self, name):
        """
        Initializes a new Coffee with a name and an empty list of orders.
        Validates the name to ensure it is a string with at least 3 characters.
        """
        self.name = name  # Calls the name setter to validate the name
        self._orders = []  # List to store all orders for this coffee

    
    def name(self):
    
        #Property that returns the coffee's name.
        return self._name

    def name(self, value):
        
        #Setter for the coffee's name.
        if not hasattr(self, '_name'):  # Check if name has been set before
            if isinstance(value, str) and len(value) >= 3:
                self._name = value  # Set the name if validation passes
            else:
                raise ValueError("Coffee name must be a string with at least 3 characters.")
        else:
            raise AttributeError("Cannot change the name of the coffee once set.")

    def orders(self):
    
        #Returns a list of all orders associated with this coffee.
        return self._orders

    def customers(self):

        #Returns a unique list of all customers who have ordered this coffee.
        return list(set(order.customer for order in self._orders))

    def num_orders(self):
       
       #Returns the number of orders associated with this coffee.
        return len(self._orders)

    def average_price(self):
       
       #Returns the average price of all orders associated with this coffee.
        if not self._orders:  # Check if there are no orders
            return 0
        # Calculate the total price and divide by the number of orders
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)


class Order:
    def __init__(self, customer, coffee, price):
        
        # Initializes a new Order with a customer, coffee, and price.
        self._customer = customer  # Customer who placed the order
        self._coffee = coffee  # Coffee being ordered
        self.price = price  # Calls the price setter to validate the price

    
    def customer(self):
       
       #Property that returns the customer who placed the order.
        return self._customer

    
    def coffee(self):
      
      #Property that returns the coffee being ordered.
        return self._coffee


    def price(self):
         
         #Property that returns the order price.
        return self._price

    
    def price(self, value):
      
      #Setter for the order price.
        if not hasattr(self, '_price'):  # Check if price has been set before
            if isinstance(value, float) and 1.0 <= value <= 10.0:
                self._price = value  # Set the price if validation passes
            else:
                raise ValueError("Price must be a float between 1.0 and 10.0.")
        else:
            raise AttributeError("Cannot change the price once set.")
