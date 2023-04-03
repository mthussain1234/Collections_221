# TASK 1.2

We want to create 3 different Menus for Starter, Mains and Dessert, and put them into list form.

```commandline
starter_menu = ["calamari", "samosa", "sandwiches"]
main_menu = ["pasta", "pizza", "risotto"]
dessert_menu = ["cake", "ice cream", "apple pie"]
```
When printing out each list we must make sure they are correctly formatted for the ease of the customer.

Using the `sep` and `\n`, we can separate items and add new lines to allow for easier reading

We also use `*` to remove commas and square brackets for easier reading.

```commandline
print("Starter Menu:")
print(*starter_menu, sep = "\n")

print("\nMain Menu:")
print(*main_menu, sep = "\n")

print("\nDessert Menu:")
print(*dessert_menu, sep = "\n")
```

We initialize an empty list to store customer's order using:

`cust_order = []`

To allow for the customer to pick what they want we use the code below:
```
print("\nSelect one item from starter menu")
starter_item = input()
print("Select one item from main menu")
main_item = input()
print("Select one item from dessert menu")
dessert_item = input()
```

The list we initialised before will now be of use as we  will store the customers answers into their own list to allow for it to be printed back to them.

```commandline
cust_order.append(starter_item)
cust_order.append(main_item)
cust_order.append(dessert_item)
```
Finally the customer order has to be printed back to them for confirmation and the code is as follows:

```commandline
print("\nYour order is as follows:")

print(*cust_order, sep = "\n")
```