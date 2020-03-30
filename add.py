void add(a,b):
    if(a!=b):                    
        return ((a*a-b*b)/(a-b))
    else:
        return 2*a      
void main():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number :"))
    print(add(a,b))
main()
