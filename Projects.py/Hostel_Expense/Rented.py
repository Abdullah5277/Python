
rooms=int(input("Enter the total persons in the room ="))
hostel=int(input("Enter the Hostel Rent = ")) 
Food=int(input("Enter the Food Expense =")) 
electricirty=int(input("Enter the electricity rate =")) 
units=int(input("Enter total units that are used ="))

electricirty_units=electricirty*units 

output=(hostel+Food+electricirty_units)/rooms

print(f"Total costs of each are : {output}")