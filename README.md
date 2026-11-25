
# Student Performance Analyzer

A Flask-based web application for analyzing student performance from CSV files using Pandas.

## Features

- Upload student data using a CSV file
- Read and process CSV data using Pandas
- Calculate total marks
- Calculate average marks
- Assign grades
- Calculate class average
- Identify the top performer
- Calculate pass percentage
- Display student results in an HTML table
- REST API for analyzing JSON student data

## Technologies Used

- Python
- Flask
- Pandas
- HTML
- CSS
- Jinja2

## Project Structure

```text
student-performance-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
└── templates/
    ├── form.html
    └── result.html
```

## CSV Format

The uploaded CSV file should contain the following columns:

```csv
name,maths,science,english
Hadee,80,90,70
Ameen,90,85,95
```

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

Move into the project folder:

```bash
cd student-performance-analyzer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Run the Application

Run:

```bash
python app.py
```

Open the application in your browser at:

`http://127.0.0.1:5000`

## API

### POST /api/analyze

The API accepts student information in JSON format.

Example request:

```json
[
    {
        "name": "Hadee",
        "maths": 80,
        "science": 90,
        "english": 70
    },
    {
        "name": "Ameen",
        "maths": 90,
        "science": 85,
        "english": 95
    }
]
```

Example response:

```json
{
    "summary": {
        "class_average": 85.0,
        "class_performer": "Ameen",
        "pass_percentage": 100.0
    }
}
```

## Author

Hadee Ameen
