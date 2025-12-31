# write a program using a user defined function that displays sum of first n natural numbers , where n is passed as an argument 

def sumSquares(n):
    sum =0
    for i in range(1,n+1):
        sum = sum + i
    print("The sum of first", n , sum)
    

sumSquares(10)        