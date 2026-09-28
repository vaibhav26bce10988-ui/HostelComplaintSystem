# Testing Documentation

## 1. Testing Objective

Testing was performed to verify that the different modules of the
Hostel Complaint & Maintenance Management System work correctly
both individually and together.

## 2. Functional Testing

| Test | Expected Result | Result |
|---|---|---|
| Register a complaint | Complaint is saved with a unique ID | Passed |
| View complaints | All stored complaints are displayed | Passed |
| Search by Complaint ID | Matching complaint is displayed | Passed |
| Search by Room Number | Matching complaints are displayed | Passed |
| Search by Type | Matching complaints are displayed | Passed |
| Search by Status | Matching complaints are displayed | Passed |
| Search by Priority | Matching complaints are displayed | Passed |
| Update complaint status | Status is updated and saved | Passed |
| View statistics | Correct statistics are displayed | Passed |
| Invalid menu choice | Error message is displayed | Passed |
| Invalid complaint type | Input is rejected | Passed |
| Invalid priority | Input is rejected | Passed |
| Invalid complaint ID | Error message is displayed | Passed |

## 3. Status Testing

The complaint status was tested using the following sequence:

```text
Pending
   ↓
In Progress
   ↓
Resolved