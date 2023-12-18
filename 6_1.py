# This is a sample Python script.
import multiprocessing


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    R = int(input())
    R2 = int(input())
    m1 = set()
    m2 = set()
    for i in range(R):
        r = int(input())
        m1.add(r)
    print(m1)
    for i in range(R2):
        r = int(input())
        m2.add(r)
    print(m2)
    numbers = set()
    for i in m1:
        if i in m2:
            numbers.add(i)
    for i in m2:
        if i in m1:
            numbers.add(i)
    print(len(numbers), 'элемента: ', [i for i in numbers])
    numbers.clear()
    for i in m1:
        if i not in m2:
            numbers.add(i)
    for i in m2:
        if i not in m1:
            numbers.add(i)
    print(len(numbers), 'элемента: ', [i for i in numbers])
    numbers.clear()
    for i in m1:
        if i not in m2:
            numbers.add(i)
    print(len(numbers), 'элемента: ', [i for i in numbers])
    numbers.clear()
    for i in m2:
        if i not in m1:
            numbers.add(i)
    print(len(numbers), 'элемента: ', [i for i in numbers])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
