# Help
"""
 start = for starting the car
 stop = for stopping the car
 quit = exiting the game
 """


command = ''

started = False
while True:
    command = input("pls enter the cmd > ").lower()
    if(command == 'start'):
        if started:
            print("car is already started")
        else:
            started =True
            print("car started")
    elif(command == 'stop'):
        if not started:
            print("car is alreasy stopped")
        else:
            started = False
            print("car stopped")
    elif(command == 'help'):
        print("""
 start = for starting the car
 stop = for stopping the car
 quit = exiting the game
 """)
    elif(command=='quit'):
        break
    else:
        print("sorry i dont understand the command")
