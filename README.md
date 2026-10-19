# PawPal+ (Module 2 Project)

## Project Overview

PawPal+ is a pet care management app made with Python and Streamlit. It helps pet owners keep track of daily tasks like feeding, walking, giving medicine, and grooming.

The app allows users to add pets, schedule tasks, organize their schedules, and check for conflicts.

## Features

- Add an owner and multiple pets.
- Schedule tasks for different pets.
- Give tasks a date, time, duration, and priority.
- Mark tasks as completed using Python.
- Sort tasks by date and time.
- Filter tasks by pet name or completion status.
- Automatically create new daily or weekly tasks.
- Detect scheduling conflicts between different pets.
- View scheduled tasks through a Streamlit website.

## Python Classes

**Owner:** Stores the owner's name and list of pets.

**Pet:** Stores information about a pet and its tasks.

**Task:** Stores task descriptions, dates, times, durations, priorities, completion status, and frequency.

**Scheduler:** Organizes tasks from multiple pets and handles sorting, filtering, recurring tasks, and conflict detection.

## Getting Started

### Setup

Create and activate your virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the Python Demo

```bash
python main.py
```

### Run the Streamlit Website

```bash
python -m streamlit run app.py
```

Open the local URL that Streamlit displays in your terminal.

## Smarter Scheduling

PawPal+ uses four main scheduling features.

| Feature | Method | Description |
|---|---|---|
| Sorting | `Scheduler.sort_by_time()` | Sorts tasks by date and time. |
| Filtering | `Scheduler.filter_tasks()` | Filters tasks by pet name or completion status. |
| Recurring Tasks | `Task.mark_complete()` and `Scheduler.complete_task()` | Creates another task for the next day or week. |
| Conflict Detection | `Scheduler.detect_conflicts()` | Finds incomplete tasks scheduled at the same date and time. |

### Scheduling Tradeoff

The scheduler checks for conflicts when two incomplete tasks have the exact same date and time. It does not check whether task durations overlap. I kept this simple because it is easier to understand and works for basic scheduling.

The system stores task priorities, but tasks are currently sorted by date and time rather than priority.

## Sample CLI Output

This is an example of the output from running `python main.py`:

```text
=== PAWPAL+ PETS ===
Milo - Cat
Buddy - Dog

=== ALL SCHEDULED TASKS ===
08:00 - Brush Milo | Priority: Low
09:00 - Feed Milo | Priority: High
10:00 - Give Milo medicine | Priority: High
08:00 - Walk Buddy | Priority: Medium

=== TASK COMPLETION ===
Feed Milo - Completed: True

=== SORTED TASKS ===
08:00 - Brush Milo
08:00 - Walk Buddy
09:00 - Feed Milo
10:00 - Give Milo medicine
09:00 - Feed Milo

=== MILO'S TASKS ===
Brush Milo
Feed Milo
Give Milo medicine
Feed Milo

=== INCOMPLETE TASKS ===
Brush Milo
Give Milo medicine
Feed Milo
Walk Buddy

=== RECURRING TASK ===
New task: Feed Milo
Next date: 2026-10-20
Completed: False

=== TASK CONFLICTS ===
WARNING: Scheduling conflict!
Brush Milo and Walk Buddy
Both scheduled at: 08:00
```

## Testing PawPal+

I used pytest to test the main features of PawPal+.

The tests check:

- Task completion
- Correct sorting of tasks
- Daily recurring tasks
- Scheduling conflicts between pets

### Run the Tests

```bash
python -m pytest -v
```

### Test Results

```text
tests/test_pawpal.py::test_task_completion PASSED
tests/test_pawpal.py::test_sorting PASSED
tests/test_pawpal.py::test_daily_recurrence PASSED
tests/test_pawpal.py::test_conflicts PASSED

4 passed in 0.02s
```

### Confidence Level

**4 out of 5 stars**

All four tests passed successfully. I am confident that the main scheduling functions work correctly. More tests could be added for empty task lists, weekly recurring tasks, and overlapping durations.

## Demo Walkthrough

1. Run the Streamlit app using `python -m streamlit run app.py`.
2. Enter an owner's name and click Update Owner.
3. Add pets by entering their names and animal types.
4. Schedule tasks by selecting a pet and entering a description, date, time, duration, priority, and frequency.
5. View scheduled tasks organized by date and time.
6. If two incomplete tasks have the same date and time, the app displays a conflict warning.

For example, users can add Milo the cat and Buddy the dog. If Milo's grooming task and Buddy's walking task are both scheduled for 8:00 AM on the same day, the system identifies the conflict.

The Python CLI demo also demonstrates completing tasks, filtering tasks, and automatically creating recurring tasks.

## UML Diagram

PawPal+ uses four main classes:

- Owner
- Pet
- Task
- Scheduler

The initial UML diagram is saved in `diagrams/uml_draft.mmd`.

The final UML diagram is saved in `diagrams/uml_final.mmd`. It includes the four main classes, their attributes, methods, and relationships.
## AI Collaboration

I used ChatGPT to help brainstorm my design, create the UML diagram, understand Python classes, and implement scheduling methods.

AI also helped me debug indentation errors and understand error messages. I reviewed the code and tested it using the terminal and pytest.

I decided to keep the scheduling algorithms simple so I could understand how they worked.

## Future Improvements

In the future, I would like to add:

- Priority-based scheduling
- Detection of overlapping task durations
- Task editing and completion buttons in Streamlit
- Notifications for upcoming tasks
- Saving data between application sessions

These improvements would make PawPal+ more useful for pet owners.