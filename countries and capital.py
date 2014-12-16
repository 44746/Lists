import random
countries = ['England','Germany','Spain','China','Russia','Ireland','Scotland','France','Belgium','Wales']
capitals = ['London','Berlin','Madrid','Beijing','Moscow','Dublin','Edinburgh','Paris','Brussels','Cardiff']
user_score= 0
counter = 10
print("REMEMBER CAPITALS")
for count in range(10):
    import random
    counter = counter-1
    random = random.randint(0,counter)
    user_answer = input("What is the capital of {0}? ".format(countries[random]))
    if user_answer == capitals[random]:
        user_score = user_score+1
    countries.pop(random)
    capitals.pop(random)
print('You got a total of {0} questions correct'.format(user_score))
