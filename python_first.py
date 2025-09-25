# print 
# msg = "Hello world"
# print (msg)
# firs_name = "Mousab"
# lasr_name = "aidoud"
# print (firs_name + ' ' + lasr_name)

##################### List 

# bike = ['trek' , 'readline' , 'gieant']
# # print(bike[0]) # first
# # print(bike[-1]) # last 
# finished = ['sam', 'bib', 'jaz', 'roz']
# fist_two = finished[:2]
# print (fist_two)
# copy_of_bike = bike [:]
# print (copy_of_bike)

##################### List : some as liste but item can't be modified 

# demension = (1991, 2025)

# # demension_2 = demension[:1]
# # print (demension_2)

# for dem in demension: 
#     dem = dem +1
#     print (dem)
##################### Loop

# for bik in bike:
#     print (bik)

# bikes = []
# bikes.append('decathlon')
# for bik in bike:
#     bikes.append(bik)
# print(bikes)


# ranges = []
# for x in range (0,10):
#     ranges.append(1*x)
# print (ranges)
# square = [x**2 for x in range(1,11)]
# print (square)
##################### While Loop 

# current_value = 1 
# while current_value <= 5:
#     print (current_value)
#     current_value +=1

############################### Condition : 

# ages = [10 , 25, 15, 33, 5 , 78]

# for age in ages: 
#     if age > 18: 
#        print ("Hello")
#     elif age < 10:
#         print ("Casse toi")
#     else:
#         print ("Forbiden")

############################## Dictionnaire : key value paire 

# aien = {'color' : 'red' , 'age' : 20}
# aien ['name'] = 'basta'
# print (aien)

# fav_numbers = {'name' : 'bola' , 'last_name' : 'hola'}
# for name, last_name in fav_numbers.items():
#     print (name + ' ' + last_name)

# for number in fav_numbers.values():
#     print ('Hello ' + str (number))

############################## Input 

# age = input ('Hello you , could i-entre you age please : ')
# age = int(age)
# print (age)

############################## Functin 

# def greet_user ():
#     """Display hello message"""
#     print("Hello")

# greet_user ()
###### Functin with argyment 

# Argument
def greet_user (username):
    """Display hello message"""
    print("Hello " + username)
# Parametter 
greet_user ('Mousab')

###### Functin with default value  
def greet_user (username='Ouali'):
    """Display hello message"""
    print("Hello " + username)
# Parametter 
greet_user ()
greet_user ('Mousab')
###### Functin with eturning valueq 
def caluculat (x , y):
    """"Add function"""
    return x+y
print (caluculat (2, 4))