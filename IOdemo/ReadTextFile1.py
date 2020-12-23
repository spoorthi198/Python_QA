import  os
file_path = os.getcwd()
os.path.dirname(file_path)
print(file_path)
with open(os.path.dirname(file_path)+"\\textfile") as file:
    print("current status", file.closed)
    content = file.read()
    print(content)


print("current status", file.closed)
