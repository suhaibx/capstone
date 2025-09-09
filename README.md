
# Capstone Data Engineering Project: Sales Revenue Analysis
This project demonstrates an end-to-end data pipeline built using Apache Airflow to analyze daily sales revenue. The pipeline extracts raw transactional data from a PostgreSQL database, aggregates it, and generates valuable business insights through data visualization and reporting.

## Project Objective
The primary goal of this pipeline is to automate the daily sales revenue analysis workflow. It transforms raw sales records into a structured, daily-level summary, providing a clear view of revenue trends over time.

## Pipeline Overview
This data pipeline is orchestrated by Apache Airflow, and it is scheduled to run on a weekly basis. The DAG (Directed Acyclic Graph) consists of three main tasks:

### 1- Extract and Transform: 
A SQL query is executed against the PostgreSQL database to join the orders, order_details, and products tables. It calculates the total revenue for each day and pushes the resulting table to Airflow's XCom for downstream tasks.

### 2- Visualize Revenue: 
The aggregated daily revenue data is pulled from XCom, and a time-series plot is generated using matplotlib. This plot is saved as a PNG file, providing a visual representation of sales trends.

## Generate CSV: 
The aggregated data is also exported to a CSV file. This provides a clean, portable data set that can be used for further analysis or reporting outside of the pipeline.

## Tools and Technologies
1- Orchestration: Apache Airflow

2- Database: PostgreSQL

3- Data Processing: Python, Pandas

4- Data Visualization: Matplotlib

5- Version Control: Git / GitHub

## Project Outputs
The pipeline successfully generates the following outputs, which are available in this repository:

1- daily_revenue_plot.png: A time-series chart of daily sales revenue.

2- daily_revenue_Capstone.csv: A CSV file containing the aggregated daily revenue data.

3- daily_sales_revenue_analysis_v6.py: The complete Airflow DAG script.
