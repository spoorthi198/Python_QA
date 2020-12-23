try:
    num1 = int(input("enter the number :> "))
    num2 = int(input("enter the number :> "))
    result = num1/num2
    print(result)
except TypeError as err:
    print("somthing went wrong", err)
except ValueError as err:
    print("somthing went wrong", err)
except Exception as e:
    print("some problem occured", e)
else:
    print("no error")  # this block will get executed when no exception raised
finally:
    print("prod ended") # this will always gets executed


num1 = int(input("enter the number: > "))
if(num1 == 0):
    raise AssertionError

print("something wen wrong")