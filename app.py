import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

#This stores the owner and scheduler in session memory
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(st.session_state.owner)


#This adds an owner name
st.subheader("Owner Information")

owner_name = st.text_input("Owner name", value=st.session_state.owner.name)

if st.button("Update Owner"):
    st.session_state.owner.name = owner_name
    st.success("Owner updated!")


#Adds pets
st.subheader("Add a Pet")

pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])

if st.button("Add Pet"):
    if pet_name:
        new_pet = Pet(pet_name, species)
        st.session_state.owner.add_pet(new_pet)
        st.success("Pet added!")
    else:
        st.warning("Please enter a pet name.")


#This displays pets
st.subheader("Your Pets")

if st.session_state.owner.pets:
    for pet in st.session_state.owner.pets:
        st.write(pet.name, "-", pet.animal_type)
else:
    st.info("No pets added yet.")


#This adds tasks
st.subheader("Schedule a Task")

if st.session_state.owner.pets:

    #This chooses which pet gets the task
    pet_names = [pet.name for pet in st.session_state.owner.pets]
    selected_pet = st.selectbox("Choose a pet", pet_names)

    task_title = st.text_input("Task description")
    due_date = st.date_input("Task date")
    due_time = st.time_input("Task time")
    duration = st.number_input("Duration (minutes)", min_value=1, value=15)
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    frequency = st.selectbox("Repeat", ["none", "daily", "weekly"])

    if st.button("Add Task"):

        if task_title:

            #Creates a Task object
            new_task = Task(
                task_title,
                str(due_date),
                due_time.strftime("%H:%M"),
                int(duration),
                priority,
                frequency=frequency
            )

            #Finds the selected pet and add its task
            for pet in st.session_state.owner.pets:
                if pet.name == selected_pet:
                    pet.add_task(new_task)
                    break

            st.success("Task added!")

        else:
            st.warning("Please enter a task description.")

else:
    st.info("Add a pet before scheduling tasks.")



#Displays and filter tasks
st.subheader("Daily Schedule")

scheduler = st.session_state.scheduler

#Chooses which tasks to display
filter_option = st.selectbox(
    "Filter tasks",
    ["All Tasks", "Incomplete", "Completed"]
)

#Gets tasks based on the selected filter
if filter_option == "Incomplete":
    tasks = scheduler.filter_tasks(completed=False)

elif filter_option == "Completed":
    tasks = scheduler.filter_tasks(completed=True)

else:
    tasks = scheduler.get_all_tasks()

#Sorts the selected tasks by date and time
tasks = sorted(
    tasks,
    key=lambda task: (task.due_date, task.due_time)
)

#Displays tasks
if tasks:
    for task in tasks:
        status = "Completed" if task.completed else "Incomplete"

        st.write(
            task.due_date,
            task.due_time,
            "-",
            task.description,
            "| Priority:",
            task.priority,
            "| Status:",
            status
        )
else:
    st.info("No tasks found.")


#Shows scheduling conflicts
st.subheader("Scheduling Conflicts")

conflicts = scheduler.detect_conflicts()

if conflicts:
    for task1, task2 in conflicts:
        st.warning(
            "Conflict: " + task1.description +
            " and " + task2.description +
            " are both scheduled at " + task1.due_time
        )
else:
    st.success("No scheduling conflicts found!")

