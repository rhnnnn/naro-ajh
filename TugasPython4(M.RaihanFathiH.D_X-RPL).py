#Input
Start=int(input("Initial Number= "))
End=int(input("Final Number= "))
times=1
#Process
print('Number between %d and %d' %(Start,End))

for a in range(Start,End+1,3) :
    print(a, end=' ')
    times=times*a


#Final Result    
print("\nFinal Result = ", times)