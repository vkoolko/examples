if __name__ == '__main__':
    l = ['b1', 'b2', 'b3', 'b4', 'b5']
    for i in range(len(l)-1):
        one, two = l[i:i+2]
        print(one, two)

    dd = (tuple(l[i:i+2]) for i in range(len(l)-1))
    print(dd)
