largets = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num= float(num)
    except:
        print("Invalid input")
        continue
    if largets is None or num > largets:
        largets = num
    if smallest is None or num < smallest:
        smallest = num

print("Maximum is", largets)
print("Minimum is", smallest)