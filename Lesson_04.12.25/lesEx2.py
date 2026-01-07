def graduate():
    grate = int(input ("Enter your count of points: \n"))
    
    if( grate <= 100 and grate >= 90 ):
        print("Your grate is: A")
        if(grate == 100):
            print("SUPER!!!")
    elif( grate <= 89 and grate >= 80):
        print("Your grate is: B")
    elif( grate <= 79 and grate >= 70):
        print("Your grate is: C")
    elif( grate <= 69 and grate >= 60):
        print("Your grate is: D")
    elif( grate <= 59 and grate >= 50):
        print("Your grate is: E")
    elif( grate <= 49 and grate >= 1):
        print("Your grate is: F")
    else:
        print("Invalid count.")
        graduate()
        

graduate()
