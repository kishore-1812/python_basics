start=int(input("Enter the starting value: "))
end=int(input("Enter the ending value: "))
print(f"Prime numbers between {start} and {end} are:")
for i in range(start,end):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)