try:
    file = open("demo.txt","r")
    data = file.read()
    print(data)
except Exception as e:
    print("somthing wrong with file",e)
finally:
    file.close()