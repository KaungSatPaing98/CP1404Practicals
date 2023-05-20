from project import Project


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            fields = line.strip().split("\t")
            name, start_date, priority, cost_estimate, completion_percentage = fields
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion_percentage = int(completion_percentage)
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def save_projects(projects, filename):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(str(project) + "\n")


def display_projects(projects):
    incomplete_projects = sorted([project for project in projects if project.completion_percentage < 100],
                                 key=lambda x: x.priority)
    completed_projects = sorted([project for project in projects if project.completion_percentage == 100],
                                key=lambda x: x.priority)
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(project)
    print("\nCompleted Projects:")
    for project in completed_projects:
        print(project)


def filter_projects_by_date(projects, date):
    filtered_projects = sorted([project for project in projects if project.start_date > date],
                               key=lambda x: x.start_date)
    print("Filtered Projects:")
    for project in filtered_projects:
        print(project)


def add_project(projects):
    name = input("Enter project name: ")
    start_date = input("Enter start date (dd/mm/yyyy): ")
    priority = int(input("Enter priority (1-10): "))
    cost_estimate = float(input("Enter cost estimate: "))
    completion_percentage = int(input("Enter completion percentage (0-100): "))
    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print("Project added successfully.")


def update_project(projects):
    name = input("Enter project name to update: ")
    project = None
    for p in projects:
        if p.name == name:
            project = p
            break
    if project is None:
        print("Project not found.")
        return
    print(f"Updating project '{project.name}':")
    completion_percentage = input("Enter new completion percentage (leave blank to retain existing value): ")
    if completion_percentage.strip() != "":
        project.completion_percentage = int(completion_percentage)
    priority = input("Enter new priority (leave blank to retain existing value): ")
    if priority.strip() != "":
        project.priority = int(priority)
    print("Project updated successfully.")


if __name__ == "__main__":
    filename = "projects.txt"
    projects = load_projects(filename)
    while True:
        print("\nMenu:")
        print("1. Load projects")
        print("2. Save projects")
        print("3. Display projects")
        print("4. Filter projects by date")



