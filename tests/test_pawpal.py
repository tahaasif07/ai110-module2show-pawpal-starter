
from pawpal_system import Owner, Pet, Task, Scheduler


#Test 1: Task completion
def test_task_completion():
    task = Task("Feed Milo", "2026-10-19", "09:00", 15, "High")

    task.mark_complete()

    assert task.completed == True


#Test 2: Sorting tasks
def test_sorting():
    owner = Owner("Alex")
    pet = Pet("Milo", "Cat")
    owner.add_pet(pet)

    task1 = Task("Feed Milo", "2026-10-19", "09:00", 15, "High")
    task2 = Task("Brush Milo", "2026-10-19", "08:00", 10, "Low")

    pet.add_task(task1)
    pet.add_task(task2)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0].description == "Brush Milo"
    assert sorted_tasks[1].description == "Feed Milo"


#Test 3: Recurring tasks
def test_daily_recurrence():
    owner = Owner("Alex")
    pet = Pet("Milo", "Cat")
    owner.add_pet(pet)

    task = Task(
        "Feed Milo", "2026-10-19", "09:00",
        15, "High", frequency="daily"
    )

    pet.add_task(task)
    scheduler = Scheduler(owner)

    new_task = scheduler.complete_task(pet, task)

    assert task.completed == True
    assert new_task.due_date == "2026-10-20"
    assert new_task.completed == False
    assert new_task in pet.tasks


#Test 4: Scheduling conflicts
def test_conflicts():
    owner = Owner("Alex")
    pet1 = Pet("Milo", "Cat")
    pet2 = Pet("Buddy", "Dog")

    owner.add_pet(pet1)
    owner.add_pet(pet2)

    pet1.add_task(Task("Brush Milo", "2026-10-19", "08:00", 10, "Low"))
    pet2.add_task(Task("Walk Buddy", "2026-10-19", "08:00", 30, "Medium"))

    scheduler = Scheduler(owner)

    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
