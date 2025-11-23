import redis
import time
import matplotlib.pyplot as plt

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def show_schedule():
    try:
        keys = r.keys("task:*")
        if not keys:
            print("⚠️ No tasks in Redis.")
            return

        tasks = []
        for key in keys:
            task = r.hgetall(key)
            try:
                tasks.append({
                    'id': key.split(":")[1],
                    'name': task.get('name', 'Unknown'),
                    'priority': int(task.get('priority', 0)),
                    'total_time': int(task.get('total_time', 0))
                })
            except ValueError:
                continue

        # Sort by highest priority ↓, then by least total_time ↑
        tasks.sort(key=lambda x: (-x['priority'], x['total_time']))

        print("\n🚀 Scheduling tasks by Priority ↓ and Total Time ↑...\n")

        # Gantt Chart data collection
        start_time = 0
        gantt_data = []

        for t in tasks:
            print(f"▶️ Executing {t['name']} (Priority {t['priority']}, Time {t['total_time']}s)")
            time.sleep(0.05)  # simulate execution
            finish_time = start_time + t['total_time']
            gantt_data.append({
                "Task": t['name'],
                "Start": start_time,
                "Finish": finish_time
            })
            start_time = finish_time
            print(f"✅ Finished {t['name']}\n")

        # Generate Gantt Chart
        create_gantt_chart(gantt_data)

    except Exception as e:
        print(f"❌ Error showing schedule: {e}")


def create_gantt_chart(data, page_size=20):
    try:
        total_tasks = len(data)
        pages = (total_tasks + page_size - 1) // page_size  # ceil division

        # Reverse order so earliest task is on top
        data = list(reversed(data))

        for page in range(pages):
            start_idx = page * page_size
            end_idx = min(start_idx + page_size, total_tasks)
            page_data = data[start_idx:end_idx]

            fig_height = max(6, len(page_data) * 0.5)
            fig, ax = plt.subplots(figsize=(14, fig_height))

            # Use distinct colors
            colors = plt.cm.tab20.colors * ((len(page_data) // 20) + 1)

            for i, task in enumerate(page_data):
                ax.barh(
                    y=i,
                    width=task["Finish"] - task["Start"],
                    left=task["Start"],
                    height=0.6,
                    color=colors[i],
                    edgecolor="black"
                )
                ax.text(
                    task["Start"] + (task["Finish"] - task["Start"]) / 2,
                    i,
                    task["Task"],
                    ha="center",
                    va="center",
                    color="white",
                    fontsize=10,
                    fontweight="bold"
                )

            # Y-axis labels
            ax.set_yticks(range(len(page_data)))
            ax.set_yticklabels([task["Task"] for task in page_data], fontsize=10)
            ax.invert_yaxis()

            # X-axis & title
            ax.set_xlabel("Time (s)", fontsize=12)
            ax.set_title(f"🕓 Task Execution Timeline (Gantt Chart) — Page {page+1}/{pages}", fontsize=14, pad=15)
            ax.grid(True, axis="x", linestyle="--", alpha=0.6)

            plt.subplots_adjust(left=0.25, right=0.95, top=0.95, bottom=0.1)
            plt.tight_layout()
            plt.show()

            if page < pages - 1:
                cont = input("Show next 20 tasks? (y/n): ").strip().lower()
                if cont != 'y':
                    break

    except Exception as e:
        print(f"❌ Error creating Gantt chart: {e}")




def add_task():
    try:
        task_id = input("Enter task ID: ").strip()
        name = input("Enter task name: ").strip()
        priority = int(input("Enter task priority (1–10): ").strip())
        total_time = int(input("Enter total time (1–60): ").strip())

        key = f"task:{task_id}"
        r.hset(key, mapping={
            "name": name,
            "priority": priority,
            "total_time": total_time
        })
        print(f"✅ Task {task_id} added successfully!")

    except Exception as e:
        print(f"❌ Error adding task: {e}")


def delete_task():
    try:
        task_id = input("Enter task ID to delete: ").strip()
        key = f"task:{task_id}"
        if r.exists(key):
            r.delete(key)
            print(f"🗑️ Task {task_id} deleted successfully!")
        else:
            print("⚠️ Task not found.")
    except Exception as e:
        print(f"❌ Error deleting task: {e}")


def menu():
    while True:
        print("\n==== Task Scheduler Menu ====")
        print("1. Show Schedule ")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            show_schedule()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("👋 Exiting Scheduler...")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
