def main():
    ls = list(map(int, input().split()))
    # ls = [1,2,8,9,12,46,76,82,15,20,30]

    dct = {}
    for i in range(1,10):
        dct[i] = 0

    for num in ls:
        for i in range(1,10):
            if num % i == 0:
                dct[i] += 1

    print(dct)

main()