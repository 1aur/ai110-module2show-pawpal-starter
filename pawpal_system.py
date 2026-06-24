from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Optional


@dataclass
class CareTask:
    """Represents one pet care activity."""

    task_name: str
    category: str
    duration_minutes: int
    priority: str
    preferred_time: str = ""
    frequency: str = "daily"
    due_date: Optional[date] = None
    is_completed: bool = False
    is_recurring: bool = False
    notes: str = ""

    def update_task(self, name: str, duration: int, priority: str) -> None:
        """Update the task name, duration, and priority."""
        self.task_name = name
        self.duration_minutes = duration
        self.priority = priority

    def get_priority_value(self) -> int:
        """Convert the task priority into a sortable number."""
        priority_values = {
            "high": 3,
            "medium": 2,
            "low": 1,
        }
        return priority_values.get(self.priority.lower(), 0)

    def get_task_info(self) -> dict:
        """Return the task details as a dictionary."""
        return {
            "task_name": self.task_name,
            "category": self.category,
            "duration_minutes": self.duration_minutes,
            "priority": self.priority,
            "preferred_time": self.preferred_time,
            "frequency": self.frequency,
            "due_date": self.due_date.isoformat() if self.due_date else "",
            "is_completed": self.is_completed,
            "is_recurring": self.is_recurring,
            "notes": self.notes,
        }

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.is_completed = True

    def mark_incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.is_completed = False

    def create_next_occurrence(self) -> Optional["CareTask"]:
        """Create the next recurring task based on the current frequency."""
        if not self.is_recurring:
            return None

        current_due_date = self.due_date or date.today()

        if self.frequency.lower() == "daily":
            next_due_date = current_due_date + timedelta(days=1)
        elif self.frequency.lower() == "weekly":
            next_due_date = current_due_date + timedelta(weeks=1)
        else:
            return None

        return CareTask(
            task_name=self.task_name,
            category=self.category,
            duration_minutes=self.duration_minutes,
            priority=self.priority,
            preferred_time=self.preferred_time,
            frequency=self.frequency,
            due_date=next_due_date,
            is_completed=False,
            is_recurring=self.is_recurring,
            notes=self.notes,
        )


@dataclass
class Pet:
    """Stores pet details and the pet's care tasks."""

    name: str
    species: str
    breed: str = ""
    age: int = 0
    special_needs: str = ""
    tasks: list[CareTask] = field(default_factory=list)

    def add_task(self, task: CareTask) -> None:
        """Add a care task to the pet."""
        self.tasks.append(task)

    def remove_task(self, task_name: str) -> None:
        """Remove a care task from the pet by name."""
        self.tasks = [
            task for task in self.tasks
            if task.task_name.lower() != task_name.lower()
        ]

    def get_tasks(self) -> list[CareTask]:
        """Return all tasks assigned to the pet."""
        return self.tasks

    def get_pet_info(self) -> dict:
        """Return the pet details as a dictionary."""
        return {
            "name": self.name,
            "species": self.species,
            "breed": self.breed,
            "age": self.age,
            "special_needs": self.special_needs,
            "tasks": [task.get_task_info() for task in self.tasks],
        }


@dataclass
class Owner:
    """Manages one owner, their pets, and access to all pet tasks."""

    name: str
    available_time_minutes: int
    preferred_start_time: str = "08:00"
    preferences: str = ""
    pets: list[Pet] = field(default_factory=list)

    def update_available_time(self, minutes: int) -> None:
        """Update the owner's available care time."""
        self.available_time_minutes = minutes

    def update_preferences(self, preferences: str) -> None:
        """Update the owner's care preferences."""
        self.preferences = preferences

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def remove_pet(self, pet_name: str) -> None:
        """Remove a pet from the owner by name."""
        self.pets = [
            pet for pet in self.pets
            if pet.name.lower() != pet_name.lower()
        ]

    def get_all_tasks(self) -> list[CareTask]:
        """Return all tasks across all of the owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks

    def get_all_task_items(self) -> list[tuple[Pet, CareTask]]:
        """Return pet-task pairs for every task across all pets."""
        task_items = []
        for pet in self.pets:
            for task in pet.get_tasks():
                task_items.append((pet, task))
        return task_items

    def get_owner_info(self) -> dict:
        """Return the owner details as a dictionary."""
        return {
            "name": self.name,
            "available_time_minutes": self.available_time_minutes,
            "preferred_start_time": self.preferred_start_time,
            "preferences": self.preferences,
            "pets": [pet.get_pet_info() for pet in self.pets],
        }


@dataclass
class Scheduler:
    """Retrieves, organizes, and schedules tasks across an owner's pets."""

    owner: Owner
    available_time_minutes: Optional[int] = None
    scheduled_tasks: list[tuple[Pet, CareTask]] = field(default_factory=list)
    unscheduled_tasks: list[tuple[Pet, CareTask]] = field(default_factory=list)

    def get_available_time(self) -> int:
        """Return the scheduler's available time limit."""
        if self.available_time_minutes is not None:
            return self.available_time_minutes
        return self.owner.available_time_minutes

    def get_all_tasks(self) -> list[CareTask]:
        """Return all tasks from the owner's pets."""
        return self.owner.get_all_tasks()

    def sort_tasks_by_priority(self) -> list[CareTask]:
        """Sort tasks by completion status, priority, and duration."""
        return sorted(
            self.get_all_tasks(),
            key=lambda task: (task.is_completed, -task.get_priority_value(), task.duration_minutes),
        )

    def sort_by_time(self) -> list[tuple[Pet, CareTask]]:
        """Sort pet-task pairs by preferred time in HH:MM format."""
        return sorted(
            self.owner.get_all_task_items(),
            key=lambda item: item[1].preferred_time or "23:59",
        )

    def filter_tasks_by_pet(self, pet_name: str) -> list[tuple[Pet, CareTask]]:
        """Return pet-task pairs for one pet name."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_task_items()
            if pet.name.lower() == pet_name.lower()
        ]

    def filter_tasks_by_completion(self, is_completed: bool) -> list[tuple[Pet, CareTask]]:
        """Return pet-task pairs matching a completion status."""
        return [
            (pet, task)
            for pet, task in self.owner.get_all_task_items()
            if task.is_completed == is_completed
        ]

    def mark_task_complete(self, pet_name: str, task_name: str) -> Optional[CareTask]:
        """Mark a task complete and add its next occurrence if recurring."""
        for pet, task in self.owner.get_all_task_items():
            if pet.name.lower() == pet_name.lower() and task.task_name.lower() == task_name.lower():
                task.mark_complete()
                next_task = task.create_next_occurrence()
                if next_task:
                    pet.add_task(next_task)
                return next_task

        return None

    def detect_conflicts(self) -> list[str]:
        """Return warnings for tasks that share the same preferred time."""
        tasks_by_time: dict[str, list[tuple[Pet, CareTask]]] = {}

        for pet, task in self.owner.get_all_task_items():
            if task.is_completed or not task.preferred_time:
                continue
            tasks_by_time.setdefault(task.preferred_time, []).append((pet, task))

        warnings = []
        for preferred_time, task_items in tasks_by_time.items():
            if len(task_items) > 1:
                task_names = [
                    f"{pet.name}: {task.task_name}"
                    for pet, task in task_items
                ]
                warnings.append(
                    f"Conflict at {preferred_time}: " + ", ".join(task_names)
                )

        return warnings

    def can_fit_task(self, task: CareTask) -> bool:
        """Check whether a task fits in the remaining schedule time."""
        time_used = sum(
            scheduled_task.duration_minutes
            for _, scheduled_task in self.scheduled_tasks
        )
        remaining_time = self.get_available_time() - time_used
        return task.duration_minutes <= remaining_time

    def generate_daily_plan(self) -> list[tuple[Pet, CareTask]]:
        """Build a daily plan from available pet tasks."""
        self.scheduled_tasks = []
        self.unscheduled_tasks = []

        task_items = sorted(
            self.owner.get_all_task_items(),
            key=lambda item: (
                item[1].is_completed,
                -item[1].get_priority_value(),
                item[1].duration_minutes,
            ),
        )

        for pet, task in task_items:
            if task.is_completed:
                self.unscheduled_tasks.append((pet, task))
            elif self.can_fit_task(task):
                self.scheduled_tasks.append((pet, task))
            else:
                self.unscheduled_tasks.append((pet, task))

        return self.scheduled_tasks

    def explain_plan(self) -> str:
        """Return a short explanation of the generated plan."""
        if not self.scheduled_tasks:
            return "No tasks were scheduled. Add tasks or increase the available time."

        total_time = sum(task.duration_minutes for _, task in self.scheduled_tasks)
        remaining_time = self.get_available_time() - total_time
        explanation_lines = [
            f"Scheduled {len(self.scheduled_tasks)} task(s) using {total_time} minute(s).",
            f"{remaining_time} minute(s) remain.",
            "Tasks were prioritized by completion status, priority, and shorter duration.",
        ]

        if self.unscheduled_tasks:
            explanation_lines.append(
                f"{len(self.unscheduled_tasks)} task(s) were not scheduled because they were completed or did not fit."
            )

        return " ".join(explanation_lines)
