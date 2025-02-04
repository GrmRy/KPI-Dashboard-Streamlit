# Retail Sales KPI Dashboard

This project is a KPI dashboard built using Streamlit and Plotly to visualize retail sales data. The dashboard displays key performance indicators (KPIs) such as total sales, total orders, average sales per order, and unique customers. It also provides interactive visualizations including a monthly sales trend line chart, a bar chart for sales by product category, and a pie chart for sales by gender.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Overview

The dashboard is designed to help users explore and analyze retail sales data. Users can filter the data by date range, product category, and gender using the sidebar filters. The dashboard then updates the KPIs and charts based on the selected criteria. Check out the live app here: [KPI Sales Dashboard](https://kpidashboardsales-sbfbu7qqxasv8bbcd9rjey.streamlit.app/)

## Features

- **Key Performance Indicators (KPIs):**
  - Total Sales (displayed in millions)
  - Total Orders
  - Average Sale per Order
  - Unique Customers

- **Visualizations:**
  - **Sales Over Time:** A smooth line chart with markers showing monthly sales trends.
  - **Sales by Product Category:** A bar chart that displays the total sales for each product category using a “Blues” color scale.
  - **Sales by Gender:** A pie chart showing the sales distribution between genders.

- **Sidebar Filters:**
  - Date range selection (start and end dates)
  - Multi-select filter for product categories
  - Multi-select filter for gender

- **Dark Theme:**  
  The dashboard uses a dark theme for a modern and visually appealing look.

## Dataset

The dataset used in this project is a retail sales dataset containing the following columns:

```
Transaction ID,Date,Customer ID,Gender,Age,Product Category,Quantity,Price per Unit,Total Amount
```

You can download the dataset from Kaggle:

- [Retail Sales Dataset on Kaggle](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)

Make sure to place the downloaded CSV file (e.g., `retail_sales.csv`) in the project directory.

## Installation

Before running the project, ensure you have the required dependencies installed.

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/retail-sales-kpi-dashboard.git
   cd retail-sales-kpi-dashboard
   ```

2. **Create a Virtual Environment (Optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *If you do not have a `requirements.txt` file, install the following packages:*

   ```bash
   pip install streamlit pandas plotly
   ```

4. **Ensure Your Dataset is Ready:**

   Place your dataset file (e.g., `retail_sales.csv`) in the project directory.

## Usage

To launch the dashboard, run the following command in your project directory:

```bash
streamlit run dashboard.py
```

This will open the dashboard in your default web browser. Use the sidebar filters to adjust the date range, product categories, and gender, and the visualizations and KPIs will update automatically.

## Project Structure

```
retail-sales-kpi-dashboard/
├── retail_sales.csv         # Your dataset file
├── dashboard.py             # Main Streamlit application
├── README.md                # Project documentation
└── requirements.txt         # Project dependencies (if available)
```


