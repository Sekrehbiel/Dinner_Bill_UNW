
PeopleOrdering = int(input("How many people will be ordering appetizers?"))
LoopsCompleted = 0
AppetizerLoop = PeopleOrdering
AppetizerSubtotal = 0
while AppetizerLoop >= 1:
    LoopsCompleted += 1
    AppetizerOrders = int(input("How many people are ordering appetizer "f" #{LoopsCompleted}?"))
    AppetizerSubtotal += (float(input("How much does this appetizer cost?"))) * 3
    AppetizerLoop -= AppetizerOrders

