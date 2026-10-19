
#This imports our classes from pawpal_system.py
from pawpal_system import Owner, Pet, Task, Scheduler


#This creates an owner
owner = Owner("Alex")

#This creates two pets
pet1 = Pet("Milo", "Cat")
pet2 = Pet("Buddy", "Dog")

#This add pets to the owner
owner.add_pet(pet1)
owner.add_pet(pet2)


#this creates tasks for the pets
task1 = Task("Feed Milo", "2026-10-19", "09:00", 15, "High", frequency="daily")
task2 = Task("Walk Buddy", "2026-10-19", "08:00", 30, "Medium")
task3 = Task("Give Milo medicine", "2026-10-19", "10:00", 5, "High")
task4 = Task("Brush Milo", "2026-10-19", "08:00", 10, "Low")

#Add this task to Milo
pet1.add_task(task4)



#This adds tasks to the correct pets
pet1.add_task(task1)
pet1.add_task(task3)
pet2.add_task(task2)


#This creates our scheduler
scheduler = Scheduler(owner)


#This displays the owner's pets
print("=== PAWPAL+ PETS ===")

for pet in owner.list_pets():
    print(pet.name, "-", pet.animal_type)


#This displays every scheduled task
print("\n=== ALL SCHEDULED TASKS ===")

for task in scheduler.get_all_tasks():
    print(task.due_time, "-", task.description, "| Priority:", task.priority)


#This marks a task as completed
new_task = scheduler.complete_task(pet1, task1)
print("\n=== TASK COMPLETION ===")
print(task1.description, "- Completed:", task1.completed)


#Sisplays tasks in chronological order
print("\n=== SORTED TASKS ===")

for task in scheduler.sort_by_time():
    print(task.due_time, "-", task.description)

#Shows only Milo's tasks
print("\n=== MILO'S TASKS ===")

for task in scheduler.filter_tasks(pet_name="Milo"):
    print(task.description)


#Shows only incomplete tasks
print("\n=== INCOMPLETE TASKS ===")

for task in scheduler.filter_tasks(completed=False):
    print(task.description)


#Shows the next repeating task
print("\n=== RECURRING TASK ===")

if new_task is not None:
    print("New task:", new_task.description)
    print("Next date:", new_task.due_date)
    print("Completed:", new_task.completed)


#Checks for scheduling conflicts
print("\n=== TASK CONFLICTS ===")

conflicts = scheduler.detect_conflicts()

if len(conflicts) == 0:
    print("No scheduling conflicts found.")
else:
    for task1, task2 in conflicts:
        print("WARNING: Scheduling conflict!")
        print(task1.description, "and", task2.description)
        print("Both scheduled at:", task1.due_time)
