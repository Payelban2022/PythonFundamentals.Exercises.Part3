import random
n = random.randint(0,10)

guess = int(input("Give me a number : "))

while guess != n:
    if guess < n:
        print("Too low")
        print(("The random no. was :") + str(n))
        print(("Your guess was:") + str(guess))

    else:

        print("Too high")
        print(("The random no was:")+str(n))
        print(("Your guess was:") + str(guess))
    break
