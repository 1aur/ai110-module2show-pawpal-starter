# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.

My initial design for PawPal+ focused on the main actions a busy pet owner would need in order to plan daily pet care. 
1. The user should be able to enter basic owner and pet information so the app knows who the plan is for. 
2. The user should be able to add and manage pet care tasks, such as walks, feeding, medication, grooming, and enrichment, with details like duration and priority. 
3. The user should be able to generate a daily care plan that fits within the time available and prioritizes the most important tasks.

The main classes I planned to include were an `Owner` class, a `Pet` class, a `CareTask` class, and a `Scheduler` class. 
- `Owner` class would store basic user information and preferences. 
- `Pet` class would store details about the pet. 
- `CareTask` class would represent each care activity, including its name, duration, and priority.
- `Scheduler` class would be responsible for choosing and organizing tasks into a daily plan based on constraints like time and priority.

- What classes did you include, and what responsibilities did you assign to each?

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

The main relationships were mostly represented: an `Owner` can have multiple `Pet` objects, and each `Pet` can have multiple `CareTask` objects. One possible improvement is that the `Scheduler` currently only receives a list of tasks and available time, instead of directly connecting to an `Owner` or `Pet`. This keeps the scheduler simple, but it may make it harder later to explain which pet the schedule belongs to.

I also noticed a few possible logic bottlenecks. Priority is stored as a string, so the scheduler will need a method like `get_priority_value()` to convert priorities into sortable values. Time is also stored as strings, which is simple for now but may need to be converted later if I build more detailed time slots. I decided not to add a separate `DailyPlan` class yet because the current project can still work with the four main classes, but I may add one later if the schedule output becomes more complex.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that conflict detection only checks for exact preferred-time matches, such as two tasks both starting at `10:00`. It does not yet calculate whether tasks overlap based on duration, such as one task running from `10:00` to `10:30` and another starting at `10:15`. I kept the conflict detection lightweight because this version of PawPal+ is focused on a simple daily planning workflow, and exact-time warnings are easier to understand and verify in the terminal. This approach is reasonable for the project because it catches obvious scheduling issues without making the algorithm too complex too early.

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
