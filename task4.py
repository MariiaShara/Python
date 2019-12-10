text = input("Please enter some words, separating them by the space key: ")
text_list = text.split(" ")
for ind, el in enumerate(text_list, 1):
    print(ind, el[:10])
