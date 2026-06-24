from dataclasses import dataclass, field


@dataclass
class CareTask:
    task_name: str
    category: str
    duration_minutes: int
    priority: str
    preferred_time: str = ""
    is_recurring: bool = False
    notes: str = ""

    def update_task(self, name: str, duration: int, priority: str) -> None:
        pass

    def get_priority_value(self) -> int:
        pass

    def get_task_info(self) -> dict:
        pass


@dataclass
class Pet:
    name: str
    species: str
    breed: str = ""
    age: int = 0
    special_needs: str = ""
    tasks: list[CareTask] = field(default_factory=list)

    def add_task(self, task: CareTask) -> None:
        pass

    def remove_task(self, task_name: str) -> None:
        pass

    def get_tasks(self) -> list[CareTask]:
        pass

    def get_pet_info(self) -> dict:
        pass


@dataclass
class Owner:
    name: str
    available_time_minutes: int
    preferred_start_time: str = "08:00"
    preferences: str = ""
    pets: list[Pet] = field(default_factory=list)

    def update_available_time(self, minutes: int) -> None:
        pass

    def update_preferences(self, preferences: str) -> None:
        pass

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_owner_info(self) -> dict:
        pass


@dataclass
class Scheduler:
    tasks: list[CareTask]
    available_time_minutes: int
    scheduled_tasks: list[CareTask] = field(default_factory=list)
    unscheduled_tasks: list[CareTask] = field(default_factory=list)

    def sort_tasks_by_priority(self) -> list[CareTask]:
        pass

    def can_fit_task(self, task: CareTask) -> bool:
        pass

    def generate_daily_plan(self) -> list[CareTask]:
        pass

    def explain_plan(self) -> str:
        pass
