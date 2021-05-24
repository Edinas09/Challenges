def bs(a):
    b = len(a)-1
    print(f"valor de b = {b}")
    print(range(b))
    counter = 0

    for x in range(b):
        # print(a)
        # print(f"entrou primeiro loop {x}")
        # print(range(b - x))
        for y in range(b - x):
            # print(f"entrou segundo loop valor de x : {x}   | valor de y: {y}")
            if a[y] > a[y+1]:
                # print("done")
                a[y], a[y+1] = a[y+1], a[y]
                counter = counter + 1
    print("Array is sorted in {} swaps.".format(counter))
    print("First Element: {}".format(a[0]))
    print("Last Element: {} ".format(a[-1]))
    return a

a = [6,4,1]
print(bs(a))

