
# import entre
# import dessert
from Appetizer2 import appetizer

# imports functions

print("Welcome to UNW Team Three's Restaurant")
print()

AppCheck = "y"
EntreCheck = "y"
DessertCheck = "y"

# determines loop conditions

AppetizerSubtotal = float(0)
EntreSubtotal = float(0)
DessertSubtotal = float(0)

# global subtotals

while AppCheck == "y":
    try:
        AppetizerPeople = float(input("How many people will be eating appetizers?"))
        AppetizerCost = float(input("How much does the appetizer cost?"))
        AppetizerSubtotal += appetizer(AppetizerPeople, AppetizerCost)
        # These lines gather information and send it to the appetizer function
        AppCheck = input("would you like to order another appetizer? If yes, type y. Type any other key to continue.")
        # determine if the user wants to order a different item
    except ValueError:
        print("Could not convert data to a float. Please input data as an float.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

while EntreCheck == "y":
    try:
        EntrePeople = float(input("How many people will be eating entres?"))
        EntreCost = float(input("How much does the appetizer cost?"))
        EntreSubtotal += entre(EntrePeople, EntreCost)
        # These lines gather information and send it to the entre function
        EntreCheck = input("would you like to order another entre? If yes, type y. Type any other key to continue.")
        # determine if the user wants to order a different item
    except ValueError:
        print("Could not convert data to a float. Please input data as an float.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

while DessertCheck == "y":
    try:
        DessertPeople = float(input("How many people will be eating desserts?"))
        DessertCost = float(input("How much does the appetizer cost?"))
        DessertSubtotal += dessert(DessertPeople, DessertCost)
        # These lines gather information and send it to the dessert function
        DessertCheck = input("would you like to order another dessert? If yes, type y. Type any other key to continue.")
        # determine if the user wants to order a different item
    except ValueError:
        print("Could not convert data to a float. Please input data as an float.")
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

Total = DessertSubtotal + EntreSubtotal + AppetizerSubtotal
print(f"Your total come to ${Total:,.2f}")
# calculate total
