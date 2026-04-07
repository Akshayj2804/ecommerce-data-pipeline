import logging
import os
from datetime import datetime

logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_pipeline():
    logging.info("Pipeline started")

    os.system("python scripts/load_raw.py")
    logging.info("Raw load completed")

    os.system("python scripts/validate.py")
    logging.info("Validation completed")

    os.system("python scripts/transform.py")
    logging.info("Transformation completed")

    logging.info("Pipeline finished successfully")
    print("Pipeline executed successfully")

if __name__ == "__main__":
    run_pipeline()