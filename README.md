# Personal Finance Manager

Personal Finance Manager is a tool designed to help you track income, expenses, budgets, and savings goals. This application allows you to manage your financial data effectively and export reports to Excel.

## Features

- **Manage Income**: Add and view income records.
- **Manage Expenses**: Add and view expense records.
- **Manage Budget**: Set and view budget amounts by category.
- **Track Savings**: Set savings goals, add savings amounts, and view progress.
- **Generate Reports**: Export all financial data to an Excel file for detailed analysis.

## Getting Started

To get started with the Personal Finance Manager, follow these steps:

### Prerequisites

- Python 3.x
- `openpyxl` library

#### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/finaldestroyer/personal_finance_manager.git
   cd personal_finance_manager

2. **Install Dependencies**:
    In terminal run install "pip install openpyxl"

##### Usage

1. **Run the Application**:
    In terminal run "python finance_manager.py"

2. **Interaction with the Menu**:
    Interaction with the Menu:
        1: Manage Income
        2: Manage Expenses
        3: Manage Budget
        4: Track Savings
        5: Generate Reports
        6: Exit

3. **Export to Excel**:
    To generate a report, select the "Generate Reports" option. The data will be exported to personal_finance_report.xlsx.

###### File Structure
    data/:                              ####Contains JSON files for income, expenses, budget, and savings data.
    income.py:                          ###Manages income records.
    expenses.py:                        ###Manages expense records.
    budget.py:                          ###Manages budget records.
    savings.py:                         ###Manages savings records.
    reports.py:                         ###Contains functions for generating reports.
    export.py:                          ###Handles exporting data to Excel.
    finance_manager.py:                 ###The main entry point for the application.

