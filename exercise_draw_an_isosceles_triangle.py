# a function that prints 
def isosceles():
    num = int(input("Enter any number: "))
    for i in range (0, num+1):
        for j in range(0, num-i+1):
            print(end=" ")
        for j in range(i,0,-1):
            print("#", end="")
        for j in range(2, i+1):
            print("#", end="")
        print()

isosceles()
    
        

