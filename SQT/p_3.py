def is_leap_year(year): 
    if (year % 4 == 0): 
        if (year % 100 == 0): 
            if (year % 400 == 0): 
                return True 
            else: 
                return False 
        else: 
            return True 
    else: 
        return False 

def day_of_week(day, month, year): 
    # Zeller's Congruence Algorithm 
    if month < 3: 
        month += 12 
        year -= 1 
    k = year % 100 
    j = year // 100 
    f = day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j) 
    return f % 7 

def main(): 
    year = 2024 
    if is_leap_year(year): 
        print(f"{year} is a leap year.") 
    else: 
        print(f"{year} is not a leap year.") 
    
    day = 29 
    month = 2 
    weekday = day_of_week(day, month, year) 
    print(f"The day of the week for {day}/{month}/{year} is {weekday}.") 

main()
