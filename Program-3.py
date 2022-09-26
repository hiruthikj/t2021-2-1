def main():
    a = int(input("Enter a: "))
    if a%2 == 1:             # odd
        for i in range(1, 2*a, 2):
            print(i, end=",")
    else:                    # even
        for i in range(1, 2*a-2, 2):
            print(i, end=",")

main()