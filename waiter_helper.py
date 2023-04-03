# Task 1.2


starter_menu = ["calamari", "samosa", "sandwiches"]
main_menu = ["pasta", "pizza", "risotto"]
dessert_menu = ["cake", "ice cream", "apple pie"]

# print menu in a formatted way
# order 3 times and have responses added to another list so not forgotten
# have order printed back to customer

print("Starter Menu:")
print(*starter_menu, sep = "\n")

print("\nMain Menu:")
print(*main_menu, sep = "\n")

print("\nDessert Menu:")
print(*dessert_menu, sep = "\n")

cust_order = []

print("\nSelect one item from starter menu")
starter_item = input()
print("Select one item from main menu")
main_item = input()
print("Select one item from dessert menu")
dessert_item = input()

cust_order.append(starter_item)
cust_order.append(main_item)
cust_order.append(dessert_item)

print("\nYour order is as follows:")

print(*cust_order, sep = "\n")





