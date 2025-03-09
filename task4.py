from datetime import datetime, timedelta
users = [
    {"name": "John Doe", "birthday": "1985.03.16"},
    {"name": "Jane Smith", "birthday": "1990.03.12"},
    {"name": "Nataliia Dubikova", "birthday": "1999.03.11" },
    {"name": "Stanislav Fomenko", "birthday": "1994.04.11"}
]

upcomming_birthdays = []
current_day = datetime.today().date() #today's date

def get_upcoming_birthdays(users):
    iterations = len(users)
    for item in range (0, iterations):
        datetime_obj = datetime.strptime(users[item]["birthday"], "%Y.%m.%d").date() #convert the string to the daytime object
        birthday_this_year = datetime_obj.replace(year = current_day.year) #change the year of the birthday
        

        #If the birthday passed in this year, move the congrat day to the next year
        if birthday_this_year < current_day:
            birthday_this_year = birthday_this_year.replace(year= current_day.year +1)
            
        
        #Check if birthay in a 7 day range 

        if (birthday_this_year - current_day).days <= 7 and (birthday_this_year - current_day).days >= 0:
            congratulation_date = birthday_this_year
            

            #Check if the day it's a weekend, move it on monday
            if congratulation_date.weekday() in(5, 6):
                congratulation_date += timedelta(days=(7 - congratulation_date.weekday()))
                
            upcomming_birthdays.append({
                "name": users[item]["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")   
            })

    return upcomming_birthdays



print(get_upcoming_birthdays(users))








