def sum(num1,num2):
    num1=int(input("enter value 1\n"))
    num2 = int(input("enter value 2\n"))
    sum=num1+num2
    print("summation is",sum)
def mul(num1,num2):
    num1 = int(input("enter value 1\n"))
    num2 = int(input("enter value 2\n"))
    mul=num1*num2
    print("Multiplication is ",mul)
def div(num1,num2):
    num1 = int(input("enter value 1\n"))
    num2 = int(input("enter value 2\n"))
    if num1>num2:
        div=num2/num1
    else:
        div=num1/num1
    print("Division is ",div)

def sub(num1,num2):
    num1 = int(input("enter value 1\n"))
    num2 = int(input("enter value 2\n"))
    sub=num2-num1
    print("Substraction is ",sub)

print("Now printing the values\n")
sum(0,0)
mul(0,0)
div(0,0)
sub(0,0)
