from rw_sheet import read_sheets, write_final_result
import pandas as pd
import holidays
from datetime import date
import time
SPREADSHEET_ID = '12nqjSOKMlWhhbg6F6yRWVaKU00qq2nr-pCcxFmz4cGg'
from arrayGenerator import get_full_stack_part_time,get_full_stack_full_time,get_product_management

where_to_write = "Sheet1!A1"
where_to_read = where_to_write


es_holidays = holidays.Spain()
holiday_names = holidays.country_holidays('ES', subdiv='CT')



start_date = input("What's the date the course will start? FORMAT: '2/24/2020' ")
end_date = input("What's the date the course will end? FORMAT: '2/24/2020' ")

cohort = input("What's the cohort?  FORMAT: 'FSPT', 'FSFT' OR 'PM' ")
if cohort == "FSPT":
    cohort_list = get_full_stack_part_time()
elif cohort == "FSFT":
    cohort_list = get_full_stack_full_time()
elif cohort == "PM":
    cohort_list = get_product_management()

#Filter Holidays
holidays_list = []
if cohort == "FSPT":
     dates_list = pd.bdate_range(start=start_date, end=end_date,freq='C',weekmask='Mon Thu')
elif cohort == "FSFT":
     dates_list = pd.bdate_range(start=start_date, end=end_date,freq='B')
elif cohort == "PM":
    dates_list = pd.bdate_range(start=start_date, end=end_date,freq='C',weekmask='Tue Thu')
for item in dates_list:
    if holiday_names.get(item.strftime("%m/%d/%Y")) != None:        
        holidays_list.append(item.strftime("%A %B %d")+" HOLIDAY")
    else:
        holidays_list.append(item.strftime("%A %B %d"))
        # full_stack_full_time[i]["date"].append(pd.bdate_range(start=start_date, end=end_date, freq='B')[counter_date].strftime("%A %B %d"))

# pd.bdate_range(start=start_date, end=end_date, freq='B')
counter_date = 0
full_stack_full_time = get_full_stack_full_time()
for i in range(len(cohort_list)):
    for j in range(len(cohort_list[i]["week_day"])):
        cohort_list[i]["date"].append(holidays_list[counter_date])  
        
        counter_date += 1
                

counter = 1

# Check if there's already something written in the sheet
while read_sheets(where_to_read,SPREADSHEET_ID) != []:
        counter += 1
        where_to_read = "Sheet1!A{counter}".format(counter=counter)             
        where_to_write = where_to_read 

for i in range(len(cohort_list)):
    for j in range(len(cohort_list[i]["week_day"])):
        cohort_list[i]["sentence"].append(cohort_list[i]["date"][j] +": "+ cohort_list[i]["class_title"][j])


for item in cohort_list:
    write_final_result([[item["Week"]]], "Sheet1!A{counter}".format(counter=counter), SPREADSHEET_ID)
    counter += 1
    time.sleep(2.4)
    for j in range(len(item["week_day"])):
        counter += 1
        write_final_result([[item["sentence"][j]]], "Sheet1!A{counter}".format(counter=counter), SPREADSHEET_ID)
    counter += 2
    write_final_result([["\n"]], "Sheet1!A{counter}".format(counter=counter), SPREADSHEET_ID)


