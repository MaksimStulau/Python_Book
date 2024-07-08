def fuel_calculator(litres, price_per_litre):

    full_price = litres * price_per_litre
    price = 100

    if litres >= 2:
        price_per_litre -= 10
        price = price_per_litre

    if litres >= 4:
        price_per_litre -= 10
        price = price_per_litre

    if litres >= 6:
        price_per_litre -= 5
        price = price_per_litre

    return price


print(fuel_calculator(5, 100))
