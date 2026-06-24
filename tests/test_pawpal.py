from pawpal_system import CareTask, Pet


def test_mark_complete_changes_task_status():
    task = CareTask(
        task_name="Morning walk",
        category="exercise",
        duration_minutes=30,
        priority="high",
    )

    task.mark_complete()

    assert task.is_completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet(name="Mochi", species="dog")
    task = CareTask(
        task_name="Breakfast",
        category="feeding",
        duration_minutes=10,
        priority="high",
    )

    pet.add_task(task)

    assert len(pet.tasks) == 1