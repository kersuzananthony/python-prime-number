import math
import time

print("Welcome to the prime number program")
inLoop = True
beginTime = time.process_time()

while inLoop:
    numberOfPrimeNumberWanted = int(input("How many prime number do you want to find? "))
    numberToBeginWith = int(input("From which number do you want to begin? "))
    numberOfPrimeFounded = 0

    while numberOfPrimeFounded <= numberOfPrimeNumberWanted:
        isPrime = True

        if numberToBeginWith % 2 == 0 and numberToBeginWith != 2:
            isPrime = False

        if isPrime:
            for i in range(3, math.ceil(math.sqrt(numberToBeginWith)), 2):
                if numberToBeginWith % i == 0:
                    isPrime = False
                    break

        if isPrime:
            print(str(numberOfPrimeFounded) + " - " + str(numberToBeginWith) + " is a prime number.")
            numberOfPrimeFounded += 1

        numberToBeginWith += 1

    # Program found all the wanted prime number
    endTime = time.process_time()
    print("{0} prime numbers found in {1}".format(numberOfPrimeNumberWanted, endTime - beginTime))
    userWantToContinue = input("Do you want to continue? (Y/n) ")
    if userWantToContinue != "Y":
        inLoop = False
