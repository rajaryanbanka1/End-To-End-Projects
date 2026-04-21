# pipeline/run_pipeline.py

import subprocess

steps = [
    "F:/Repository/End-To-End-Projects/E-commerce Data Platform/ingestion/kaggle_ingest.py",
    "F:/Repository/End-To-End-Projects/E-commerce Data Platform/processing/transform.py",
    "F:/Repository/End-To-End-Projects/E-commerce Data Platform/processing/curate.py",
    "F:/Repository/End-To-End-Projects/E-commerce Data Platform/ingestion/load_to_db.py"
]

for step in steps:
    subprocess.run(step, shell=True)

print("Pipeline completed")