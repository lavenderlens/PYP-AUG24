id = 1234#or as string - immutable
first_name = "John"
last_name = "Doe"
checked_bags = False
visited_countries = ["Latvia", "Guyana", "Yemen", "Uzbekistan", "Latvia"]#or as set {} - unique values only
visited_countries_set = {"Latvia", "Guyana", "Yemen", "Uzbekistan", "Latvia"}#or as set {} - unique values only
flight = "LGW to CDG"#or as dict - more meaningful
flight_dict = {"departure": "LGW","arrival": "CDG"}
flight_time = 1.25

print(f'id: {id}, {type(id)}')
print(f'first_name: {first_name}, {type(first_name)}')
print(f'last_name: {last_name}, {type(last_name)}')
print(f'checked_bags: {checked_bags}, {type(checked_bags)}')
print(f'flight: {flight}, {type(flight)}')
print(f'flight_time: {flight_time}, {type(flight_time)}')

print(type(visited_countries))
print(visited_countries)#ordered, duplicate values permitted
print(type(visited_countries_set))
print(visited_countries_set)#unordered, unique values only

if checked_bags:
    print("Proceed to checkin to drop your bags")
