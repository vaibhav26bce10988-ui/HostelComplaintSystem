# Design Decisions

## 1. Choice of Python

Python was selected because it is simple to understand and suitable
for implementing the programming concepts taught in CSE1021.

## 2. Command-Line Interface

A command-line interface was selected because the project is designed
as a simple first-semester programming project.

It allows users to interact with the system using menu options.

## 3. Modular Structure

The project is divided into multiple Python files.

Each file performs a specific task such as registration, searching,
status management, validation, storage, and statistics.

This makes the program easier to understand and maintain.

## 4. JSON Storage

A JSON file is used to store complaint data.

It is simple to use with Python and is sufficient for a small
hostel complaint management system.

## 5. Complaint Status

The complaint follows a simple status flow:

Pending → In Progress → Resolved

This makes it easy to track the progress of a complaint.

## 6. Input Validation

Input validation is used to prevent incomplete or invalid complaint
information from being stored.

## 7. Search Method

The system uses simple sequential searching through the stored
complaints.

This approach is suitable for a small dataset and demonstrates
basic programming and searching concepts covered in the course.

## 8. Statistics

The system calculates complaint counts and resolution rate using
loops, conditions, dictionaries, and basic arithmetic.

These concepts are directly related to the programming concepts
covered in CSE1021.