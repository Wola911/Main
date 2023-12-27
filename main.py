from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    
    print("START")
    print(users)

    users_new = {}
    users_dict = {}

    m_monday = []
    m_tuesday = []
    m_wednesday = []
    m_thursday = []
    m_friday = []

    if len(users) == 0:
        return users_new

    today = date.today()
    this_week = today.weekday()

    l_set = 5 - this_week
    l_sun = 6 - this_week
    end_next_week = l_sun + 5

    for m_list in users:

        m_name = m_list["name"]
        m_birthday = m_list["birthday"]

        m_date = today + timedelta(days=l_set)
        if m_birthday.month == m_date.month and m_birthday.day == m_date.day:
            # users_dict["Monday"].append(m_name)
            m_monday.append(m_name)
            continue

        m_date = today + timedelta(days=l_sun)
        if m_birthday.month == m_date.month and m_birthday.day == m_date.day:
            # users_dict["Monday"].append(m_name)
            m_monday.append(m_name)
            continue

        if m_birthday.month == (today + timedelta(days=(l_sun + 1))).month and m_birthday.day == (today + timedelta(days=(l_sun+1))).day:
            # users_dict["Monday"].append(m_name)
            m_monday.append(m_name)
        elif m_birthday.month == (today + timedelta(days=(l_sun + 2))).month and m_birthday.day == (today + timedelta(days=(l_sun+2))).day:
            # users_dict["Tuesday"].append(m_name)
            m_tuesday.append(m_name)
        elif m_birthday.month == (today + timedelta(days=(l_sun + 3))).month and m_birthday.day == (today + timedelta(days=(l_sun+3))).day:
            # users_dict["Wednesday"].append(m_name)
            m_wednesday.append(m_name)
        elif m_birthday.month == (today + timedelta(days=(l_sun + 4))).month and m_birthday.day == (today + timedelta(days=(l_sun+4))).day:
            # users_dict["Thursday"].append(m_name)
            m_thursday.append(m_name)
        elif m_birthday.month == (today + timedelta(days=(l_sun + 5))).month and m_birthday.day == (today + timedelta(days=(l_sun+5))).day:
            # users_dict["Friday"].append(m_name)
            m_friday.append(m_name)

    
    if len(m_monday) > 0:
       m_dict = {"Monday": m_monday}
       users_dict.update(m_dict) 

    if len(m_tuesday) > 0:
       m_dict = {"Tuesday": m_tuesday}
       users_dict.update(m_dict) 

    if len(m_wednesday) > 0:
       m_dict = {"Wednesday": m_wednesday}
       users_dict.update(m_dict) 

    if len(m_thursday) > 0:
       m_dict = {"Thursday": m_thursday}
       users_dict.update(m_dict) 

    if len(m_friday) > 0:
       m_dict = {"Friday": m_friday}
       users_dict.update(m_dict) 

    users = users_dict

    print(users_dict)
    print("FINISH")

    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
