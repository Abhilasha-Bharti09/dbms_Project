# 🩸 VITAL FLOW — Backend Contribution

## 📌 About the Project

Blood Connect is a team-based blood donation management system designed to help connect blood requests with suitable nearby donors.

This repository contains my backend contribution to the project.

## 👩‍💻 My Contribution

I developed the `logic.py` backend module, which handles the core backend operations of the system.

### 🔹 Supabase Integration

- Connected the Python application with Supabase.
- Loaded Supabase credentials securely using environment variables.
- Created the Supabase client for database operations.

### 🔹 Nearest Donor Search

- Implemented donor-search logic using hospital latitude and longitude.
- Integrated the Supabase RPC function `get_nearest_donors_sql`.
- Filtered donors according to the required blood group.
- Retrieved donor information including distance.

### 🔹 Blood Request Status Management

Implemented request lifecycle logic:

```text
Pending
   ↓ Accept
Accepted
   ↓ Completed
Deactivated
