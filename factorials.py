'''
Author: Ashley Muka
Assignment Title: Factorials
Assignment Description: Create a program to calculate the
factorial of a nonnegative integer using recursion
Due Date:11/03/2023
Date Created:10/30/2023
Date Last Modified:11/02/2023

'''

#process
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)


if __name__ == "__main__":

    try:
#input      
        num = int(input("Enter a nonnegative number: \n"))

        while num < 0:
            num = int(input("Please enter a nonnegative number. \n"))

        else:
#output            
            fact = factorial_recursive(num)
            print(f'The factorial of {num} is {fact}')

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
    
            


    




    


























        
