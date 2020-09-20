# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Short cut of reformat is : Alt + Shift + Enter
# ctrl + shift + f10 to execute tests


def concatenateStringWithInt():
    a = 5
    b = 2.5
    c, d, e = 1, 1.7, "Hello"
    print("{}{}".format("I am string ", a))
    print(type(b))
    print(type(e))
    print(e + " string")  # same data types can be concatenated with + sign


def listDataType():
    listvalues = [1, 2, "Hello", 3]
    print(listvalues[0])  # Print first value
    print(listvalues[-1])  # Print last value
    print(listvalues[1:3])  # Prints [2, 'Hello']
    print(listvalues)  # Prints the whole list

    listvalues.insert(3, "World")
    print("{}{}".format("After addition :", listvalues))  # Prints the list

    del listvalues[3]  # deletes the index 3 value
    print("{}{}".format("After deletion :", listvalues))  # Prints the list

    listvalues.append("End")
    print(listvalues)  # Prints the whole list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # concatenateStringWithInt()
    listDataType()
