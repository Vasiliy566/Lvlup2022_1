class ResourceForWith:
    def __init__(self, filepath):
        self.file = open(filepath)

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()


with ResourceForWith("test.txt") as file:
    file.read()

with open("test.txt") as file:
    ...
