# Job Market Analyzer

A Python Data Engineering project that analyzes job market skill demand using ETL pipeline architecture.

## Project Overview

This project extracts job skills data, transforms it to identify the most demanded skills, and loads the results into a report.

The project demonstrates core Data Engineering concepts such as:

- Data Extraction
- Data Transformation
- Data Loading
- Automated pipelines
- Data analysis with Pandas

## Tech Stack

- Python
- Pandas
- Git
- GitHub

## Project Structure

Job-market-analyzer
│
├── data
│   └── job_skills.csv
│
├── output
│   └── top_skills_report.csv
│
├── src
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── pipeline.py
└── README.md

## How to Run the Project

1. Clone the repository
2. Install required libraries
3. Run the pipeline

```bash
python pipeline.py
