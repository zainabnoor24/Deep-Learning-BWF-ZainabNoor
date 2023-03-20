#3-1
print("\n3-1-----")
names = ["Ali", "Ayesha", "Ahmad","Zoha"]

print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3-2
print("\n3-2-----")
print("How are you {}?".format(names[0]))
print("How are you {}?".format(names[1]))
print("How are you {}?".format(names[2]))
print("How are you {}?".format(names[3]))

#3-3
print("\n3-3-----")
transport = ['car', "bicycle"]

print("I came to university today using {}".format(transport[0]))
print("I like to go to school by  {}".format(transport[1]))


#3-4
print("\n3-4-----")
friends = ["Ali", "Ayesha", "Ahmad","Zoha"]
for friend in friends:
    print("You are invited to the party {}".format(friend))


#3-5
print("\n3-5-----")

friends = ["Ali", "Ayesha", "Ahmad","Zoha"]

for friend in friends:
    print("You are invited to the party {}".format(friend))
       
print("----{} is not coming to the party-----".format(friends[1]))  
friends.pop(1) 

friends.append("JOe")  
for friend in friends:
    print("You are invited to the party {}".format(friend))  
    



#3-6
print("\n3-6-----")    
 
friends = ["Ali", "Ayesha", "Ahmad","Zoha"]

for friend in friends:
    print("You are invited to the party {}".format(friend))
       
print("----{} is not coming to the party-----".format(friends[1]))  
friends.pop(1) 

friends.append("JOe")  
for friend in friends:
    print("You are invited to the party {}".format(friend))  
    

print("We just found a bigger dinner table, so now more space is available. \n")
friends.insert(0, "Noureen")
friends.insert(2, "Marium")
friends.append("Elsa")

for friend in friends:
    print("Welcome to my dinner party {}".format(friend))    




#3-7
print("\n3-7-----")    
   
 
friends = ["Ali", "Ayesha", "Ahmad","Zoha"]

for friend in friends:
    print("You are invited to the party {}".format(friend))
       
print("----{} is not coming to the party-----".format(friends[1]))  
friends.pop(1) 

friends.append("JOe")  
for friend in friends:
    print("You are invited to the party {}".format(friend))  
    

print("We just found a bigger dinner table, so now more space is available. \n")
friends.insert(0, "Noureen")
friends.insert(2, "Marium")
friends.append("Elsa")

for friend in friends:
    print("Welcome to my dinner party {}".format(friend))    



print("I can invite only two people")  

friends.pop(0)  
print("We are sorry we can't invite you ")
friends.pop(1)  
print("We are sorry we can't invite you")
friends.pop(0)  
print("We are sorry we can't invite you")
friends.pop(1) 
print("We are sorry we can't invite you")
friends.pop(0) 
print("We are sorry we can't invite you")

print("{0} & {1}, you guys are still invited".format(friends[0], friends[1]))
del friends[0]  
del friends[0]
print(friends)




#3-8
print("\n3-8-----")    
places = ["lahore", "multan", "islamabad", "pakistan", "turkey"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)



#3-9
print("\n3-9-----")    
friends2 = ["Ali", "Ayesha", "Ahmad","Zoha"]
no_of_invitations = len(friends2)
print("{} people are invited to my dinner party".format(no_of_invitations))
