data = [10, 2, 8, 4]

n = len(data)


for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]


if n % 2 != 0:
    median = data[n // 2]
else:
    mid1 = data[n // 2 - 1]
    mid2 = data[n // 2]
    median = (mid1 + mid2) / 2

print("Sorted list:", data)
print("Median:", median)
