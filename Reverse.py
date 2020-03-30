z = int(input("Enter the number"))
rev = 0
while z > 0:
    a = z % 10
    rev = rev * 10 + a
    z = z // 10
print(rev)
    
