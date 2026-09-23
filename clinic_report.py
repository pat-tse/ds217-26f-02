#!/usr/bin/env python3
"""Summarize one week of clinic encounters and save the two report files."""

from pathlib import Path

from vitals_tools import (
    count_patients,
    mean_systolic,
    patients_at_or_above,
    systolic_readings,
)


DATA_PATH = Path("data") / "clinic_encounters.csv"
OUTPUT_DIR = Path("output")


def read_encounters(data_path):
    """A usable encounter should have a patient_id, date, and a systolic blood pressure value between teh values of 60 and 250

    Give back two values: the list of usable encounters, and how many data
    rows you skipped. `main()` unpacks them the way the lecture unpacks a
    tuple, with two names on the left of the `=`.
    """

    encounters = []
    skipped = 0
    with open(data_path, "r", encoding="utf-8") as report_file:
        file_lst = report_file.read().split("\n")
        for i in range(1, len(file_lst)):
            values = file_lst[i].split(",")
            if len(values) == 3 and values[2].isdigit() and 60 <= int(values[2]) <= 250:
                encounters.append(values)
            else:
                print("SKIPPED:", file_lst[i])  
                skipped += 1  
                
        return encounters, skipped


def main():
    """TODO: describe the two artifacts this writes."""
    encounters, skipped = read_encounters(DATA_PATH)
    readings = systolic_readings(encounters)
    # TODO: build the six report lines and write them to output/vitals_report.txt.
    # TODO: read the file back and print it, so you can see what was saved.
    # TODO: choose your follow-up cutoff, then write output/followup_list.txt
    #       with the Cutoff line, the Reason line, and one patient ID per line.
    with open(OUTPUT_DIR/"vitals_report.txt", "w", encoding="utf-8") as vitals_report:
        output = "Usable encounters: " + str(len(encounters)) + "\nSkipped rows: " + str(skipped) + "\nPatients seen: " + str(len(count_patients(encounters))) + "\nMean systolic: " + str(mean_systolic(readings)) + " mmHg\nHighest systolic: " + str(max(readings)) + " mmHg\nLowest systolic: " + str(min(readings)) + " mmHg"
        vitals_report.write(output)
    
    cutoff = 150
    patient_ids = patients_at_or_above(encounters, cutoff)

    with open(OUTPUT_DIR/"followup_list.txt", "w", encoding="utf-8") as followup:
        answer = "Cutoff: " + str(cutoff) + "\nReason: " + "Systolic levels are at dangerous levels\n"
        for id in patient_ids:
            answer += id + "\n"
        
        followup.write(answer)

if __name__ == "__main__":
    main()
