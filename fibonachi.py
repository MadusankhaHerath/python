def fibonacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return  fibonacci(n-1) + fibonacci(n-2)


while True:
    num = int(input("enter number :"))

    if num==-1:
        break

    result = fibonacci(num)
    print (f"number is {result}")
