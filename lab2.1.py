import random

while True:
    name = input("Please enter your name: ")
    age = input("Hello, " + name + "! How old are you? ")
    food = input("Do you like pizza or pasta? ")

    if food.lower() == "pizza":
        print("Sorry, " + name + ", we have to ask my parents before we can get pizza tonight.")
    else:
        print("Awesome, " + name + "! We're going to Olive Garden and ordering pasta tonight!")
        for i in range(random.randint(1, 5)):
            print("Yum")

    another_person = input("Does someone else want to go to dinner? ")
    if another_person.lower() != "y" and another_person.lower() != "yes":
        print("Thanks for dinner, " + name + "!")
        break



import random

def dinner_plans(name, age, food):
    if food.lower() == "pizza":
        print("Sorry, " + name + ", we have to ask my parents before we can get pizza tonight.")
    else:
        print("Awesome, " + name + "! We're going to Olive Garden and ordering pasta tonight!")
        for i in range(random.randint(1, 5)):
            print("Yum")

    another_person = input("Does someone else want to go to dinner? ")
    if another_person.lower() != "y" and another_person.lower() != "yes":
        print("Thanks for dinner, " + name + "!")
        return True
    else:
        return False

def main():
    while True:
        name = input("Please enter your name: ")
        age = input("Hello, " + name + "! How old are you? ")
        food = input("Do you like pizza or pasta? ")
        stop = dinner_plans(name, age, food)
        if stop:
            break

if __name__ == "__main__":
    main()




