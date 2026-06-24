from pawpal_system import CareTask, Owner, Pet, Scheduler


def print_schedule(owner: Owner, scheduler: Scheduler) -> None:
    scheduled_tasks = scheduler.generate_daily_plan()

    print("Today's Schedule")
    print("================")
    print(f"Owner: {owner.name}")
    print(f"Available time: {scheduler.get_available_time()} minutes")
    print()

    print("Scheduled Tasks:")
    if scheduled_tasks:
        for number, (pet, task) in enumerate(scheduled_tasks, start=1):
            print(
                f"{number}. {pet.name} - {task.task_name} "
                f"({task.duration_minutes} min, priority: {task.priority}, "
                f"frequency: {task.frequency})"
            )
    else:
        print("No tasks scheduled.")

    if scheduler.unscheduled_tasks:
        print()
        print("Unscheduled Tasks:")
        for pet, task in scheduler.unscheduled_tasks:
            print(
                f"- {pet.name} - {task.task_name} "
                f"({task.duration_minutes} min, priority: {task.priority})"
            )

    print()
    print("Reasoning:")
    print(scheduler.explain_plan())


def main() -> None:
    owner = Owner(
        name="Jordan",
        available_time_minutes=75,
        preferred_start_time="08:00",
        preferences="Prioritize medication and walks before grooming.",
    )

    dog = Pet(name="Mochi", species="dog", breed="Golden Retriever", age=3)
    cat = Pet(name="Luna", species="cat", breed="Tabby", age=5)

    dog.add_task(
        CareTask(
            task_name="Morning walk",
            category="exercise",
            duration_minutes=30,
            priority="high",
            preferred_time="08:00",
        )
    )
    dog.add_task(
        CareTask(
            task_name="Breakfast",
            category="feeding",
            duration_minutes=10,
            priority="high",
            preferred_time="09:00",
        )
    )
    cat.add_task(
        CareTask(
            task_name="Medication",
            category="health",
            duration_minutes=15,
            priority="high",
            preferred_time="09:30",
        )
    )
    cat.add_task(
        CareTask(
            task_name="Brush fur",
            category="grooming",
            duration_minutes=20,
            priority="medium",
            preferred_time="10:00",
        )
    )

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    print_schedule(owner, scheduler)


if __name__ == "__main__":
    main()
