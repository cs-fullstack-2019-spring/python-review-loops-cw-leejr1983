def main():
    #exercise1()
    #exercise2()
    exercise3()


# Exercise 1:
# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Hint: Use 'continue' statement.
# Expected Output : 0 1 2 4 5


def exercise1():
    for numbers in range (0,6):
        if (numbers != 3 and numbers != 6):
            print (numbers)


# Exercise 2:
# Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4

def exercise2():
    evenNumbers= 0
    oddNumbers= 0
    for numbers in range (0,9):
        if (numbers  %2 == 0):
            evenNumbers += 1
        else:
            oddNumbers += 1

    print("Number of even numbers:", str(evenNumbers))
    print("Number of odd numbers:", str(oddNumbers))


# Exercise 3:
# Write a Python program that accepts a sequence of lines (blank line to terminate)
# as input and prints the lines as output after User enters a blank line to end.
# Do not use an array to hold the lines of text
# Hints: You can use "\n" if you want to add a line break between sentences

def exercise3():
    sequence= ""
    while True:
        userInput= input("Please enter your input")





















if __name__ == '__main__':
    main()