from datetime import time

time1 =time()

print(time1.hour)
print(time1.minute)
print(time1.second)

time2 = time(hour=15, minute=29, second=20)
print(time2)


print(time2.hour)
print(time2.minute)
print(time2.second)


time3 = time.fromisoformat('18:44:50')
print(time3)