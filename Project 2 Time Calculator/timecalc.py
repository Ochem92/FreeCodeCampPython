def add_time(start_time, add_time, day = None):
    lmeridian = ["AM","PM"]
    ldays = ["Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday","Sunday"]
    daystate=''
    maintime, start_meridian = start_time.split(" ")
    start_hour, start_min = maintime.split(":")
    new_hour, new_min = add_time.split(":")

    sum_min = int(start_min) + int(new_min)
    new_min = sum_min % 60
    if new_min < 10:
        new_min = str(new_min).zfill(2)

    total_hours = (int(start_hour) + int(new_hour) + (1 if int(sum_min) > 59 else 0))

    new_hour = (total_hours % 24) % 12
    if new_hour == 0:
        new_hour = 12

    day_switches = total_hours // 12
    print(day_switches)

    meridian_index = lmeridian.index(start_meridian)
    final_meridian = lmeridian[(meridian_index +(day_switches % 2 )) % 2 ]

    total_days = (day_switches + meridian_index) // 2
    print("total days:",total_days)

    if day == None:
        if day_switches == 0:
            new_time =  f"{new_hour}:{new_min} {final_meridian}"
        elif day_switches > (3-meridian_index):
            new_time = f"{new_hour}:{new_min} {final_meridian} ({total_days} days later)"
        elif day_switches > (1-meridian_index):
            new_time = f"{new_hour}:{new_min} {final_meridian} (next day)"
        else:
            new_time =  f"{new_hour}:{new_min} {final_meridian}"
    else:

        day_index = ldays.index(day.lower().capitalize())
        new_day_index = (day_index + total_days) % 7
        if day_switches == 0:
            new_time = f"{new_hour}:{new_min} {final_meridian}, {ldays[new_day_index]}"
        elif day_switches > (3 - meridian_index):
            new_time = f"{new_hour}:{new_min} {final_meridian}, {ldays[new_day_index]} ({total_days} days later)"
        elif day_switches > (1 - meridian_index):
            new_time = f"{new_hour}:{new_min} {final_meridian}, {ldays[new_day_index]} (next day)"
        else:
            new_time = f"{new_hour}:{new_min} {final_meridian}, {ldays[new_day_index]}"
    return new_time


