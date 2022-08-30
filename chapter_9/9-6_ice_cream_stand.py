class Restaurant:

    def __init__(self,restaurant_name,cousine_type=None):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type    
        self.number_served = 0  

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name} \nCousine type: {self.cousine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served

class IceCreamStand(Restaurant):
    
    def __init__(self,restaurant_name,flavors=["mango","chocolate","vanilla","lemon"]):
        super().__init__(self,restaurant_name)
        self.flavors = flavors

    def display_flavors(self):
        print("Ice cream flavors in this restaurant:")
        for flavor in self.flavors:
            print(flavor)


ice_cream_point = IceCreamStand("Lola Restaurant")

ice_cream_point.display_flavors()