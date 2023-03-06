# file = open(r"C:\Users\xzqt\Desktop\hello.txt", mode = "r")
# data = file.readlines()
# print(data)

# file.close()

#to read files change "w to "r"
#write on files

try:
    with open(r"C:\Users\xzqt\Desktop\newfile.txt", mode="w") as file:
        file.writelines(["This is a new file that is created using Python.","\nThis is another line"])
        print("File created on desktop")
except FileNotFoundError:
    print("The file path is incorrect.")
except PermissionError:
    print("You don't have permission to write to this file.")
except Exception as e:
    print(f"An error occurred: {e}")


