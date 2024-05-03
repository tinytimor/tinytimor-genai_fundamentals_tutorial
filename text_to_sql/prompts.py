data_dictionary = {
    "diagnosis_mapping": """
    Data Dictionary for the 'diagnosis' table in the MIMIC-IV-ED dataset
    
    Table Description:
    This table provides coded diagnoses associated with each ED visit, based on the International Classification of Diseases (ICD) ontology.
    
    Columns:
    - subject_id: (INTEGER) A unique identifier assigned to each individual patient.
    - stay_id: (INTEGER) A unique identifier for the ED visit.
    - seq_num: (INTEGER) A pseudo-order representing the relevance of the diagnosis, with 1 being the most relevant.
    - icd_code: (TEXT) The coded representation of the diagnosis using the ICD ontology.
    - icd_version: (INTEGER) The version of the ICD ontology used (9 or 10).
    - icd_title: (TEXT) The textual description of the ICD code.
    """,
    "edstays_mapping":"""
    Data Dictionary for the 'edstays' table in the MIMIC-IV-ED dataset
    
    Table Description:
    This table tracks patient stays in the emergency department (ED). Each row represents a unique ED visit.
    
    Columns:
    - subject_id: (INTEGER) A unique identifier assigned to each individual patient.
    - hadm_id: (REAL) An identifier representing the hospital admission, if the patient was admitted after the ED visit.
    - stay_id: (INTEGER) A unique identifier for the ED visit.
    - intime: (TEXT) The date and time when the patient was admitted to the ED.
    - outtime: (TEXT) The date and time when the patient was discharged from the ED.
    - gender: (TEXT) The patient's gender.
    - race: (TEXT) The patient's race.
    - arrival_transport: (TEXT) The mode of transportation used by the patient to arrive at the ED (e.g., ambulance, walk-in).
    - disposition: (TEXT) The discharge location or status of the patient after the ED visit (e.g., admitted, discharged home).
    """,
    "medrecon_mapping":"""
    Data Dictionary for the 'medrecon' table in the MIMIC-IV-ED dataset
    
    Table Description:
    This table provides information about the medications the patient was taking prior to their ED visit (medication reconciliation).
    
    Columns:
    - subject_id: (INTEGER) A unique identifier assigned to each individual patient.
    - stay_id: (INTEGER) A unique identifier for the ED visit.
    - charttime: (TEXT) The date and time when the medication reconciliation was documented.
    - name: (TEXT) The textual description of the medication.
    - gsn: (INTEGER) The Generic Sequence Number (GSN) for the medication, if available.
    - ndc: (INTEGER) The National Drug Code (NDC) for the medication, if available.
    - etc_rn: (INTEGER) A sequential number for grouping medications into classes based on an ontology.
    - etccode: (TEXT) The coded representation of the medication class based on an ontology.
    - etcdescription: (TEXT) The textual description of the medication class based on an ontology.
    """,
    "pyxis_mapping": """
    Data Dictionary for the 'pyxis' table in the MIMIC-IV-ED dataset
    
    Table Description:
    This table contains information about medications dispensed from the automated Pyxis MedStation system during the ED visit.
    
    Columns:
    - subject_id: (INTEGER) A unique identifier assigned to each individual patient.
    - stay_id: (INTEGER) A unique identifier for the ED visit.
    - charttime: (TEXT) The date and time when the medication was dispensed.
    - med_rn: (INTEGER) A sequential number for delineating multiple medications dispensed at the same time.
    - name: (TEXT) The textual description of the dispensed medication.
    - gsn_rn: (INTEGER) A sequential number for delineating multiple GSN values associated with the same medication.
    - gsn: (REAL) The Generic Sequence Number (GSN) for the medication, if available.
    """,
    "triage_mapping": """
    Data Dictionary for the 'triage' table in the MIMIC-IV-ED dataset
    
    Table Description:
    This table contains information collected during the triage process, including vital signs, pain level, and the chief complaint reported by the patient.
    
    Columns:
    - subject_id: (INTEGER) A unique identifier assigned to each individual patient.
    - stay_id: (INTEGER) A unique identifier for the ED visit.
    - temperature: (REAL) The patient's body temperature recorded at triage.
    - heartrate: (REAL) The patient's heart rate recorded at triage.
    - resprate: (REAL) The patient's respiratory rate recorded at triage.
    - o2sat: (REAL) The patient's oxygen saturation level recorded at triage.
    - sbp: (REAL) The patient's systolic blood pressure recorded at triage.
    - dbp: (REAL) The patient's diastolic blood pressure recorded at triage.
    - pain: (TEXT) The patient's reported pain level at triage.
    - acuity: (INTEGER) The level of severity assigned by the care provider based on the triage assessment.
    - chiefcomplaint: (TEXT) The patient's reported reason for presenting to the ED, often a comma-separated list of entries.
    """,
    "vitalsign_mapping": """
    Data Dictionary for the 'vitalsign' table in the MIMIC-IV-ED dataset
    
    Table Description:
    This table contains aperiodic vital sign measurements documented for patients during their ED stay.
    
    Columns:
    - subject_id: (INTEGER) A unique identifier assigned to each individual patient.
    - stay_id: (INTEGER) A unique identifier for the ED visit.
    - charttime: (TEXT) The date and time when the vital signs were recorded.
    - temperature: (REAL) The patient's body temperature.
    - heartrate: (REAL) The patient's heart rate.
    - resprate: (REAL) The patient's respiratory rate.
    - o2sat: (REAL) The patient's oxygen saturation level.
    - sbp: (REAL) The patient's systolic blood pressure.
    - dbp: (REAL) The patient's diastolic blood pressure.
    - rhythm: (TEXT) The patient's heart rhythm.
    - pain: (TEXT) The patient's reported pain level.
    """
}