####### CONDITIONALS #########

#5-1
print("\n5-1-----")

car = "subaru"
morning = "good"
print(car=="subaru")
print(car=="audi")
print(morning=="bad")
print(morning=="good")
print((car=="subaru") and (morning=="good"))
print((car=="subaru") and (morning=="bad"))
print((car=="subaru") or (morning=="good"))
print((car=="audi") or (morning=="good"))

#5-2
print("\n5-2-----")

string1="hello"
string2="helo"
string3="HELLO"
lst = ["Ali", "Ayesha", "Ahmad","Zoha"]

print(string1==string2)
print(string1==string3.lower())
print(2>5)
print(5<2)
print(3==3)
for i in lst:
    if(i == "Ali"):
        print("Element Exists")
    else:
        print("Element not exists")



####### USER INPUTS #########
#7-1
print("\n7-1-----")

user_input = input("What type of rental car would you like? ")
print("Let's see if we can find you a {}".format(user_input))


#7-2
print("\n7-2-----")
group = input("How many people are in your dinner group? ")
group = int(group)
if group > 8:
    print("You'll have to wait for a table")
else:
    print("You're table is ready")




#7-3
print("\n7-3-----")
number = input("Enter a number: ")
number = int(number)
if number % 10 == 0:
    print("{} is multiple of 10".format(number))
else:
    print("{} is not multiple of 10".format(number))
    