def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    number = int(input())
    c = 0
    m = []
    p = 0
    p_p = 0
    for i in range(1, len(str(number))+1):
        m.append(((number%(10**i))-p)//10**(i-1))
        p += ((number%(10**i))-p)
    new_number = ''
    for i in m:
        new_number += str(i)
    if int(new_number) == number:
        print(True)
    else:
        print(False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
