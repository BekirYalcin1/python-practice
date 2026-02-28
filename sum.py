
total = 0

while True:
    num = input("Enter a number: ")
    
    try:
        num = float(num)
        
    except:
        print("Error, please enter a numeric value")
        exit()
    total = total + num

    ask = input("Do you want to enter another number? (yes/no): ")
    if ask == "yes":
            continue
    elif ask == "no":
         break
    
print("The total is:", total)