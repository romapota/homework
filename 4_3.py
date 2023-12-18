# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def sorted_word(word):
    m = [i for i in word]
    m_n = sorted(m)
    new_word = ''.join(m_n)
    return new_word
def print_hi(name):
    m = []
    m_n = []
    t = []
    R = int(input())
    for i in range(R):
        r = str(input())
        m.append(r)
    for i in m:
        for j in m:
            if len(i) == len(j):
                n_i = sorted_word(i)
                n_j = sorted_word(j)
                if n_j == n_i:
                    t.append(j)
        if t not in m_n:
            m_n.append(t)
        t = []
    print(m_n)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
