from datetime import datetime, timedelta

from dataclasses import dataclass, field

#Task class: stores information about a pet's task
@dataclass
class Task:
    description: str
    due_date: str
    due_time: str
    duration: int
    priority: str
    completed: bool = False
    frequency: str = "none"

    #Marks a task as completed
    
    #Completes a task and create the next one if repeating
    def mark_complete(self):
        self.completed = True

        #Checks if the task repeats
        if self.frequency == "daily":
            days = 1
        elif self.frequency == "weekly":
            days = 7
        else:
            return None

        #Converts the text date into a Python date
        current_date = datetime.strptime(self.due_date, "%Y-%m-%d")

        #Adds days to calculate the next date
        next_date = current_date + timedelta(days=days)

        #Creates a new task for the next date
        new_task = Task(
            self.description,
            next_date.strftime("%Y-%m-%d"),
            self.due_time,
            self.duration,
            self.priority,
            False,
            self.frequency
        )

        return new_task



#Pet class: stores information about a pet
@dataclass
class Pet:
    name: str
    animal_type: str
    tasks: list = field(default_factory=list)

    
    #Adds a task to the pet's task list
    def add_task(self, task):
        self.tasks.append(task)

    #Returns all tasks belonging to the pet
    def list_tasks(self):
        return self.tasks



#Owner class: stores pets belonging to an owner
@dataclass
class Owner:
    name: str
    pets: list = field(default_factory=list)

   
    #Adds a pet to the owner's list
    def add_pet(self, pet):
        self.pets.append(pet)

    #Returns all pets belonging to the owner
    def list_pets(self):
        return self.pets




#Scheduler class: organizes tasks for all pets
class Scheduler:

    #Connects the scheduler to the owner
    def __init__(self, owner):
        self.owner = owner

    #Gets tasks from every pet
    def get_all_tasks(self):
        all_tasks = []

        for pet in self.owner.pets:
            for task in pet.tasks:
                all_tasks.append(task)

        return all_tasks

    #Sorts tasks by date and time
    
    #Sorts tasks by date and time
    def sort_by_time(self):
        """Return all tasks sorted by date and time."""

        tasks = self.get_all_tasks()

        sorted_tasks = sorted(
            tasks,
            key=lambda task: (task.due_date, task.due_time)
        )

        return sorted_tasks


    
    #Filters tasks by pet name or completion status
    def filter_tasks(self, pet_name=None, completed=None):
        filtered_tasks = []

        # Goes through each pet
        for pet in self.owner.pets:

            #Skips pets that don't match the name
            if pet_name is not None and pet.name != pet_name:
                continue

            #Goes through this pet's tasks
            for task in pet.tasks:

                #Skips tasks with a different completion status
                if completed is not None and task.completed != completed:
                    continue

                #Adds matching tasks to the list
                filtered_tasks.append(task)

        return filtered_tasks
    
    #Completes a task and save its next occurrence
    def complete_task(self, pet, task):
        new_task = task.mark_complete()

        #Adds the repeating task to the same pet
        if new_task is not None:
            pet.add_task(new_task)

        return new_task




    #Finds tasks scheduled at the same date and time
    def detect_conflicts(self):
        conflicts = []

        #Gets all tasks from all pets
        tasks = self.get_all_tasks()

        #Compares each task with the other tasks
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):

                task1 = tasks[i]
                task2 = tasks[j]

                #Checks if both tasks are incomplete
                if not task1.completed and not task2.completed:

                    #Checks if date and time are the same
                    if task1.due_date == task2.due_date:
                        if task1.due_time == task2.due_time:
                            conflicts.append((task1, task2))

        return conflicts
