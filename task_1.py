try:
    with open("for_task_1.txt", "w") as f:
        line = input("Enter some text or data: ")
        while line:
            f.writelines(line + "\n")
            line = input("Enter some text or data: ")
            if not line:
                break

except IOError:
    print("Input Output Error")
