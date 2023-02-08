square = 0
s = 0
for i in range(1, 101):
    square += i**2
    s += i
s = s**2
print(s - square)


7 100001st prime


lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))
l=[]

print("The Prime Numbers sum is: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            l.append(number)
x = sum(l)
print(x)
