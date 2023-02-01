fib = [1,2]
while fib[-1]<=4000000:
    fib.append(fib[-1] + fib[-2])
print(fib)
l1 = []
for i in fib:
    if i%2==0:
        l1.append(i)
print(l1)
print(sum(l1))
