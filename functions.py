def make_pizza (size , *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni' )


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {'fisrt': first , 'last': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

users_1 = build_profile('albert', 'einstein', location='princeton', field='physics')
print(users_1)


    