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

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
