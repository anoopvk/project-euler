f = open("p022_names.txt")
a = f.read()
b = a.split('","')
# del b[0][0]
print(len(b))
b[0] = b[0].replace('"', "")
b[5162] = b[5162].replace('"', "")
print(b[0] < b[1])


def sortt(a):
    for j in range(len(a)):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                temp = a[i + 1]
                a[i + 1] = a[i]
                a[i] = temp
    return a


sorted = sortt(b)
total = 0
# print(ord("A"))
for name in range(len(sorted)):
    sum = 0
    for i in sorted[name]:
        number = ord(i) - 64
        sum += number
    sum = sum * (name + 1)
    print("sum =", sum)
    total += sum

print("total=", total)
