a=[5667,2346,5323,7896]
max1=0
min1=a[0]
max2=0
min2=a[-1]
c=0
for i in range(0,4):
    if a[i]>max1:
        max1=a[i]
    if a[i]<min1:
        min1=a[i]
for i in range(0,4):
    if a[i]<max1 and a[i]>max2:
        max2=a[i]
    if a[i]>min1 and a[i]<min2:
        min2=a[i]
print(max2,min2)
