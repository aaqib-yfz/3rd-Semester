stack = []


while True:

    print("1: Push")
    print("2: Pop")
    print("3: Quit")

    def empty():
        if len(stack) == 0:

            print("Stack is Empty")

    var = int(input('Enter your choice from 1 to 3 : '))

    if var == 1:
        val1 = input("Enter element you want to add : ")
        stack.append(val1)
        print(stack)
    elif var == 2:

        if len(stack) != 0:
            val2 = stack.pop()
            print(val2)


        else:
            empty()
    elif var == 3:
        print("you are quit")
        break



