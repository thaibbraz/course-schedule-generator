from rw_sheet import read_sheets, write_final_result
import pandas as pd
import holidays
from datetime import date
SPREADSHEET_ID = '12nqjSOKMlWhhbg6F6yRWVaKU00qq2nr-pCcxFmz4cGg'


where_to_write = "Sheet1!A1"
where_to_read = where_to_write
# data_result = read_sheets(where_to_read, SPREADSHEET_ID)
# print(data_result)

es_holidays = holidays.Spain()
holiday_names = holidays.country_holidays('ES', subdiv='CT')

full_stack_full_time = [
        {
        "Week": "Week 1",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Introduction, Variables, Operators, and Conditionals","Objects & Arrays","Loops & Looping through Objects","Looping through Arrays & Functions", "Milestone 1"]
    },{
        "Week": "Week 2",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Higher Order Functions & Closures","Classes, Testing, & File Structure","Queues and Stacks & Linked Lists", "Linked List & Recursion", "Milestone 2"]
    },{
        "Week": "Week 3",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Trees","Graphs","Manipulating the DOM","Manipulating the DOM (continued)", "Milestone 3"]
    },{
        "Week": "Week 4",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Vue","Vue (continued)","React","React (continued)", "Milestone 4"]
    },{
        "Week": "Week 5",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Fetch","APIs","Databases", "Databases (continued)", "Milestone 5"]
    },{
        "Week": "Week 6",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["MVP Solo Project","MVP Solo Project","MVP Solo Project", "MVP Solo Project","MVP Solo Project"]
    },{
        "Week": "Week 7",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["MVP Solo Project","MVP Solo Project","Feature Extension Project", "Feature Extension Project","Feature Extension Project"]
    },{
        "Week": "Week 8",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Feature Extension Project","Feature Extension Project","Feature Extension Project Presentation", "Collaborative Project","Collaborative Project"]
    },{
        "Week": "Week 9",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Collaborative Project","Collaborative Project","Collaborative Project", "Collaborative Project","Collaborative Project"]
    },{
        "Week": "Week 10",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Collaborative Project","Collaborative Project","Collaborative Project", "Collaborative Project","Collaborative Project"]
    },{
        "Week": "Week 11",
        "week_day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        "date": [],
        "sentence": [],
        "class_title": ["Collaborative Project Presentation & Career Week","Career Week","Career Week", "Career Week","Graduation"]
    },

]

# start_date = input("What's the date the course will start? FORMAT: '2/24/2020' ")
# end_date = input("What's the date the course will end? FORMAT: '2/24/2020' ")

# if start_date == end_date:
#     print("The course will be on the same day")
# else:


#Filter Holidays
holidays_list = []
for item in pd.bdate_range(start="4/18/2022", end="12/19/2022",freq='B'):
    if holiday_names.get(item.strftime("%m/%d/%Y")) != None:        
        holidays_list.append(item.strftime("%A %B %d")+" HOLIDAY")
    else:
        holidays_list.append(item.strftime("%A %B %d"))
        # full_stack_full_time[i]["date"].append(pd.bdate_range(start=start_date, end=end_date, freq='B')[counter_date].strftime("%A %B %d"))
print(holidays_list)
# pd.bdate_range(start=start_date, end=end_date, freq='B')
counter_date = 0
for i in range(len(full_stack_full_time)):
    for j in range(len(full_stack_full_time[i]["week_day"])):
        full_stack_full_time[i]["date"].append(holidays_list[counter_date])
        
        counter_date += 1
                

counter = 1

# Check if there's already something written in the sheet
while read_sheets(where_to_read,SPREADSHEET_ID) != []:
        counter += 1
        where_to_read = "Sheet1!A{counter}".format(counter=counter)             
        where_to_write = where_to_read 

for i in range(len(full_stack_full_time)):
    for j in range(len(full_stack_full_time[i]["week_day"])):
        full_stack_full_time[i]["sentence"].append(full_stack_full_time[i]["date"][j] +": "+ full_stack_full_time[i]["class_title"][j])

# print(full_stack_full_time[0])
for item in full_stack_full_time:
    write_final_result([[item["Week"]]], "Sheet1!A{counter}".format(counter=counter), SPREADSHEET_ID)
    counter += 1
    for j in range(len(item["week_day"])):
        counter += 1
        write_final_result([[item["sentence"][j]]], "Sheet1!A{counter}".format(counter=counter), SPREADSHEET_ID)
    counter += 2
    write_final_result([["\n"]], "Sheet1!A{counter}".format(counter=counter), SPREADSHEET_ID)


