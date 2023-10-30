import subprocess
import logging
from datetime import datetime

# Configure the logging settings
log_filename = f"runner_log_{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the list of Python scripts you want to run
scripts_to_run = ["alchemy.py", "KRUSE.py", "KRUSW.py", "Ontility.py", "Pytes.py", "renvu.py", "solar_electric.py", "Soligent.py", "saw.py", "trina.py", "tps.py"]

# Loop through the list and execute each script
for script in scripts_to_run:
    try:
        subprocess.check_call(["python", script])
        logging.info(f"{script} executed successfully.")
    except subprocess.CalledProcessError:
        logging.error(f"Error executing {script}.")

logging.info("All scripts have been executed.")
