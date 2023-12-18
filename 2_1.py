# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    s = str(input())
    m = []
    str_n = ''
    for i in s:
        if i not in str_n:
            str_n += i
        else:
            m.append(str_n)
            str_n = ''
            str_n += i
    m.append(str_n)
    print(max(m))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
