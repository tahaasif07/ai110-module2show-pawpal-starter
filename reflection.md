# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

-**Three core actions:**

1. Users can add pets by entering their names and animal types.
2. Users can schedule tasks for their pets, such as feeding, walking, or giving medicine.
3. Users can view their pets' daily tasks, see which tasks are most important, and mark tasks as completed.

**Classes and their responsibilities:**

1. **Owner:** Stores the owner's name and a list of their pets. The owner can add pets and view them.
2. **Pet:** Stores the pet's name, animal type, and scheduled tasks. Each pet can have multiple tasks.
3. **Task:** Stores information about a task, such as its description, date, time, priority, and whether it is completed.
4. **Scheduler:** Organizes tasks for all pets. It can sort tasks by time, filter tasks, and find scheduling conflicts.

I chose these four classes because they each have their own job. This makes the program easier to understand and update.

**b. Design changes**

During the design process, I added duration and priority to the Task class. Duration basically tells the system how long a task takes, and priority helps identify which tasks are more important. I made this change because it would help the scheduler organize tasks better while keeping the code simple.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

My scheduler consider things such as the date, time, completion status, and pet name when organizing tasks. Each task also has a priority level. I focused on sorting tasks items such as date and time because it's a simple way to help pet owners see what needs to be done first. The priority status is displayed but does not change the sorting order.

**b. Tradeoffs**

One tradeoff I made was checking for scheduling conflicts only when two incomplete tasks have the exact same date and time. My scheduler does not check whether tasks overlap based on their duration. I chose this approach because it is easier to understand and works for basic pet scheduling. In the future, this is something I could improve in order to detect overlapping tasks.

---

## 3. AI Collaboration

**a. How you used AI**

I used ChatGPT throughout my project to help plan my classes, create my UML diagram, and write Python code. I also used it to help me with things such as sorting, filtering, recurring tasks, and conflict detection. The most helpful prompts were when I asked AI to explain things in beginner-friendly terms and help me fix errors. This made it easier for me to understand what each part of the code was doing.

**b. Judgment and verification**

One AI suggestion I decided to keep rather simple was conflict detection. Instead of checking if task durations overlap, I used a simpler method that checks if two tasks have the exact same date and time. I chose this because I could understand the logic better. I verified that it worked by running my program and scheduling two tasks at 8:00 AM. The system successfully displayed a conflict warning. I also used terminal errors to fix problems with indentation and returning values.

---

## 4. Testing and Verification

**a. What you tested**

I used pytest to test four main parts of my program. I tested whether a task could be marked as completed, whether tasks were sorted by time correctly, whether daily recurring tasks created a new task for the next day, and whether the scheduler could detect conflicts between two pets. These tests were important because they helped me make sure the main features were working correctly.

**b. Confidence**

I would give my scheduler a confidence level of 4 out of 5 stars. All four of my pytest tests passed, which made me more confident in my program. If I had more time, I would test weekly recurring tasks, pets with no tasks, and tasks that overlap because of their duration. I would also test more situations where multiple pets have tasks on the same day.

---

## 5. Reflection

**a. What went well**

The part of this project I am most satisfied with is getting the scheduling system to work. I was able to use Python classes to organize pets and tasks. I also got items such as sorting, filtering, recurring tasks, and conflict detection working. It was very cool seeing the program work in the terminal and then connecting it to the Streamlit website.

**b. What you would improve**

If I had another chance to improve my project, I would make the scheduler consider items such as task durations and priorities more. Right now, my program sorts tasks by date and time and checks for conflicts at the exact same time. I would also improve the website by adding more options to edit tasks and make the design look better.

**c. Key takeaway**

One important thing I learned is that planning a program before coding makes it much easier to build. Creating the UML diagram helped me understand how my classes connect. I also learned that AI can help with coding and debugging, but I still need to understand the code and test it myself to make sure it works.