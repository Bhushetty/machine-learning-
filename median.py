data = [10, 2, 8, 4]

data.sort()
n = len(data)

if n % 2 == 1:
    median = data[n // 2]
else:
    median = (data[n // 2 - 1] + data[n // 2]) / 2

print(median)
