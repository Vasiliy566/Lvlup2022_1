# f = open('data/example.txt', encoding="utf8")
# i = 0
# # some action with file
# f.close()

# f = open('data/example.txt', encoding="utf8")
# with open("data/example.txt", encoding="utf8") as f:
#     data = [line for line in f]
#
# print(data)
file_path = "data/example.txt"

with open(file_path, mode="a") as f:
    f.write("line1\n")
    f.write("line2\n")


# CODE

with open("data/example.txt", mode="r", encoding="utf8") as f:
    for line in f:
        print(line)
