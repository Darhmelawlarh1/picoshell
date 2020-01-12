cost_price = int(input("Enter your cost price:"))
selling_price = int(input("Enter your selling price:"))
Sales = selling_price - cost_price
if (int(Sales) <= 6500):
    print("You made a loss of {}".format(Sales))
else:
    print("You made a profit of {}".format(Sales))
