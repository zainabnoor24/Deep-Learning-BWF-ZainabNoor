############9-1
print("\n9-1-----")

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print('The name of the Restaurant is {} and it makes {}'.format(self.name, self.cuisine_type))
    
    def open_restaurant(self):
        print('The Restaurant is open')
        

restaurant = Restaurant('ABC', 'Noodles')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()






############9-2
print("\n9-2-----")


class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print('The name of the Restaurant is {} and it makes {}'.format(self.name, self.cuisine_type))
    
    def open_restaurant(self):
        print('The Restaurant is open')
        

restaurant = Restaurant('ABC', 'Noodles')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
print()
restaurant = Restaurant('Macdonalds', 'burger')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
print()
restaurant = Restaurant('ASDD', 'sandwich')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()




############9-3
print("\n9-3-----")


class User:
    
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = id

    def describe_user(self):
        print('{} {} has user id {}'.format(self.first_name, self.last_name, self.id))
        
    def greet_user(self):
        print('Welcome {}'.format(self.first_name))
        
name = User('zainab', 'noor', 1221233)
print(name.first_name)
print(name.last_name)
print(name.id)
print()
name.describe_user()
print()
name.greet_user()

print()
name1 = User('ali', 'tyrt', 6786775)
print(name1.first_name)
print(name1.last_name)
print(name1.id)
print()
name1.describe_user()
print()
name1.greet_user()





############9-4
print("\n9-4-----")

class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print('The name of the Restaurant is {} and it makes {}'.format(self.name, self.cuisine_type))
    
    def open_restaurant(self):
        print('The Restaurant is open')
    
    def customer_numbers(self):
        print('This restaurant has {} customers  '.format(self.number_served))
        
    def set_number_served(self, served):
        self.number_served = served
        
    def increment_number_served(self, customers):
        self. number_served += customers
        

restaurant = Restaurant('Csadas', 'Noodles')

print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.customer_numbers()
restaurant.set_number_served(22)
restaurant.customer_numbers()
restaurant.increment_number_served(7)
restaurant.customer_numbers()






############9-7
print("\n9-7-----")

class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.age} years old, from {self.location}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
        
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print(f"Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
admin = Admin("jnn", "j", 8, "Ny")
admin.describe_user()
admin.show_privileges()



############9-8
print("\n9-8-----")

class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.age} years old, from {self.location}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
        
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print(f"Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
        
        
admin = Admin("znb", "noor", 35, "pak")
admin.describe_user()
admin.privileges.show_privileges()