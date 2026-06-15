# You're creating a monthly report for a cafe's sales.
# Instead of putting all logic in one place, break it down.
# Tasks:
# 1. Write a functio generate_report() that calls: 
#     - fetch_sales()
#     - filter_valid_orders()
#     - summarize_data()

def fetch_sales():
    print("Fetching the sales data")

def filter_valid_orders():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarazing data")

def generate_report():
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print("Report is ready")

generate_report()