import os
import sys
import pandas as pd

sys.path.append(os.path.abspath('../..'))

from src.data_generator.generate_synthetic_cruise_bookings_data import generate_data
from src.validation.validator import validate


DATA_DIR = "../../data"
REPORT_DIR = "../../reports"
REPORT_PATH = "../../reports/validation_report.txt"

#check if directories for data and reports exists; create if none
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)

#generate datasets 
print("Generating synthetic datasets...")
generate_data()  #datasets will be placed in data directory
print("Datasets generated.\n")

#run validations on dataset
print("Running data quality validations...")
issues = validate()
issue_count = len(issues)

if issue_count > 0:
    print("Issues found")

#calculate quality scores
score = max(0, 100 - (issue_count * 2))  #weighted penalty
print("Data Quality Score: {0}".format(score)) 

#save issue as report
print("Saving validation report...")

bookings = pd.read_csv(f"{DATA_DIR}/bookings.csv")
total_records = len(bookings)


with open(REPORT_PATH, "w") as f:
    f.write("CRUISE DATA QUALITY REPORT\n")
    f.write("===========================\n\n")
    f.write(f"Total Number of Bookings: {total_records}\n\n")

    if not issues:
        f.write("All data quality checks passed.\n")
    else:
        f.write("Issues Detected:\n")
        for issue in issues:
            f.write(f"- {issue}\n")

    f.write(f"\nData Quality Score: {score}%\n")

print("Report saved at:", REPORT_PATH)

print("\nPipeline completed successfully.")
print(f"Final Data Quality Score: {score}%")

