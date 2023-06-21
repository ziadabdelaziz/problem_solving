#!/usr/bin/python3

def main():
    landr = input()

    l, r = [int(x) for x in landr.split(" ")]
    found = False

    for i in range(l, r - 1):
        for j in range(i + 1, r):
            for k in range (j + 1, r + 1):
                if (gcd(i, j) == 1 and gcd(j, k) == 1) and gcd(i, k) != 1:
                    print(i, j , k)
                    found = True
                    return

    if not found:
        print(-1)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

main()
