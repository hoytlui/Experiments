from menu import MENU
from resources import resources


# global variable
profit = 0


def print_report():
    """Return report"""
    global profit
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = profit
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def make_coffee(choice):
    """Subtract ingredients used from resources"""
    for ingredient, value in MENU[choice]['ingredients'].items():
        resources[ingredient] = resources[ingredient] - value


def is_resources_sufficient(choice):
    """Return True if resources are sufficient, False otherwise"""
    for ingredient, ingredient_value in MENU[choice]['ingredients'].items():
        if ingredient_value > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_payment(choice):
    global profit
    # calculate money received
    quarters = int(input("How many quarters do you have? "))
    dimes = int(input("How many dimes do you have? "))
    nickles = int(input("How many nickles do you have? "))
    pennies = int(input("How many pennies do you have? "))
    money_received = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    # compare money received against cost
    cost = MENU[choice]['cost']
    if money_received < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        profit += cost
        change = round(money_received - cost, 2)
        print(f"Here is ${change} in change. Enjoy your coffee.")
        


is_on = True
while is_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino)\n")
    # enter 'off' to exit loop
    if choice == 'off':
        is_on = False
    # enter 'report' to print resources available
    elif choice == 'report':
        print_report()
    # check resources, process payment, make coffee
    else:
        if is_resources_sufficient(choice) == True:
            process_payment(choice)
            make_coffee(choice)

# print resources remained
print_report()

