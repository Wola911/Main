from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    
    week_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday"}
    names_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
    users_dict = {}

    if len(users) == 0:
        return users_dict

    today = date.today()

    for i in range(0, 7):

        m_date = today + timedelta(days=i) 
        m_weekday = m_date.weekday()
        
        for user in users:

            m_name = user["name"]
            m_birthday = user["birthday"]
            
            if m_birthday.month == m_date.month and m_birthday.day == m_date.day:
                if m_weekday == 5 or m_weekday == 6:
                    names_dict[0].append(m_name)
                else:
                    names_dict[m_weekday].append(m_name)

        if not(m_weekday == 5 or m_weekday == 6) and len(names_dict[m_weekday]) > 0:
            new_dict = {week_dict[m_weekday]:names_dict[m_weekday]}
            users_dict.update(new_dict)

    users = users_dict

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
