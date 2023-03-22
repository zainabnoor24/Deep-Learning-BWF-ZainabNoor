#6-1
print("\n6-1-----")
person = {
    "first_name": "Zainab",
    "last_name": "Noor",
    "age": 22,
    "city": "Islamabad"
    }
for x, y in person.items():
    print(x, y)


#6-2
print("\n6-2-----")
fav_nos = {
    "ali": 4,
    "amna": 56,
    "ahmad": 33,
    "alia": 44,
    "zoha": 22
    }
for x, y in fav_nos.items():
    print(x, y)


#6-5
print("\n6-5-----")

rivers = {
    'nile': "egypt",
    "mississippi": "united states"
}
for x, y in rivers.items():
    print("The {0} runs through {1}".format(x, y))  
for river in rivers.keys():
    print(river)    
print()

for place in rivers.values():
    print(place)   
    
#6-6
print("\n6-6-----")
favorite_languages = {
'zainab': 'python',
'Sana': 'c',
'ali': 'ruby'
}
polled_people = ["ali", "sal", "sarah", "dave", "jen"]

favorite_languages_lower = [x.lower() for x in favorite_languages]

for users in polled_people:
    if users in favorite_languages_lower:
        print("Thanks for taking the poll, {}".format(users))
    else:
        print("Please take the poll {}".format(users))