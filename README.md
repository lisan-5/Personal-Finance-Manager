# Personal Finance Manager Pro

A comprehensive command-line personal finance management system built with Python, designed to help users track expenses, manage budgets, and gain financial insights.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- 📊 **Expense Tracking**: Categorize and track all your expenses
- 💰 **Income Management**: Record and monitor your income sources
- 📈 **Financial Reports**: Generate detailed financial reports and insights
- 🎯 **Budget Planning**: Set and track budgets by category
- 📅 **Transaction History**: View and filter transaction history
- 📊 **Trend Analysis**: Analyze monthly spending patterns
- 🏷️ **Category Management**: Customize expense categories
- 📤 **Data Export**: Export data to CSV format

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lisan-5/Personal-Finance-Manager.git
cd personal-finance-manager-pro
```

2. Run the application:
```bash
python main.py
```

## Usage

The application provides an interactive command-line interface with the following options:

1. **Add Expense**: Record new expenses with categories
2. **Add Income**: Track your income sources
3. **View Report**: Generate financial reports and insights
4. **Set Budget**: Set monthly budgets by category
5. **Export Data**: Export your financial data to CSV
6. **View Transactions**: Browse your transaction history
7. **Manage Categories**: Customize expense categories
8. **Analyze Trends**: View monthly financial trends
9. **Exit**: Close the application

## Project Structure

```
personal-finance-manager-pro/
├── main.py
├── modules/
│   ├── analysis/
│   │   └── trends.py
│   ├── budget/
│   │   └── manager.py
│   ├── categories/
│   │   └── manager.py
│   ├── config/
│   │   └── constants.py
│   ├── database/
│   │   ├── core.py
│   │   └── transactions.py
│   ├── reports/
│   │   └── report_generator.py
│   ├── transactions/
│   │   ├── expense_manager.py
│   │   ├── income_manager.py
│   │   └── viewer.py
│   └── utils/
│       ├── calculations.py
│       ├── console.py
│       ├── date_helpers.py
│       └── input_validators.py
```

## Data Storage

The application stores all financial data in a JSON file (`finance_data.json`) with the following structure:

- Expenses: Timestamp, category, amount, and description
- Income: Timestamp, amount, and description
- Budget: Category-wise budget allocation
- Categories: List of expense categories

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Thanks!!!


## Author

Lisanegebriel Abay - [@lisan-5](https://github.com/lisan-5)
