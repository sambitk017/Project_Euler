def smallest_number(number):
    for i in range(1, 21):
        if number% i !=0:
            return False
    return True
number = 20
while True:
    if smallest_number(number):
        break
    number += 20
print(number)
