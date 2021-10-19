# Profit and Loss Calculator

def profit_calc(cost, sell):
    if (cost == sell):
        return False

    elif (cost < sell):
        return (sell - cost)

    elif (cost > sell):
        return (sell - cost)

if (__name__ == "__main__"):
    cost_input = int(input("Cost of making or buying the product: "))
    sell_input = int(input("Cost of the sold product: "))

    profit = profit_calc(cost_input, sell_input)

    if (profit == False):
        print("You are not making or losing money.")
    elif (profit < 0):
        print("$" + str(abs(profit)), "loss.")
    else:
        print("$" + str(abs(profit)), "profit.")