#Author: Lzj
#mail: harry_lee2683@outlook.com
rent = 3000

def cost():
    utilities = int(input('请输入本月的水电费用'))
    food_cost = int(input('请输入本月的食材费用'))
    global variable_cost
    variable_cost = utilities + food_cost
    print('本月的变动成本费用是' + str(variable_cost))

def sum_cost():
    sum = rent + variable_cost
    print('本月的总成本是' + str(sum))

cost()
sum_cost()
def egg():
    global quantity
    quantity = 108

egg()
print(quantity)