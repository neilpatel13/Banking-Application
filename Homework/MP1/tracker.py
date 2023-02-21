from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    """
    task["lastActivity"] = datetime.strptime(due, '%m/%d/%y %H:%M:%S') # update lastActivity with the current datetime value
    task['name'] = name # set the name, description, and due date (all must be provided)
    task['description'] = description # due date must match one of the formats mentioned in str_to_datetime()
    task['due'] = due() # add the new task to the tasks list
    """
    task["lastActivity"] = datetime.strptime(due, '%m/%d/%y %H:%M:%S') # update lastActivity with the current datetime value
    if name and description and due:
        task['name'] = name
        task['description'] = description
        
        # due date must match one of the formats mentioned in str_to_datetime()
        due_date = str_to_datetime(due)
        if due_date:
            task['due'] = due_date.strptime(due,'%m/%d/%y %H:%M:%S')
        else:
            print("Invalid due date format. Please use mm/dd/yy hh:mm:ss")
            return
    else:
        print("Name, description, and due date must be provided.")
        return
    tasks.append(task)
    print("New Task was made")# output a message confirming the new task was added or if the addition was rejected due to missing data
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    save()
    """UCID: np656 (2/19) the solution for this task was adding the name, description, and due date
    as in a dict key value pair using task[key] = value"""

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    #for i in range(len(tasks)):
    #   pass 
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index >= len(tasks) or index < 0:
        print("Invalid index. Please select a valid index.")
        return
    task = tasks[index]
    name = input(f"What's the name of this task? ({task['name']}) \n").strip()
    desc = input(f"What's a brief descriptions of this task? ({task['description']}) \n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) ({task['due']}) \n").strip()
    update_task(index, name=name, description=desc, due=due)
    """UCID: np656 (2/20) the solution for this task was first checking the index of the tasks to make sure user is 
    selecting the right one, after it was just processing the name, desc, and due by changing TODO to the task with 
    index of that variable."""

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    """
    task = TASK_TEMPLATE.copy()
    task["lastActivity"] = datetime 
    task['name'] = name 
    task['description'] = description
    task['due'] = due() 
    """
    # find the task by index
    if index >= len(tasks) or index < 0:
        print("Invalid index. Please select a valid index.")
        return    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    task = tasks[index]
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    task_name = name if name else task['name']
    task_desc = description if description else task['description']
    task_due = str_to_datetime(due) if due else str_to_datetime(task['due'])
    # update lastActivity with the current datetime value
    task['lastActivity'] = datetime.strptime(due, '%m/%d/%y %H:%M:%S')
    # update the task only if any items were changed
    if task_name != task['name'] or task_desc != task['description'] or task_due != str_to_datetime(task['due']):
        task['name'] = task_name
        task['description'] = task_desc
        task['due'] = task_due
        print("Task updated successfully.")
    else:
        print("No changes were made to the task.")
    # save the updated tasks list to the fil
    save()
    """UCID: np656 (2/20) the solution for this task was first checking the index of the tasks to make sure user is 
    selecting the right one, after it was just checking the task in the specified index was there using the if else task[paramater]
    then it was just updating the name, desc, and due by setting the new input to the same fields of the task."""

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index >= len(tasks) or index < 0:     # find task from list by index
        print("Invalid index. Please select a valid index.")
        return     # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    task = tasks[index]
    
    # if it's not done, record the current datetime as the value
    if not task['done']:
        task['done'] = datetime.now()
        print("Task marked as completed.")
    # if it is done, print a message saying it's already completed
    else:
        print("This task is already completed.")
    # make sure save() is still called last in this function
    save()
    """UCID: np656 (2/20) the solution for this task was first checking the index of the tasks to make sure user is 
    selecting the right one, after it checking if the task was either not done or already done, for not done, I used
    the datetime.now in the done index of task to mark it done, it made it set true, and for already done, just printing a message saying its done already"""

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    if index < 0 or index >= len(tasks):
        print("Invalid index. Please enter a valid index within the range of available tasks.")
        return    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    task = tasks[index]
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #task = {}
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
"""UCID: np656 (2/20) the solution for this task was first checking the index of the tasks to make sure user is 
    selecting the right one, after it was just using the printing function given."""

def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    # Check if the index is valid
    if index < 0 or index >= len(tasks):
        print("Invalid index. Task not deleted.")
        return
    # Remove the task from the list
    del tasks[index]
    print(f"Task at index {index} has been deleted.")
    # Save the updated task list
    save()
"""UCID: np656 (2/20) the solution for this task was first checking the index of the tasks to make sure user is 
    selecting the right one, after it was just using the del function to delete the task at the specified index and
    printing a message or completed deletion."""

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    _tasks = [t for t in tasks if not t['done']]
    if _tasks:
        list_tasks(_tasks)
    else:
        print("No incomplete tasks.")
    """UCID: np656 (2/20) the solution for this task was by appending all the task not in done to a seperate list
    and printing the list out"""

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    over_due = datetime.now()
    _tasks = [t for t in tasks if not t['done'] and str_to_datetime(t['due']) < over_due]
    if _tasks:
        print("Overdue tasks:")
        list_tasks(_tasks)
    else:
        print("No overdue tasks to show.")
"""UCID: np656 (2/20) the solution for this task was first comparing all task that were less than over_due
variable and seeing if it was not in done, and then appending it to a seperate list and printing it out"""

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    if index < 0 or index >= len(tasks):    # get the task by index
        print("Invalid index.")     # consider index out of bounds scenarios and include appropriate message(s) for invalid index
        return
    task = tasks[index]
# get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due 
    # (clearly note that it's over due, values should be positive)
    # get the time remaining
    now = datetime.now()
    due_date = datetime.strptime(task['due'], "%Y-%m-%d %H:%M:%S")
    time_remain = due_date - now
    # display the time remaining
    if time_remain.total_seconds() <= 0:
        time_overdue = -time_remain
        print(f"Task is {time_overdue.days} days, {time_overdue.seconds // 3600} hours, {(time_overdue.seconds // 60) % 60} minutes, and {time_overdue.seconds % 60} seconds overdue.")
    else:
        print(f"Task has {time_remain.days} days, {time_remain.seconds // 3600} hours, {(time_remain.seconds // 60) % 60} minutes, and {time_remain.seconds % 60} seconds remaining.")
    #task = {}
"""UCID: np656 (2/20) the solution for this task using the datetime.strptime to get the due date and subtract it
from datetime.now to get the time remaining, and then in the printing function, printing out each value of datetime."""
# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()