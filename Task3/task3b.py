

#4-1
print("\n4-1-----") 
pizzas = ["tikka", "beef peppwrroni", "fajita"]


for pizza in pizzas:
    print("I like {} pizza ".format(pizza))
    
print("I really like pizza")


#4-2
print("\n4-2-----")
animals = ["dog", "cat", "tiger"]
for animal in animals:
    print("{} has four legs".format(animal))
print("All these have tails") 





#4-3
print("\n4-3-----")
for i in range(1, 21):
    print(i)
    
#4-4
print("\n4-4-----")

#for i in range(1, 1000001):
    #print(i)

#4-5
print("\n4-5-----")
lst = list(range(1, 1000000))
print(min(lst))
print(max(lst))
print(sum(lst))
    
#4-6
print("\n4-6-----")
for i in range(1, 20, 2):
    print(i)

#4-7
print("\n4-7-----")
for i in range(3, 33, 3):
    print(i)
    
#4-8
print("\n4-8-----")
for i in range(1, 11):
    print("{} cubed is {}".format(i, i ** 3))
    

#4-9
print("\n4-9-----")
list2=[]
for i in range(1, 11):
    list2.append(i ** 3)
    
print(list2)


#4-10
print("\n4-10-----")
places = ["lahore", "multan", "islamabad", "pakistan", "turkey"]
print(places[0:4])
print(places[2])
print(places[2:])

#4-11
print("\n4-11-----")
pizzas = ["tikka", "beef peppwrroni", "fajita"]
friend_pizzas = ["tikka", "beef peppwrroni", "fajita"]

pizzas.append("cheese")
friend_pizzas.append("bbq")

for pizza in pizzas:
    print(pizza)
    
print()
for friend_pizza in friend_pizzas:
    print(friend_pizza)



#4-13
print("\n4-13-----")
buffet_restaurants = ("beef", "pasta", "ice crean", "macroni", "desert")

for buffet_restaurant in buffet_restaurants:
    print(buffet_restaurant)

buffet_restaurants = ("chinese rice", "pasta", "burger", "fish", "desert")  
for buffet_restaurant in buffet_restaurants:
    print(buffet_restaurant)