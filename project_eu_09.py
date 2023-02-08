def Pythagorem_triplet():
    total = 1000
    for a in range (1 , 1001):
        for b in range(a+1 , 1000):
            c = total - a - b
            # print(a , b, c)
            if a**2 + b**2 == c**2:
                return str(a*b*c)


if __name__ == "__main__":
    print(Pythagorem_triplet())
