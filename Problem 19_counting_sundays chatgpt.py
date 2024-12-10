#AI suggestion

#It looks when I shift the day it goes wrong, 
#but when I test my code it works for the first 4 years or so,
#I never saw the error.


zero_year = ["monday", "thursday", "thursday", "sunday", "tuesday", "friday", "sunday", 
             "wednesday", "saturday", "monday", "thursday", "saturday"]

def first_of_month(start_year, end_year, initial_year_days):
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    current_year_days = [None] * 12
    previous_year_days = initial_year_days[:]
    day_shift_non_leap = 1  # Shift for non-leap years
    day_shift_leap = 2  # Shift for leap years
    all_years_days = []

    for year in range(start_year, end_year + 1):
        for month_index in range(12):
            previous_day_index = weekdays.index(previous_year_days[month_index])
            
            # Check for leap year
            if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                current_day_index = (previous_day_index + day_shift_leap) % 7
            else:
                current_day_index = (previous_day_index + day_shift_non_leap) % 7
            
            current_year_days[month_index] = weekdays[current_day_index]
        
        # Store the computed days for the current year
        all_years_days.append(current_year_days[:])
        previous_year_days = current_year_days[:]
    
    return all_years_days

def count_sundays_on_first(all_years_days):
    sunday_count = 0
    for year_days in all_years_days:
        sunday_count += year_days.count("sunday")
    return sunday_count

# Calculate the number of months starting on a Sunday
result = count_sundays_on_first(first_of_month(1901, 2000, zero_year))
print(result)  # Should output the correct answer, 171
