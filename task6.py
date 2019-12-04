distance=int(input("Enter the distance you ran in the first day in km: "))
target_distance=int(input("Enter the target distance in km: "))
day=1
while(distance<=target_distance):
    distance=1.1*distance
    day=day+1
print(f"You will run your target distance on the {day} day.")