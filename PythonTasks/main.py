from menu import MENU

coffeemachine = {"water": {"quantity": 1000, "value": "ml"},
                 "milk": {"quantity": 500, "value": "ml"},
                 "coffee": {"quantity": 100, "value": "g"},
                 "money": {"quantity": 5.0, "value": "$"}}


def checkresources(drinktype):
    is_enough = True
    for i in MENU[drinktype]["ingredients"]:
        if coffeemachine[i]["quantity"] < MENU[drinktype]["ingredients"][i]:
            is_enough = False
            print(f"Sorry, there is not enough {i}")
            break
    return is_enough


def howmuch():
    quarters = 0.25 * int(input("How many quarters: "))
    dimes = 0.1 * int(input("How many dimes: "))
    nickels = 0.05 * int(input("How many nickels: "))
    pennies = 0.01 * int(input("How many pennies: "))

    total = quarters + dimes + nickels + pennies
    return total


def checkmoney(money, drinktype):
    cost = MENU[drinktype]["cost"]
    if cost > money:
        print(f"You paid ${money}, {drinktype} costs ${cost}. Please pay extra ${round(cost - money, 2)}")
        return False
    elif cost < money:
        print(f"You paid ${money}, {drinktype} costs ${cost}. Here is your change ${round(money - cost, 2)}")
        return True
    else:
        return True


while True:
    choice = input("What would you like to drink? espresso/latte/cappuccino: ")

    if choice == "off":
        break
    elif choice == "report":
        for i in coffeemachine:
            print(i + ": " + str(coffeemachine[i]["quantity"]) + " " + coffeemachine[i]["value"])
    else:
        if checkresources(choice):
            if checkmoney(howmuch(), choice):
                coffeemachine["money"]["quantity"] += MENU[choice]["cost"]
                for i in MENU[choice]["ingredients"]:
                    coffeemachine[i]["quantity"] -= MENU[choice]["ingredients"][i]
                print(f"Here is your {choice}. Enjoy!")