import random
countries = ['England','Germany','Spain','China','Russia','Ireland','Scotland','France','Belgium','Wales']
capitals = ['London','Berlin','Madrid','Beijing','Moscow','Dublin','Edinburgh','Paris','Brussels','Cardiff']
print("REMEMBER CAPITALS")
random = random.randint(0,10)
user_answer = input("What is the capital of {0}? ".format(countries[random]))
if user_answer == capitals[random]:
    print("You got it correct.")
else:
    print("You got it wrong.")


