n = int(input("Enter the size of the list "))
print("\n")
numList = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())[:n]
print("User List: ", numList)
b = []
for i in range(0, n):
    ele = numList[i] * 0.45359237
    b.append(ele)
print(b)




