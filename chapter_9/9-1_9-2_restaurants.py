class Restaurant:

    def __init__(self,restaurant_name,cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type        

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name} \nCousine type: {self.cousine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is now open!")


restaurant_1 = Restaurant("FatPig","Fast-Food")
restaurant_2 = Restaurant("Tampo Ten","Thai")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
