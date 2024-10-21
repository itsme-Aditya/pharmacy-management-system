# Pharmacy Management System

## Introduction

The Pharmacy Management System is a simple web application built using Streamlit, designed to manage drugs, customers and orders efficiently. It allows users to add drugs, customers, and orders, and view the relevant information easily.

## Demo

[![Watch the demo](https://img.youtube.com/vi/O_Y2Y01gwwg/0.jpg)](https://youtu.be/O_Y2Y01gwwg)

## Features

- **Add Drugs**: Store drug information including name, expiry date, use, quantity, and price.
- **Add Customers**: Manage customer details like name, email, and phone number.
- **Add Orders**: Process orders for drugs and maintain a record of transactions.
- **View Records**: Easily view all drugs, customers, and orders in a user-friendly interface.

## Key Technologies Used

- **SQLite3**: A lightweight database engine for data storage.
- **Streamlit**: A Python library for creating web applications easily.
- **Pandas**: A data analysis library for handling structured data.
- **Python**: The programming language used to develop the application.

## Getting Started

Follow these steps to set up the Pharmacy Management System on your Linux machine:

### Step 1: Clone the Repository

Open your terminal and run the following command (replace 'repo_url' with url of this repo) to clone the repository:

```bash
git clone 'repo_url'
```
### Step 2: Change Directory

Navigate to the cloned repository:

```bash
cd Pharmacy_Management_System
```
### Step 3: Set Up a Python Virtual Environment

Create and activate a Python virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```
### Step 4: Install Required Packages

Install the necessary packages using pip:

```bash
pip install streamlit pandas Pillow
```
### Step 5: Verify SQLite3 Installation

Check if sqlite3 is already available in Python by running:

```bash
python -c "import sqlite3; print(sqlite3.version)"
```
### Step 6: Run the Streamlit Application

Finally, start the Streamlit application:

```bash
streamlit run app.py
```
