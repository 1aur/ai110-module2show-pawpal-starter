import streamlit as st
from pawpal_system import CareTask, Owner, Pet, Scheduler


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")


if "owner" not in st.session_state:
    st.session_state["owner"] = Owner(
        name="",
        available_time_minutes=60,
        preferred_start_time="08:00",
        preferences=""
    )

owner = st.session_state["owner"]


st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+.

Use this app to add pets, create care tasks, and generate a daily pet care schedule.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.
"""
    )

st.divider()

st.subheader("Owner Information")

owner_name = st.text_input("Owner name", value=owner.name)
available_time = st.number_input(
    "Available care time today (minutes)",
    min_value=1,
    max_value=480,
    value=owner.available_time_minutes,
)
preferred_start_time = st.text_input(
    "Preferred start time",
    value=owner.preferred_start_time,
)
preferences = st.text_input("Care preferences", value=owner.preferences)

owner.name = owner_name
owner.available_time_minutes = int(available_time)
owner.preferred_start_time = preferred_start_time
owner.preferences = preferences

st.divider()

st.subheader("Pets")

pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    if pet_name.strip():
        new_pet = Pet(name=pet_name, species=species)
        owner.add_pet(new_pet)
        st.success(f"Added {pet_name}.")
    else:
        st.warning("Please enter a pet name.")

if owner.pets:
    st.write("Current pets:")
    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species})")
else:
    st.info("No pets yet. Add one above.")

st.divider()

st.subheader("Tasks")

if owner.pets:
    pet_options = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Choose pet for this task", pet_options)

    selected_pet = next(
        pet for pet in owner.pets
        if pet.name == selected_pet_name
    )

    col1, col2 = st.columns(2)

    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
        category = st.selectbox(
            "Category",
            ["walk", "feeding", "meds", "grooming", "enrichment", "other"],
        )

    with col2:
        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            max_value=240,
            value=20,
        )
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    preferred_time = st.text_input("Preferred time", value="08:00")

    if st.button("Add task"):
        new_task = CareTask(
            task_name=task_title,
            category=category,
            duration_minutes=int(duration),
            priority=priority,
            preferred_time=preferred_time,
        )

        selected_pet.add_task(new_task)
        st.success(f"Added {task_title} for {selected_pet.name}.")

    st.write("Current tasks:")
    task_rows = []

    for pet in owner.pets:
        for task in pet.tasks:
            task_rows.append(
                {
                    "Pet": pet.name,
                    "Task": task.task_name,
                    "Category": task.category,
                    "Duration": task.duration_minutes,
                    "Priority": task.priority,
                    "Preferred Time": task.preferred_time,
                    "Completed": task.is_completed,
                }
            )

    if task_rows:
        st.table(task_rows)
    else:
        st.info("No tasks yet. Add one above.")
else:
    st.info("Add a pet before adding tasks.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner)
    scheduled_tasks = scheduler.generate_daily_plan()

    st.markdown("### Today's Schedule")

    if scheduled_tasks:
        for pet, task in scheduled_tasks:
            st.write(
                f"{pet.name}: {task.task_name} "
                f"({task.duration_minutes} min, priority: {task.priority})"
            )

        st.info(scheduler.explain_plan())
    else:
        st.warning("No tasks were scheduled.")