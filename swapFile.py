
def swapFile():
    file1 = input("enter name of first file:- ")
    file2 = input("enter name of second file:- ")


    with open(file1, 'r') as a:
        data_a = a.read()
        print(data_a)
    with open(file2, 'r') as b:
        data_b = b.read()
        print(data_b)
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as b:
        b.write(data_a)

swapFile()