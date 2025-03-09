from datetime import datetime

date_string = "2021-03-08"


def get_days_from_today(date_string):
    day_now = datetime.today() #get the currrent day
    date_object = datetime.strptime(date_string, "%Y-%m-%d") #convert the selected day into the datetime object
    time_difference = day_now - date_object #calculating the differense between the selected days, as output days and hours, minutes
    return time_difference.days #only days difference returns

print(get_days_from_today(date_string))


 
