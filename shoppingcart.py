cart = []
prices = []
total = 0

while True:
    food = input("Enter a product (press x to quit): ").lower()
    if food == "x":
        break
    else:
        price = float(input(f"What is the price of {food}: "))
        cart.append(food)
        prices.append(price)
        total = price + total
print("--------------YOUR CART-----------------")
for food in cart:
    print(food, end= " ")

print()
print(f"The total is ${total:.2f}")
 

print("-----------------------------------------")