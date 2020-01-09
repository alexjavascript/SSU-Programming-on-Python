print("Welcome to Simple Calculator")

operation = input("What would you like to do? (+ -): ")

if (operation == "+" or operation == "-"):
    
    a = float(input("Inter first  number: "))
    b = float(input("Inter second number: "))
    
    if (operation == "+"):
        c = a + b
        print( "Result is: " + str(c) )
    else
        c = a - b
        print( "Result is: " + str(c) )   

else:
    print("Please, enter valid operation (+ -)")