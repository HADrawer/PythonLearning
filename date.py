from datetime import date

world_cup_2022 = date(2022,11,21)
print(world_cup_2022)

today = date.today()
print(today)

some_day = date.fromordinal(738480)
print(some_day)

another_day = date.fromisoformat('2022-11-21')
print(another_day)

days_from_WorldCup = world_cup_2022 - today
print(days_from_WorldCup)

print(type(days_from_WorldCup))

print(today > world_cup_2022)

print(world_cup_2022.isoformat())
