def calculate_profit_margin(revenue,expense):
    profit=revenue-expense
    margin=profit*100/revenue
    return profit,margin

revenue=50
expense=10

profit,margin=calculate_profit_margin(revenue,expense)

print(f"Profit: {profit} and margin: {margin}")