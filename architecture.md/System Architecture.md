# System Architecture

## 1. Architecture Overview

The Hostel Complaint & Maintenance Management System is a
Python-based command-line application.

The system follows a simple modular architecture where each
module performs a specific task.

## 2. Architecture Flow

User
  ↓
main.py
  ↓
Main Menu
  ↓
┌───────────────────────────────────────┐
│                                       │
├── registration.py → Register Complaint
│
├── complaint.py → View Complaints
│
├── search.py → Search Complaints
│
├── status.py → Update Complaint Status
│
└── statistics.py → Generate Statistics
                ↓
            storage.py
                ↓
        complaints.json

validation.py is used to validate complaint data
before it is stored.

## 3. Module Description

### main.py
Controls the main program and displays the menu.

### registration.py
Collects complaint details from the user and registers
a new complaint.

### complaint.py
Generates complaint IDs and displays all complaints.

### search.py
Allows users to search complaints using different fields.

### status.py
Updates the status of a complaint.

### statistics.py
Calculates complaint statistics such as total, pending,
in-progress and resolved complaints.

### validation.py
Checks whether the entered complaint information is valid.

### storage.py
Reads and writes complaint data using a JSON file.

### complaints.json
Stores complaint information permanently.

## 4. Data Flow

1. User enters complaint details.
2. `registration.py` receives the input.
3. `validation.py` checks the input.
4. A unique complaint ID is generated.
5. `storage.py` saves the complaint.
6. The complaint is stored in `complaints.json`.
7. Other modules read the stored data when required.

## 5. Complaint Status Flow

Pending → In Progress → Resolved