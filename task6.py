goods = []
n = 1
while input("Would you like to add a product? Enter yes/no: ") == 'yes':
    product_info = {"name": input("Enter " + str(n) + " product's name: "),
                    "price": int(input("Enter " + str(n) + " product's price: ")),
                    "quantity": int(input("Enter " + str(n) + " product's quantity: ")),
                    "measurement": input("Enter " + str(n) + " product's units of measurement: ")}
    goods.append((n, product_info))
    n += 1
print(goods)
analytics = {}
for i in goods:
    for k, v in i[1].items():
        if k in analytics:
            analytics[k].append(v)
        else:
            analytics[k] = [v]
print(analytics)

