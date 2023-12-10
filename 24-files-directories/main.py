with open("/Users/mahasan/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)

with open("../../../../../Desktop/my_file.txt") as file:
    content = file.read()
    print(content)

with open("/Users/mahasan/Desktop/my_file.txt", mode="a") as file:
    # file.write("\nThis is a beautiful start.")
    file.write("\nTrying to write with absolute path.")

with open("../../../../../Desktop/my_file.txt", mode="a") as file:
    file.write("\nTrying to write with relative path.")