# Naukri Job Automation Bot

This project automates the end-to-end job search process on [Naukri.com](https://www.naukri.com) using Python and Selenium. It simulates a real user logging in, searching for jobs, applying filters, and scraping structured job listing data into a CSV file.

---

## Features

- Automates login to a Naukri.com account
- Enters job title and preferred location
- Expands job-type filters and selects specific roles
- Scrapes relevant job data including:
  - Job Title
  - Company Name
  - Location
  - Experience Required
  - Posting Date
  - Skill Tags
  - Job Description
- Saves the extracted results into a CSV file using `pandas`
- Modular class-based Selenium structure with clean method separation

---

## Tech Stack

| Tool         | Purpose                        |
|--------------|--------------------------------|
| Python       | Core programming language      |
| Selenium     | Web browser automation         |
| pandas       | Data handling and CSV writing  |
| ChromeDriver | Interface with Chrome browser  |

---

## Project Structure

| Path                        | Description                                |
|-----------------------------|--------------------------------------------|
| `naukri/`                   | Main package directory                     |
| ├── `__init__.py`           | Initializes the Python package             |
| ├── `main.py`               | Naukri bot core Selenium logic             |
| └── `constructor.py`        | Stores email, password, and job config     |
| `run.py`                    | Entry point for running the bot            |
| `requirements.txt`          | Required Python packages                   |
| `naukri_job_results.csv`    | Output file with scraped job data          |
| `.gitignore`                | Specifies untracked files for Git          |
| `README.md`                 | Project documentation (this file)          |


