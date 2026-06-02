# Todo Application (Flask + SQLite)

A clean and structured task management system built using **Flask** for backend routing, **SQLite** for persistent storage, and **Tailwind CSS** for a minimal and responsive interface.  
This application is suitable for learning backend development fundamentals, CRUD API design, and real-time UI updating via Fetch API.

---

## Table of Contents

1. Overview
2. Features
3. Technology Stack
4. Project Workflow
5. Database Structure
6. API Endpoints
7. UI and User Interaction
8. Automatic Date Handling & Overdue Logic
9. Project Structure
10. Installation & Setup
11. Future Enhancements
12. License

---

## 1. Overview

This Todo Application allows users to add tasks with optional scheduling details.  
If no date or time is provided, the system assigns the current date and time automatically.  
Tasks can be completed, reset, or deleted. Additionally, the application visually separates:

- **Today’s Tasks**
- **Overdue Tasks**

This organization supports daily workflow tracking and prioritization management.

---

## 2. Features

| Category | Description |
|---------|-------------|
| Task Creation | Add tasks with optional date & day. Defaults are auto-generated. |
| Task Display | View all tasks in a structured table layout. |
| Status Management | Mark tasks as completed or reset to pending. |
| Task Removal | Delete tasks permanently from the database. |
| Smart UI Panels | Collapsible sections show **Today’s Tasks** and **Overdue Tasks**. |
| Auto State Correction | Older tasks are automatically reorganized. |
| Persistent Storage | SQLite database maintains tasks over sessions. |

---

## 3. Technology Stack

| Component | Technology |
|----------|------------|
| Backend Framework | Flask |
| Database | SQLite |
| Frontend Structure | HTML5 |
| Styling | Tailwind CSS |
| Runtime Logic | JavaScript (Fetch API) |

---

## 4. Project Workflow

1. User submits task form.
2. Backend inserts data into SQLite (with auto timestamp fallback when required).
3. Frontend task table updates without page reload.
4. Special sections dynamically fetch:
   - Only tasks scheduled for **today**
   - Tasks whose scheduled date has already **passed**
5. User interacts through action buttons:
   - Complete
   - Reset
   - Delete

---

## 5. Database Structure

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER (PK) | Unique Task ID |
| task | TEXT | Description of the task |
| day | TEXT | Day name (optional or auto-assigned) |
| date | TEXT (YYYY-MM-DD) | Scheduled date |
| time | TEXT (HH:MM:SS) | Scheduled time |
| status | TEXT | `pending` or `completed` |
| created_at | DATETIME | Auto timestamp |

---

## 6. API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/task/add` | Add a new task |
| GET | `/api/task/all` | Retrieve all tasks |
| POST | `/api/task/update` | Update task text |
| POST | `/api/task/complete` | Mark a task completed |
| POST | `/api/task/delete` | Delete task |
| POST | `/api/task/reset` | Reset status to pending |
| GET | `/api/task/today` | Fetch only tasks scheduled for today |
| GET | `/api/task/overdue` | Fetch tasks where scheduled date has passed |

---

## 7. UI & User Interaction

- **Task Table** lists all tasks with actionable controls.
- **Today’s Tasks Panel** shows only tasks matching the current system date.
- **Overdue Panel** highlights tasks past their due date.
- Expand/Collapse panels allow clean visibility and workspace focus.

---

## 8. Automatic Date Handling & Overdue Logic

If a user does not provide values:

| Field | Automatically Assigned |
|-------|------------------------|
| Day | Current weekday name |
| Date | System local date |
| Time | System local time |

Overdue logic:

