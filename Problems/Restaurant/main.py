import itertools

combined_meal = itertools.product(main_courses, desserts, drinks)
combined_prices = itertools.product(price_main_courses, price_desserts, price_drinks)

for meal, prices in zip(combined_meal, combined_prices):
    cost = sum(prices)
    if cost <= 30:
        print(' '.join(meal), cost)
