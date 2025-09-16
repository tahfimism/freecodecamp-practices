def add_time(start, duration, start_day = None):

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    s_hr, gg = start.strip().split(":")
    s_min, s_zone = gg.split(" ")

    d_hr, d_min = duration.strip().split(":")

    s_hr, s_min, d_hr, d_min = int(s_hr), int(s_min), int(d_hr), int(d_min)

    # changed to 24 hour format
    if s_zone == "AM" and s_hr == 12:
        s_hr = 0
    elif s_zone == "PM" and s_hr != 12:
        s_hr += 12

    # new minute
    n_min = s_min + d_min
    extra_hr = n_min // 60
    n_min = n_min % 60

    # new hour
    n_hr = s_hr + d_hr + extra_hr
    extra_day = n_hr // 24
    n_hr = n_hr % 24



    #change back to 12 hour format
    if n_hr == 0:
        n_hr = 12
        n_zone = "AM"
    elif n_hr < 12:
        n_zone = "AM"
    elif n_hr == 12:
        n_zone = "PM"
    else:  # n_hr > 12
        n_hr -= 12
        n_zone = "PM"



    if start_day == None:
        if extra_day == 0:
            new_time = f"{n_hr}:{n_min:02d} {n_zone}"
        elif extra_day == 1:
            new_time = f"{n_hr}:{n_min:02d} {n_zone} (next day)"
        else:
            new_time = f"{n_hr}:{n_min:02d} {n_zone} ({extra_day} days later)"
        
    else:
        if extra_day == 0:
            new_time = f"{n_hr}:{n_min:02d} {n_zone}, {start_day}"


        else:
            new_day = days.index(start_day.title()) + extra_day
            new_day = days[new_day % 7]

            if extra_day == 1:
                new_time = f"{n_hr}:{n_min:02d} {n_zone}, {new_day} (next day)"
            else:
                new_time = f"{n_hr}:{n_min:02d} {n_zone}, {new_day} ({extra_day} days later)"
        
    

    



    return new_time