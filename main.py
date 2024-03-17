name = input("Hi there! What's your name? Enter here: ")
import time
time.sleep(1)
print("\nI see! That's a very cool name. Hello, " + name + "!")
time.sleep(1)
print("\nI'm going to ask a few questions!\n")
color = input("First, what's you're favorite color? ")
time.sleep(1)
print("\nThat's cool! " + color + " is a very cool color, " + name + "!\n")

season = input("Okay, now what's your favorite season? ")
time.sleep(1)
print("\nWow, that's cool, " + name + "! " + season + " is a very cool one!\n")
time.sleep(1)

animal = input("That's fun. What would you say your favorite animal is? ")
time.sleep(1)
print("\n" + animal + " are very nice," + name + "! Definitely cute :)")
time.sleep(1)

print("\nWell, it was very nice to meet you, " + name + "! I have stored all your information for legal usage. Thank you for giving it to me!\n")

print("So, your name is " + name + ", your favorite color is " + color + ", your favorite season is " + season + ", and your favorite animal is " + animal + "!")
time.sleep(1)
print("\nWell, it was very nice meeting you! See you soon :)")