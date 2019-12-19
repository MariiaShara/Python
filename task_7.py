import json

results = []
profits = []
firms_dict = {}
profit_dict = {}

try:
    with open("for_task_7.txt", "r", encoding="utf-8") as f:
        for line in f:
            firm, type_of_bussiness, revenue, costs = line.split()
            result = int(revenue) - int(costs)
            results.append(result)
            firms_dict[firm] = result
except IOError:
    print("Input Output Error")
except ValueError:
    print("В файле содержатся неправильные данные.")

for el in results:
    if el >= 0:
        profits.append(el)
try:
    average_profit = round(sum(profits) / len(profits))
except ZeroDivisionError:
    average_profit = None
    print("Все фирмы получили убытки.")

profit_dict["average_profit"] = average_profit
result_list = [firms_dict, profit_dict]

with open("task_7.json", "w", encoding="utf-8") as f:
    json.dump(result_list, f)
