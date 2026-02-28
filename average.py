total = 0.0
count = 0

while True:
    num = input("Enter a number: ")
    try:
        num = float(num)
    except:
        print("Error, please enter a numeric value")
        continue
    count += 1
    total = total + num

    continue_input = input("Do you want to enter another number? (yes/no): ")
    if continue_input.lower() == "yes":
        continue
    else:
        break

average = float(total / count)
print("The average is:", average)