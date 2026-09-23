"""Reusable helpers for summarizing clinic systolic readings."""

def systolic_readings(encounters):
    """This method will return all systolic values which is the last entry in each encounter"""
    lst = []
    for values in encounters:
        lst.append(int(values[2]))
    return lst



def mean_systolic(readings):
    """This method will return the mean of all systolic readings"""
    total = 0
    for val in readings:
        total += val
    return total/len(readings)


def count_patients(encounters):
    """Returns the number of unique patients"""
    # TODO: collect the patient IDs and keep only the distinct ones.
    patient_ids = []
    for values in encounters:
        if values[0] not in patient_ids:
            patient_ids.append(values[0])
    
    return patient_ids


def patients_at_or_above(encounters, cutoff):
    """Patients with a systolic value of 150mmHg or higher must follow-up"""
    # TODO: keep each patient whose systolic reading is at or above cutoff.
    patient_ids = []
    for values in encounters:
        if int(values[2]) >= cutoff and values[0] not in patient_ids:
            patient_ids.append(values[0])
    return patient_ids
    
