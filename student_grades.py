import re

def average_marks(marks_csv):
    """Return the average of comma-separated integer marks (0–100)."""
    if not isinstance(marks_csv, str):
        raise TypeError("marks_csv must be a string")
    parts = [part.strip() for part in marks_csv.split(",")]
    if not parts or any(not part for part in parts):
        raise ValueError("marks_csv must contain comma-separated marks")
    try:
        marks = [int(part) for part in parts]
    except ValueError as exc:
        raise ValueError("all marks must be integers") from exc
    if any(mark < 0 or mark > 100 for mark in marks):
        raise ValueError("marks must be between 0 and 100")
    return round(sum(marks) / len(marks), 2)

def parse_srn(srn):
    """Return (campus, admission_year, department) for a valid SRN."""
    if not isinstance(srn, str):
        raise TypeError("srn must be a string")
    if not re.fullmatch(r"PES[1-3]UG\d{2}[A-Z]{2}\d{3}", srn):
        raise ValueError("invalid SRN format")
    return srn[:4], int(srn[6:8]), srn[8:10]

def short_name(full_name):
    """Return first initial and surname for a name with at least two parts."""
    if not isinstance(full_name, str):
        raise TypeError("full_name must be a string")
    parts = full_name.split()
    if len(parts) < 2:
        raise ValueError("full_name must contain at least first and last names")
    return parts[0][0].upper() + ". " + parts[-1].capitalize()

def main():
    print("==== Running average_marks ====")
    try:
        print("Average Marks:", average_marks(input("Enter marks as CSV (e.g. 78,85,92): ")))
    except (TypeError, ValueError) as exc:
        print("Invalid marks:", exc)
    print("\\n==== Running parse_srn ====")
    try:
        print("Campus, Year and Dept:", parse_srn(input("Enter an SRN (e.g. PES1UG23CS123): ")))
    except (TypeError, ValueError) as exc:
        print("Invalid SRN:", exc)
    print("\\n==== Running short_name ====")
    try:
        print("Short Name:", short_name(input("Enter first and last name (e.g. ravi kumar): ")))
    except (TypeError, ValueError) as exc:
        print("Invalid name:", exc)

if __name__ == "__main__":
    main()
