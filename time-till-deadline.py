from datetime import datetime
from time import time

user_input = input("Enter your goal with a deadline seperated by colon\n")

input_list = user_input.split(":")

# split puts items in list that can be accessed by index

goal = input_list[0]

deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds()/60/60)
# calculation how many dates from now till the deadline


print(f"Dear use! Time remaining for your goal:{goal} is {hours_till} days")
