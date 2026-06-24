# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Running `python main.py` prints:

```text
Tasks Sorted By Time
--------------------
1. 07:30 - Luna: Medication (15 min, priority: high, frequency: daily, done)
2. 08:00 - Mochi: Morning walk (30 min, priority: high, frequency: daily, not done)
3. 09:00 - Mochi: Breakfast (10 min, priority: high, frequency: daily, done)
4. 09:00 - Mochi: Breakfast (10 min, priority: high, frequency: daily, not done)
5. 10:00 - Mochi: Evening enrichment (25 min, priority: medium, frequency: daily, not done)
6. 10:00 - Luna: Brush fur (20 min, priority: medium, frequency: daily, not done)

Mochi's Tasks
-------------
1. 10:00 - Mochi: Evening enrichment (25 min, priority: medium, frequency: daily, not done)
2. 09:00 - Mochi: Breakfast (10 min, priority: high, frequency: daily, done)
3. 08:00 - Mochi: Morning walk (30 min, priority: high, frequency: daily, not done)
4. 09:00 - Mochi: Breakfast (10 min, priority: high, frequency: daily, not done)

Incomplete Tasks
----------------
1. 10:00 - Mochi: Evening enrichment (25 min, priority: medium, frequency: daily, not done)
2. 08:00 - Mochi: Morning walk (30 min, priority: high, frequency: daily, not done)
3. 09:00 - Mochi: Breakfast (10 min, priority: high, frequency: daily, not done)
4. 10:00 - Luna: Brush fur (20 min, priority: medium, frequency: daily, not done)

Conflict Warnings
-----------------
- Conflict at 10:00: Mochi: Evening enrichment, Luna: Brush fur

Recurring Task Created
----------------------
Breakfast was recreated for 2026-06-24.

Today's Schedule
================
Owner: Jordan
Available time: 75 minutes

Scheduled Tasks:
1. Mochi - Breakfast (10 min, priority: high, frequency: daily)
2. Mochi - Morning walk (30 min, priority: high, frequency: daily)
3. Luna - Brush fur (20 min, priority: medium, frequency: daily)

Unscheduled Tasks:
- Mochi - Evening enrichment (25 min, priority: medium)
- Mochi - Breakfast (10 min, priority: high)
- Luna - Medication (15 min, priority: high)

Reasoning:
Scheduled 3 task(s) using 60 minute(s). 15 minute(s) remain. Tasks were prioritized by completion status, priority, and shorter duration. 3 task(s) were not scheduled because they were completed or did not fit.
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `Scheduler.sort_by_time()` and `Scheduler.sort_tasks_by_priority()` | Sorts tasks by preferred time for timeline views and by priority/duration for daily planning. |
| Filtering | `Scheduler.filter_tasks_by_pet()` and `Scheduler.filter_tasks_by_completion()` | Lets the system show tasks for one pet or separate completed and incomplete tasks. |
| Conflict handling | `Scheduler.detect_conflicts()` | Returns warning messages when two incomplete tasks share the same preferred time. |
| Recurring tasks | `CareTask.create_next_occurrence()` and `Scheduler.mark_task_complete()` | When a recurring daily or weekly task is completed, the next task is created using `timedelta`. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
