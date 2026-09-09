# CLI Task Tracker

A simple and lightweight **Command-Line Task Tracker** that helps you manage your daily tasks directly from the terminal.

You can create, update, delete, list, and manage tasks without leaving the command line.

## ✨ Features

* ➕ Add new tasks
* 📋 View all tasks
* 🔍 View tasks by status
* ✏️ Update task status
* 🗑️ Delete tasks
* ✅ Mark tasks as completed
* 🔄 Change task status
* 💾 Store tasks locally using JSON
* ⚡ Fast and easy CLI interface

## 🛠️ Technologies Used

* Python
* Python `sys` module for CLI arguments
* JSON for local data storage
* Git & GitHub

## 🚀 Usage

This task tracker is a simple command-line application built with Python.

You can add tasks, update their status, view tasks by status, and delete tasks directly from the terminal.

### ➕ Add a Task

To add a new task:

```bash
python main.py add "learn python"
```

The task will be added with the default `todo` status.

---

### 🔄 Update Task Status

To update the status of a task:

```bash
python main.py update <id> "<status>"
```

Available statuses:

* `todo`
* `in-progress`
* `done`

Examples:

```bash
python main.py update 1 "in-progress"
```

```bash
python main.py update 1 "done"
```

```bash
python main.py update 1 "todo"
```

---

### 📋 List Tasks

You can view all tasks or filter tasks by their status.

#### Show All Tasks

```bash
python main.py list
```

This displays all tasks regardless of their status.

#### Show Todo Tasks

```bash
python main.py list todo
```

This displays only tasks with the `todo` status.

#### Show In-Progress Tasks

```bash
python main.py list in-progress
```

This displays only tasks with the `in-progress` status.

#### Show Completed Tasks

```bash
python main.py list done
```

This displays only tasks with the `done` status.

---

### 🗑️ Delete a Task

To delete a task:

```bash
python main.py delete <id>
```

Example:

```bash
python main.py delete 1
```

This permanently removes the task with the specified ID.

---

## 📝 Command Summary

| Command                                    | Description                         |
| ------------------------------------------ | ----------------------------------- |
| `python main.py add "task"`                | Add a new task                      |
| `python main.py update <id> "todo"`        | Change task status to `todo`        |
| `python main.py update <id> "in-progress"` | Change task status to `in-progress` |
| `python main.py update <id> "done"`        | Mark task as completed              |
| `python main.py list`                      | Show all tasks                      |
| `python main.py list todo`                 | Show only todo tasks                |
| `python main.py list in-progress`          | Show only in-progress tasks         |
| `python main.py list done`                 | Show only completed tasks           |
| `python main.py delete <id>`               | Delete a task                       |

## 📁 Project Structure

The project has a simple structure:

```text
task-tracker/
│
├── main.py
├── tasks.json
└── README.md
```

### Files

* **`main.py`** — The main Python file containing the task tracker application and CLI commands.
* **`tasks.json`** — Stores all tasks and their statuses. This file is automatically created by the application if it does not already exist.
* **`README.md`** — Project documentation and usage instructions.

> **Note:** You don't need to manually create `tasks.json`. The application will automatically create it when required.

## 🔄 Workflow

The Task Tracker follows a simple workflow:

```text
┌───────────────┐
│   Add Task    │
│   status:     │
│     todo      │
└───────┬───────┘
        │
        ▼
┌──────────────────┐
│  Update Status   │
│                  │
│  todo            │
│    ↓             │
│  in-progress     │
│    ↓             │
│  done            │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    List Tasks    │
│                  │
│  All             │
│  Todo            │
│  In-progress     │
│  Done            │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Delete Task    │
└──────────────────┘
```
## 🔗 Project URL

## 🔗 Project URL

[Python CLI Task Tracker] : https://github.com/Tazbin-Hossen/Python_CLI_Task_Tracker



## 📄 License

This project is open-source and available under the **MIT License**.
