# Design and implement a program that allows the user to enter the price of an item. The program calculates the amount of VAT to be paid at 20%. 
# The VAT amount and total price are then displayed.

# We're asking the user to enter the price of the item
Number = int(input("Please enter the price: \n"))

# We're printing a message to inform that calculation is taking place
Calcuate = print("Calculating, Please wait......\n")

# We're taking the number inputed by the user and devide it by 5 in order to find out the 20% discount
Calcuation = print ("20% of", Number, "is £",Number/5)

# We're now going to display the final price after discount
FinalPrice = print ("The final price is ", "is £",(Number-(Number/5)),"!")
