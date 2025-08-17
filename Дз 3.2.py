ListA = [1, 5, 24, 4, 8, 15, 43, 2, 7]
ListB = [4, 7, 9, 23, 22, 2, 0, 2]
ListC = []

for item in ListA:
    if item in ListB:
        ListC.append(item)
print(ListC)
