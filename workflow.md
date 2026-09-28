# System Workflow

## Main Workflow

Start
  ↓
Open Application
  ↓
Display Main Menu
  ↓
Choose an Option
  ↓
┌─────────────────────────────────────┐
│                                     │
├── Register Complaint                │
│        ↓                            │
│   Enter Complaint Details           │
│        ↓                            │
│   Validate Details                  │
│        ↓                            │
│   Generate Complaint ID             │
│        ↓                            │
│   Save Complaint                    │
│                                     │
├── View All Complaints               │
│        ↓                            │
│   Read Complaint Data               │
│        ↓                            │
│   Display Complaints                │
│                                     │
├── Search Complaint                  │
│        ↓                            │
│   Enter Search Criteria             │
│        ↓                            │
│   Search Stored Complaints          │
│        ↓                            │
│   Display Matching Complaints       │
│                                     │
├── Update Complaint Status            │
│        ↓                            │
│   Enter Complaint ID                │
│        ↓                            │
│   Select New Status                 │
│        ↓                            │
│   Save Updated Status               │
│                                     │
└── Complaint Statistics              │
         ↓
    Read Complaint Data
         ↓
    Calculate Statistics
         ↓
    Display Results

          ↓
      Return to Menu
          ↓
        Exit
          ↓
         End