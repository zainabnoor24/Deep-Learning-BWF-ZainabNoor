
############8-1
print("\n8-1-----")

def display_message():
    print("I am learning functions in this chapter")
display_message()



############8-2
print("\n8-2-----")
def favorite_book(title):
    print("My favorite book to read is {}".format(title))
    
favorite_book("Kite Runner")


############8-3
print("\n8-3-----")
def make_shirt(size, text_message):
    print(" I want a shirt of size {} with '{}' message".format(size, text_message))
    
make_shirt(14,'hello world')


############8-4
print("\n8-4-----")
def make_shirt(text_message, size = 'Large'):
    print(" I want a shirt of size  {0} with '{1}' message".format(size, text_message))
    
make_shirt("'I love Python'")
make_shirt(size = 'medium', text_message = 'I love Python')
make_shirt(size='small', text_message='I love Python')


############8-5
print("\n8-5-----")
def describe_city(city, country='pakistan'):
    print("{} is located in {}".format(city.title(), country))
    
describe_city('lahore')
describe_city('isb')
describe_city('sialkot')



############8-6
print("\n8-6-----")

def city_country(city, country):

    city_location = "{}, {}".format(city.title(), country.title())
    print(city_location)
    return city_location
city_country('lahore', 'pakistan')
city_country('KL', 'malaysia')
city_country('sydney', 'australia')


############8-7
print("\n8-7-----")


def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist name': artist_name, 'album_title': album_title}
    
    if number_of_songs:
        album['number of songs'] = number_of_songs
    return album


musician = make_album('as', 'assd')
print(musician)
musician = make_album('Ksdt', 'sdf', number_of_songs=3)
print(musician)



############8-12
print("\n8-12-----")
def making_sandwich(*choices):
    print("\nThe following will be included with the sandwich: ")
    for choice in choices:
        print(choice)


making_sandwich('chicken', 'onion', 'tomato')
making_sandwich('burger', 'ketchup', 'mayo')
making_sandwich( 'lettuce', 'mayo', 'tomato')


  

############8-14
print("\n8-14-----")
def make_car(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info


cars = make_car('suburu', 'outback', color = 'blue', tow_package = True)
print(cars)