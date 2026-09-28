# Hostel Complaint & Maintenance Management System

## 1. Project Overview

The Hostel Complaint & Maintenance Management System is a
Python-based command-line application designed to help hostel
students register and manage maintenance complaints.

The system allows users to register complaints, view complaints,
search for specific complaints, update complaint status, and view
basic complaint statistics.

## 2. Problem

Hostel students may face problems such as electrical faults,
plumbing issues, cleaning problems, and damaged furniture.

Managing these complaints manually can make it difficult to track
their status and find previous complaints.

This project provides a simple digital solution for managing
hostel maintenance complaints.

## 3. Features

- Register new complaints
- Automatically generate complaint IDs
- View all registered complaints
- Search complaints
- Search by complaint ID, room, type, status, or priority
- Update complaint status
- Track Pending, In Progress, and Resolved complaints
- View complaint statistics
- Calculate resolution rate
- Find the most common complaint type
- Validate user input
- Store data using JSON

## 4. Technologies Used

- Python 3
- JSON
- Visual Studio Code
- Git
- GitHub

## 5. Project Structure

```text
HostelComplaintSystem/
│
├── main.py
├── registration.py
├── complaint.py
├── search.py
├── status.py
├── statistics.py
├── validation.py
├── storage.py
│
├── data/
│   └── complaints.json
│
├── docs/
│   └── system_architecture.png
│
├── README.md
├── statement.md
├── architecture.md
├── workflow.md
├── requirements.md
└── design.md