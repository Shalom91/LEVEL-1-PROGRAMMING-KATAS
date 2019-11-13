# check if interger is an even or odd number
def even_or_odd():
    num = int(input("Enter a number: ")) # input interger
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))
even_or_odd()
