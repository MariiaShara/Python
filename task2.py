time_in_sec=int(input("Enter time in seconds: "))
hours=time_in_sec // 3600
minutes=(time_in_sec % 3600)//60
seconds=(time_in_sec % 3600) % 60
print("Time is %.2d:%.2d:%.2d" %(hours,minutes,seconds))


