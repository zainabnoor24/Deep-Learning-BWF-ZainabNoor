
################6-7
print("\n6-7-----")

people= []
person1 = {
    "first_name": "zainab",
    "last_name": "noor",
    "age": 22,
    "city": "wah"
    }
person2 = {
    "first_name": "ali",
    "last_name": "shaan",
    "age": 45,
    "city": "new york"
    }    
person3 = {
    "first_name": "amna",
    "last_name": "ahmad",
    "age": 56,
    "city": "lahore"
    } 
people.append(person1) 
people.append(person2)
people.append(person3)

for person in people:
    firstName = person["first_name"]
    lastName = person["last_name"]
    age = person["age"]
    city = person["city"]
    
    print("{0} {1} is from {2} and he's {3} years old".format(firstName, lastName, city, age))   
    
    



############6-8
print("\n6-8-----")

pets = []

dog_1 = {
    "type_of_dog": "German Shepard",
    "owner": "ab"
 }
dog_2 = {
    "type_of_dog": "Golden Retriever",
    "owner": "aa"
}
dog_3 = {
    "type_of_dog": "German Shepard",
    "owner": "js"
}

pets.append(dog_1)
pets.append(dog_2)
pets.append(dog_3)

for pet in pets:
    typeOfDog = pet["type_of_dog"]
    owner = pet["owner"]
     
    print("{0} is my pet and it's owner is {1}".format(typeOfDog , owner ))
    



############6-9
print("\n6-9-----")
favorite_places = {
    "jf": "lahore",
    "ss": "london",
    "bs": "NY"
    }

for x, y in favorite_places.items():
    print("{}'s favorite place is {}".format(x, y))



############6-10
print("\n6-10-----")
favorite_numbers = {
     "noor": [2, 8], 
    "zainab":[12, 18],
    "joe": [ 24, 26, 28],
    "ali": [ 34, 36, 38]
    }
for x, y in favorite_numbers.items():
    print("{} favorite numbers are: ".format(x))  
    
    for z in y:
        print(z) 




############6-11
print("\n6-11-----")
cities = {
    "london": {
        "country": "UK",
        "population": 545455,
        "fact": "abc"
    },
    "wah": {
        "country": "pakistan",
        "population": 6723423,
        "fact": "dfd"
    },
    "new york": {
        "country": "united states",
        "population": 23223,
        "fact": "dfgdfd"
    }
}

for city, information in cities.items():
    print("{0} is located in {1} and has a population of about {2}. One interesting fact about {0} is: {4}\n".format(city , information["country"], information["population"], city , information["fact"]))
    
    