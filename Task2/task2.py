#2-1. Simple Message: Store a message in a variable, and then print that message.'''
msg="this is variable"
print("2-1-----")
print(msg)

#2-2. Simple Messages: Store a message in a variable, and print that message.Then change the value of your variable to a new message, and print the new message'''
msg2="this is variable"
print("\n2-2-----")
print(msg2)
msg2="Hello Python world!"
print(msg2)



#2-3. Personal Message: Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”'''
name="Eric"
print("\n2-3-----")
print("Hello "+name+", would you like to learn some Python today?")


#2-4. Name Cases: Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase'''
print("\n2-4-----")
name2="Zainab"
print(name2.upper())
print(name2.lower())
print(name2.title())


#2-5
print("\n2-5-----")
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')


#2-6
print("\n2-6-----")
famous_person = "Albert Einstein"
message = "'A person who never made a mistake never tried anything new.'"
print("{0} once said, {1}".format(famous_person, message))

#2-7
print("\n2-7-----")
name = " \tZainab Noor\n "
print(name.lstrip())
print(name.rstrip())
print(name.strip())


#2-8
print("\n2-8-----")
print(5+3)
print(11-3)
print(4*2)
print(16 // 2)

#2-9
print("\n2-9-----")
favNo = 21
print("My favorite_number is {}".format(favNo))
  