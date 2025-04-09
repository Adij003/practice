#bubble sort

arr = [24, 12, 45, 22, 67, 10]
# arr = [12, 24, 45, 22, 67, 10]
# arr = [12, 24, 45, 22, 67, 10]
# arr = [12, 24, 22, 45, 67, 10]
# arr = [12, 24, 22, 45, 67, 10]
# arr = [12, 24, 22, 45, 10, 67]

length = len(arr)
for i in range(length):
    for j in range(length-i-1):
        if(arr[j]>arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)