MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffee_machine():
    ask_customer = input("What would you like to have? (espresso/latte/cappuccino): ")
    if ask_customer == "espresso" and resources["water"] >= 50 and resources["coffee"] >= 18:
        water_remaining = resources["water"] - 50
        milk_remaining = resources["milk"]
        coffee_remaining = resources["coffee"] - 18
        resources["water"] = water_remaining
        resources["milk"] = milk_remaining
        resources["coffee"] = coffee_remaining
    elif ask_customer == "latte" and resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
        water_remaining = resources["water"] - 200
        milk_remaining = resources["milk"] - 150
        coffee_remaining = resources["coffee"] - 24
        resources["water"] = water_remaining
        resources["milk"] = milk_remaining
        resources["coffee"] = coffee_remaining
    elif ask_customer == "cappuccino" and resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
        water_remaining = resources["water"] - 250
        milk_remaining = resources["milk"] - 100
        coffee_remaining = resources["coffee"] - 24
        resources["water"] = water_remaining
        resources["milk"] = milk_remaining
        resources["coffee"] = coffee_remaining
    elif ask_customer == "resources":
        print(resources)
    else:
        print("Lack of ingredients")
        exit()
    if ask_customer == "espresso":
        print("You have to pay $1.5")
    elif ask_customer == "latte":
        print("You have to pay $2.5")
    elif ask_customer == "cappuccino":
        print("You have to pay $3.0")
    if ask_customer == "espresso" or ask_customer == "latte" or ask_customer == "cappuccino":
        print("Please insert coins.")
        insert_dollars = int(input("How many dollars?: "))
        insert_scents = int(input("How many scents?: ")) * 0.1

        def total_amount_insert():
            total_amt = insert_scents + insert_dollars
            return total_amt

        total_amount = total_amount_insert()
        # print(total_amount)

        def money_return():
            if ask_customer == "espresso":
                return_money = total_amount - 1.5
                return return_money
            elif ask_customer == "latte":
                return_money = total_amount - 2.5
                return return_money
            elif ask_customer == "cappuccino":
                return_money = total_amount - 3.5
                return return_money

        money_returned = money_return()
        print(f"Here is your ${money_returned} in change.")
        print(f"Here is your {ask_customer}. Enjoy!!")
    elif ask_customer == "resources":
        print("Money = $0")


for i in range(1000):
    coffee_machine()
