def pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(str(j) + " ", end='')
        print()


def pattern2(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print('  ', end='')
        for j in range(i, 1, -1):
            print(str(j) + " ", end='')
        for j in range(1, i + 1):
            print(str(j) + " ", end='')
        print()


def pattern3(n):
    for i in range(1, n + 1):
        for j in range(n - i + 1, 0, -1):
            print(str(j) + " ", end='')
        print()


def pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(str(i) + " ", end='')
        print()


def pattern5(n):
    for i in range(1, n + 1):
        for j in range(i - 1):
            print('  ', end='')
        for j in range(i, n + 1):
            print(str(j) + " ", end='')
        print()


def pattern6(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == (n - 1):
                print('*   ', end='')
            else:
                if j == 0 or j == (n - 1):
                    print('*   ', end='')
                else:
                    print('    ', end='')
        print()


def pattern7(n):
    for i in range(n):
        for j in range(n):
            print('*   ', end='')
        print()


def pattern8(n):
    for i in range(n):
        for j in range(n - i - 1):
            print('  ', end='')
        for j in range(2 * i + 1):
            print('* ', end='')
        print()


rows = int(input("Enter Number of Rows: "))

print('>>> Pattern 1')
pattern1(rows)
print()
print('>>> Pattern 2')
pattern2(rows)
print()
print('>>> Pattern 3')
pattern3(rows)
print()
print('>>> Pattern 4')
pattern4(rows)
print()
print('>>> Pattern 5')
pattern5(rows)
print()
print('>>> Pattern 6')
pattern6(rows)
print()
print('>>> Pattern 7')
pattern7(rows)
print()
print('>>> Pattern 8')
pattern8(rows)
print()
