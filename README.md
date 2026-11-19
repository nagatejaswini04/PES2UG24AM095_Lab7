# Lab 7 – Fuzz Testing (Student Grades)

**Student:** Naga Tejaswini  
**SRN:** PES2UG24AM095  
**Section:** 5B

Adapted from the supplied friend's Spam Scoring repository for the assigned
Problem 16 Student Grades application. Friend's functions are not copied.

## Files
- `student_grades.py` – hardened application
- `test_student_grades.py` – Hypothesis property-based tests
- `reports/` – execution status
- `evidence/` – save actual terminal screenshots here

## Run in PowerShell
```powershell
py -m pip install -r requirements.txt
py student_grades.py
py -m pytest -v
```

Tests cover valid and invalid CSV marks, malformed SRNs, names with unusual
spacing/word counts, and non-string inputs.

## Evidence
The friend reference provides test-structure guidance, but it is a different
assignment. Capture actual screenshots from your own runs; no screenshot or
test result is fabricated. The before-fix failure evidence must be captured
using the original buggy `student_grades.py` from the assigned repository.

## Suggested commits
```powershell
git add test_student_grades.py
git commit -m "Add Hypothesis fuzz tests for student grades"
git add student_grades.py README.md requirements.txt reports evidence
git commit -m "Fix input validation bugs in student grades"
```
