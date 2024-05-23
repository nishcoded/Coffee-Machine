from stock import menu, stock_level


def count_coins():
    """returns the total of the coins inserted"""
    print("Please insert coins!")
    sum = int(input("How many quarters? ")) * 0.25
    sum += int(input("How many dimes? ")) * 0.1
    sum += int(input("How many nickels? ")) * 0.05
    sum += int(input("How many pennies? ")) * 0.01
    return sum


def is_coins_enough(money_received, beverage_cost):
    """returns true if user inserts enough coins for the drink"""
    if money_received >= beverage_cost:
        change = round(money_received - beverage_cost, 2)
        print(f"\nHere is your change: ${change}")
        global profit
        profit += beverage_cost
        return True

    else:
        print(f"Sorry, the coins you inserted ${money_received} is short as it costs ${beverage_cost}!")
        print("Money refunded.")
        return False


def is_stock_enough(user_order_ingredients, beverage):
    """returns true if machine has got enough ingredient for the drink"""
    for item in user_order_ingredients:
        if user_order_ingredients[item] >= stock_level[item]:
            print(f"Sorry, we haven't got enough {item} for {beverage}.")
            return False

    return True


def update_stock(beverage, user_order_ingredients):
    """updates the ingredients in stock level"""
    for item in user_order_ingredients:
        stock_level[item] -= user_order_ingredients[item]
    print(f"Enjoy your {beverage}!")


profit = 0
continue_order = True
while continue_order:
    customer_choice = input("\nWhat would you like? Espresso, Latte, or Cappuccino: ").lower()

    if customer_choice == "off":
        continue_order = False

    elif customer_choice == "report":
        print(f"Coffee: {stock_level["coffee"]}g")
        print(f"Water: {stock_level["water"]}ml")
        print(f"Milk: {stock_level["milk"]}ml")
        print(f"Money received: ${profit}")

    else:
        coffee_name = menu[customer_choice]
        if is_stock_enough(coffee_name["ingredients"], customer_choice):
            payment = count_coins()
            if is_coins_enough(payment, coffee_name["price"]):
                update_stock(customer_choice, coffee_name["ingredients"])


















