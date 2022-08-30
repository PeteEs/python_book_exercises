class Restaurant:

    def __init__(self,restaurant_name,cousine_type):
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

restaurant_1 = Restaurant("FatPig","Fast-Food")
print(restaurant_1.number_served)

restaurant_1.set_number_served(10)
print(restaurant_1.number_served)

restaurant_1.increment_number_served(5)
print(restaurant_1.number_served)
