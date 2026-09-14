import sys
import json , os
from datetime import datetime

#creat command and arguments
command = sys.argv[1]
arguments = sys.argv[2:]


# create json file
if not os.path.exists("tasks.json"):
    with open("tasks.json" , 'w') as filename:
        json.dump([] , filename)


with open("tasks.json" , 'r') as filename:
    task = json.load(filename)

# creating add task
if command.lower() == 'add':

    if not task:
        unique_id = 1
    else:
        unique_id = task[-1]["Id"]+1

    new_task = {
        "Id" : unique_id,
        "Description" : " ".join(arguments),
        "Status" : 'ToDo',
        "CreateAt" : str(datetime.now().strftime("%d-%m-%Y %H:%M")),
        "UpdateAt" : str(datetime.now().strftime("%d-%m-%Y %H:%M"))
    }

    task.append(new_task)
    with open("tasks.json"  , 'w') as filename:
        json.dump(task , filename , indent = 4)



#create list
with open("tasks.json", 'r') as filename:
        task_list = json.load(filename)

if command.lower() == "list":
    if not arguments:
        for curr_task in task_list:
            print("Task ", curr_task["Id"] , " : ", curr_task["Description"] , "--" , curr_task["Status"])
    else:
        status = arguments[0].lower()
        for curr_task in task_list:
            if curr_task["Status"].lower() == status:
                print("Task ", curr_task["Id"] , " : ", curr_task["Description"], "-- " ,curr_task["Status"])

#create task
if command.lower() == 'update':

    if not arguments :
        print("Error..")
        print("Try again later..")
    else :
        for sub_task in task_list:
            if sub_task["Id"] == int(arguments[0]):
                sub_task["Status"] = arguments[1]
                sub_task["UpdateAt"] = datetime.now().strftime("%d-%m-%Y %H:%M")

with open("tasks.json" , 'w') as filename:
    json.dump(task_list , filename , indent=4)

#delete task 
if command.lower() == 'delete':
    for sub_task in task_list:
        if sub_task["Id"] == int(arguments[0]):
            task_list.remove(sub_task)
            break

with open("tasks.json" , 'r') as filename:
    json.dump(task_list , filename , indent = 4)


