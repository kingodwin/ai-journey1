item_1_price = int(input("How much does item 1 cost?"))
item_1_quantity = int(input("How many of the item 1 do you want to buy?"))
item_2_price = int(input("How much does item 2 cost?"))
item_2_quantity = int(input("How many of the item 2 do you want to buy?"))

item_1 = item_1_price * item_1_quantity
item_2 =  item_2_price * item_2_quantity
grand_total = item_1 + item_2

print(f"Item_1: {item_1_price} * {item_1_quantity} = {item_1}")
print(f"Item_2: {item_2_price} * {item_2_quantity} = {item_2}")
print(f"Grand_total: {grand_total}")
