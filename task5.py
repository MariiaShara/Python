revenue=int(input("Enter the firm's revenue: "))
costs=int(input("Enter the firm's costs: "))
result=revenue-costs
if result > 0:
    print(f"The firm's profit is: {result}")
    print("The firm's profit margin is: %.2f" %(result/revenue))
    employees=int(input("Enter the number of employees: "))
    profit_per_employees=result/employees
    print(f"Profits per employee: %.2f" %(result/employees))
elif result < 0:
    print(f"The firm's loss is: {-result}")
else:
    print("The firm's revenue equals costs")