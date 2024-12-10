
# You are given the following information, but you may prefer to do some research for yourself.</p>
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
#  but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


import numpy as np



# New approach:

# I did some research and there is quite a simple pattern:
#The day of the week the first of the month falls on (for a given year) shifts one day down the days of the week next year,
#except on leap years, where this is a shift by 2 days
#determine the days of the week each month of 1900 fell on, then apply these shifts for each year forward
#the day of the week that was the first of the ith month is at the ith index
# (old approach commented below)


zero_year = ["monday","thursday","thursday","sunday","tuesday","friday","sunday","wednesday","saturday","monday","thursday","saturday"]


def first_of_month(start,end, zero_year):

    day = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    current_year = [None]*12
    previous_year = zero_year
    rule = 1
    leap_rule = 2
    years=[]

    for year in range(start,end+1):
        for i in range(0,12):
            
            #leap year logic
            if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) == True:
                for m in range(0,7):
                    try:
                        if previous_year[i] == day[m]:
                            current_year[i] = day[m+leap_rule]
                            break
                    except:
                        current_year[i] = day[1]

            #non-leap years
            else:
                for j in range(0,7):
                    try:
                        if previous_year[i] == day[j]:
                            current_year[i] = day[j+rule]
                            break
                    except:
                        current_year[i] = day[0]
        
        years.append(current_year[:])
        previous_year = current_year[:]


    return years



def sunday_sum(years):
    sundays = 0
    for year in years:
        for first_day in year:
            if first_day == "sunday":
                sundays += 1
    return sundays



#Weakness of program. In it's current form, start parameter can only be 1901, since zero_year is hard_coded.

#Currently get wrong answer, I didn't consider that 2000 is a leap year maybe?

print(sunday_sum(first_of_month(1901,2000,zero_year)))




# Old Approach:
#Make an array of length equal to the number of days from 1 Jan 1901 to 31 Dec 2000
#fill the array with the days of the week in order, until the array is full.

# create logic to determine the month based on the number of days that has passed
# Check day of the week when the month changes, by looking at the current value on the days array.

#A year has 365.25 days
# the number of days from 1 Jan 1901 to 31 Dec 2000 is therefore 36525 (365.25* 100)


# days_in_range = 1000

# day = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]


# #I'm having thoughts that this isn't necessary and we can just use our modulo 7 somewhere else to
# #extract the day for some day in the list
# days = [None]*days_in_range

# firsts = ["monday"]
# #print(days)

# #Check if first of month logic

# current_month = "january"
# counter = 1

# year = 1900
# leap_year = False

# for i in range(0, len(days)):
#     days[i] = day[i % 7]

#     if current_month == "january" and counter == 31:
#         current_month = "february"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "february" and counter == 28 and leap_year == False:
#         current_month = "march"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)


#     elif current_month == "march" and counter == 31:
#         current_month = "april"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "april" and counter == 30:
#         current_month = "may"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)


#     elif current_month == "may" and counter == 31:
#         current_month = "june"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "june" and counter == 30:
#         current_month = "july"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "july" and counter == 31:
#         current_month = "august"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "august" and counter == 31:
#         current_month = "september"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "september" and counter == 30:
#         current_month = "october"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "october" and counter == 31:
#         current_month = "november"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "november" and counter == 30:
#         current_month = "december"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#     elif current_month == "december" and counter == 31:
#         current_month = "january"
#         counter = 1
#         first_of_next_month_day = day[(i+1) % 7]
#         firsts.append(first_of_next_month_day)

#         year += 1

#     if i % 100 == 0:
#         pass
#         #print(i / 365)
    
#     if i % 365 == 0:
#         pass
#         #print("year",year)
#         #print(current_month)
    
#     counter += 1