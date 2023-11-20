"""A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50.They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise."""

print ("The USB stick are priced at 6$ a piece. \nNote: The girl has 50$")
a = int(input("How many USB sticks can the girl buy:"))
b = int(50-(a*6))
print("Change:\n",b)