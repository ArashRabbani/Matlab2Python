# 1
for I in range(1,6):
    print(I)

# 2
I=1;
while I<=5:
    print(I)
    I=I+1;

# 3
for I in range(1,6):
    print(I)
    if I==3:
        break
    
# 4
for I in range(1,6):
    if I==3:
        continue 
        print(I)

# 5
for I in range(1,6):
    if I==3 and I<4:
        continue
    
    print(I)

# 6
for I in range(1,6):
    if I==3 or I==4:
        continue
    print(I)

# 7
for I in range(1,6):
    if I!=3:
        print(I)
        