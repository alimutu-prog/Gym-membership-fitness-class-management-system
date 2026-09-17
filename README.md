# Gym-membership-fitness-class-management-system

## Project Title
**Project 8 — Gym Membership & Fitness Class Management System**

## Team Members
* **Japheth Waweru**— Member management
* **Adio Marcel**— Fitness class management
* **Vincent Mussa**— Registrations & file handling
* **Allan Limutu** — Menu, validation, exception handling, testing

## Project Description
A menu-based Python application for a gym to manage members and the
fitness classes they can register for. The system tracks member details,
class capacity, and registrations, and saves all information to disk so
it is available again the next time the program runs.

## Main Features
* **Member Management:** Register a new gym member; prevent duplicate members (same contact)
* **Member Search & Display:** Display all members and search by ID or name
* **Fitness Class Operations:** Add a fitness class with a set capacity as well as display all fitness classes and see whether each is OPEN or FULL
* **Registration Workflow:** Register a member for a class; blocked if the class is full or the member is already registered
* **Cancellation System:** Cancel a registration, which frees up a spot in the class
* **Reporting & Persistence:** View a member's registered classes, or view all registrations. Automates reading and writing to disk on startup and exit.

## Menu Structure
1. Add Member
2. Display All Members
3. Search Member
4. Add Fitness Class
5. Display All Fitness Classes
6. Register Member for a Class
7. Cancel a Registration
8. View a Member's Registered Classes
9. View All Registrations
10. Save Data
11. Exit


## Classes Used
* **`Member`** — Manages member personal info and membership tier details.
* **`FitnessClass`** — Tracks class schedules, instructors, and dynamic capacity limits.
* **`Registration`** — Links a single `Member` to a `FitnessClass` with status tracking.
* **`GymSystem`** — Central orchestrator managing state, collections, and core business rules.
* **`file_handler`** — Facilitates CSV serialization and data loading/saving.

## Files Used
- `data/members.csv` — one row per member
- `data/classes.csv` — one row per fitness class
- `data/registrations.csv` — one row per registration

These are created automatically the first time you save data.

## How to Run the Application
```bash
python main.py
```


## Project Structure

member.py -> Member class (Member A)
fitness_class.py -> FitnessClass class (Member B)
registration.py -> Registration class (Member C)
file_handler.py -> save/load functions (Member C)
gym_system.py -> manager class tying it together (shared, sections labelled)
main.py -> menu, validation, error handling (Member D)
Class_Design_Document.md
Test_Plan.md
Test_Results.md


## Team Contributions
- Japheth Waweru: Built the `Member` class and the add/display/search
  member features; wrote and executed Member test cases.
- Adio Marcel: Built the `FitnessClass` class, including capacity
  tracking (`is_full`); wrote and executed FitnessClass test cases.
- Vincent Mussa: Built the `Registration` class, the register/cancel
  logic, and all file handling (`file_handler.py`); wrote and executed
  Registration and file-handling test cases.
- Allan Limutu: Built the main menu loop, all input validation, and
  exception handling across the app; ran the full Test Plan and
  recorded Pass/Fail results; demonstrated the GitHub commit history.
