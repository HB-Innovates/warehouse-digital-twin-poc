"""
kpi_logger.py
Logs throughput and travel time KPIs.
"""
import logging

logging.basicConfig(filename='warehouse_kpi.log', level=logging.INFO)

def log_throughput(value):
    logging.info(f"Throughput: {value}")

def log_travel_time(value):
    logging.info(f"Travel time: {value}")

if __name__ == "__main__":
    log_throughput(100)
    log_travel_time(12.5)
    print("KPIs logged to warehouse_kpi.log")
