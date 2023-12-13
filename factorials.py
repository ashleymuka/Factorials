'''
Description: Create a program to calculate the
factorial of a nonnegative integer using recursion

'''

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)


if __name__ == "__main__":

    try:

        num = int(input("Enter a nonnegative number: \n"))

        while num < 0:
            num = int(input("Please enter a nonnegative number. \n"))

        else:
       
            fact = factorial_recursive(num)
            print(f'The factorial of {num} is {fact}')

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
    
            


    




    


























        
