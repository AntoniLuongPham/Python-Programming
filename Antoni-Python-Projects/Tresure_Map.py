# import vars
row_1 = ["b", "b", "b"]
row_2 = ["b", "b", "b"]
row_3 = ["b", "b", "b"]
two = []

# place the "a" some where......
def find_where_to_place_the_a():
    global two
    global row_1
    global row_2
    global row_3
    # if the x(first number) = 1
    if two[0] == 1:
        # if the y(second number) = 1
        if two[1] == 1:
            row_1 = ["a", "b", "b"]
        elif two[1] == 2:
            row_2 = ["a", "b", "b"]
        elif two[1] == 3:
            row_3 = ["a", "b", "b"]
    elif two[0] == 2:
        if two[1] == 1:
            row_1 = ["b", "a", "b"]
        elif two[1] == 2:
            row_2 = ["b", "a", "b"]
        elif two[1] == 3:
            row_3 = ["b", "a", "b"]
    elif two[0] == 3:
        if two[1] == 1:
            row_1 = ["b", "b", "a"]
        elif two[1] == 2:
            row_2 = ["b", "b", "a"]
        elif two[1] == 3:
            row_3 = ["b", "b", "a"]
    print(row_1)
    print(row_2)
    print(row_3)


# main program
def main():
    global two
    global row_1
    global row_2
    global row_3
    print(row_1)
    print(row_2)
    print(row_3)
    one = str(input("Where do you want to put the a? EX: 31? "))
    for c in one:
        two.append(int(c))
    find_where_to_place_the_a()


main()
