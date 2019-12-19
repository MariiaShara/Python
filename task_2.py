try:
    with open("for_task_2.txt") as f:
        content = f.readlines()
    print(f"В файле {len(content)} строк(и).")
    for i, line in enumerate(content, 1):
        line = str(line)
        print(f"{i} строка {len(line.split())} слов(а).")

except IOError:
    print("Input Output Error")
