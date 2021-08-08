def pattern1(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print('    ', end='')
        for j in range(2 * i - 1):
            if i == n:
                print('*   ', end='')
            else:
                if j == 0 or j == (2 * (i - 1)):
                    print('*   ', end='')
                else:
                    print('    ', end='')
        print()


def pattern2(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print('    ', end='')
        for j in range(2 * i - 1):
            print('*   ', end='')
        print()


def pattern3(n):
    for i in range(n):
        for j in range(n - i):
            print('    ', end='')
        for j in range(2 * i + 1):
            if j == 0 or j == (2 * i):
                print('*   ', end='')
            else:
                print('    ', end='')
        print()

    for i in range(n - 1, 0, -1):
        for j in range(n - i + 1):
            print('    ', end='')
        for j in range(2 * i - 1):
            if j == 0 or j == (2 * (i - 1)):
                print('*   ', end='')
            else:
                print('    ', end='')
        print()


def pattern4(n):
    for i in range(n):
        for j in range(n - i):
            print('    ', end='')
        for j in range(2 * i + 1):
            print('*   ', end='')
        print()
    for i in range(n - 1, 0, -1):
        for j in range(n - i + 1):
            print('    ', end='')
        for j in range(2 * i - 1):
            print('*   ', end='')
        print()


def pattern5(n):
    for i in range(n):
        for j in range(i):
            print('  ', end='')
        for j in range(n - i):
            print('$ ', end='')
        print()


def pattern6(n):
    for i in range(n):
        for j in range(n - i - 1):
            print('  ', end='')
        for j in range(i + 1):
            print('# ', end='')
        print()


rows = int(input("Enter Number of Rows: "))
print(">>> Pattern 1")
pattern1(rows)
print()
print(">>> Pattern 2")
pattern2(rows)
print()
print(">>> Pattern 3")
pattern3(rows)
print()
print(">>> Pattern 4")
pattern4(rows)
print()
print(">>> Pattern 5")
pattern5(rows)
print()
print(">>> Pattern 6")
pattern6(rows)
print()
