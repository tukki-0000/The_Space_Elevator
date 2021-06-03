print("Start a number guessing game!")
print("Range of number is 1~10")


answer = 7

guess = int(input("The number you expect  "))
#print(guess)
#print(type(guess))
tries = 1

#back
while(guess != answer):
    if(guess > answer):
        print("Less than you expected answer")

    else:
        print("Greatest than you expected answer")

    tries = tries + 1
    guess = int(input("The number you expect  "))
#one more

print("Correct!! answer is {}".format(answer))
print("Number of your trial is {}".format(tries))
