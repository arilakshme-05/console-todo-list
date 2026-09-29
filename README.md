# Console To-Do List

A lightweight, terminal-based task management application in Python that supports adding, viewing, updating, and deleting tasks with automatic file persistence.

---

##  Features

* **Add Tasks:** Append new tasks to your To-Do list.
* **View Tasks:** Display all current tasks with index numbers.
* **Update Tasks:** Modify existing tasks in real time.
* **Delete Tasks:** Remove completed or unwanted tasks.
* **File Persistence:** Automatically saves and retrieves tasks from a local `tasks.txt` file using Python's built-in file handling (`open()`).

---

##  Tech Stack & Requirements

* **Language:** Python 3.x
* **Storage:** Local text file (`tasks.txt`)
* **Dependencies:** None (uses standard Python built-in modules)

---

##  Repository Structure

```text
console-todo-list/
│
├── todo.py          # Main application script
├── tasks.txt        # Text file created automatically to store tasks
└── README.md        # Project documentation

How to Run
1.Clone the repository:
git clone [https://github.com/arilakshme-05/console-todo-list.git](https://github.com/arilakshme-05/console-todo-list.git)
cd console-todo-list

2.Run the application:
Windows:
py todo.py
macOS / Linux:
python3 todo.py

3.Data Storage:
A file named tasks.txt will be automatically generated in the same directory upon adding tasks.
