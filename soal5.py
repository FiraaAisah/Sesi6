for i in range(5, 0, -1):
    for j in range(i, 6):
        print("_" if j < i else j, end=" ")
    print()
