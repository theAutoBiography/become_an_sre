from flask import Flask
import logging
import random
import time
from threading import Thread

app = Flask(__name__)

# Configure logging to store logs in "day1app.log"
logging.basicConfig(filename='day1app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_log_message():
  """Generates a random log message mimicking a production system."""
  log_levels = ["INFO", "WARNING", "ERROR"]
  log_level = random.choice(log_levels)
  
  actions = ["user login", "file upload", "database query", "payment processed", 
             "page accessed", "API request", "cache miss", "background job started"]
  action = random.choice(actions)

  statuses = ["successful", "failed", "delayed", "timeout"]
  status = random.choice(statuses) if log_level != "INFO" else ""

  user_ids = range(1, 101)  # Simulate 100 users
  user_id = random.choice(user_ids)

  # Define error codes for all levels
  error_codes = {
      "user login": {
          "INFO": ["LOGIN_SUCCESS"],
          "WARNING": ["LOGIN_FAILED_ATTEMPT"],
          "ERROR": ["LOGIN_INVALID_CREDS", "LOGIN_ACCOUNT_LOCKED"]
      },
      "file upload": {
          "INFO": ["FILE_UPLOAD_SUCCESS"],
          "WARNING": ["FILE_UPLOAD_LARGE_FILE"],
          "ERROR": ["FILE_UPLOAD_ERR", "FILE_SIZE_ERR", "FILE_TYPE_ERR"]
      },
      "database query": {
          "INFO": ["DB_QUERY_SUCCESS"],
          "WARNING": ["DB_QUERY_SLOW"],
          "ERROR": ["DB_CONN_ERR", "DB_QUERY_ERR", "DB_TIMEOUT"]
      },
      "payment processed": {
          "INFO": ["PAYMENT_SUCCESS"],
          "WARNING": ["PAYMENT_DELAYED"],
          "ERROR": ["PAYMENT_AUTH_ERR", "PAYMENT_GATEWAY_ERR", "PAYMENT_FAILED"]
      },
      "page accessed": {
          "INFO": ["PAGE_ACCESS_SUCCESS"],
          "WARNING": ["PAGE_ACCESS_SLOW"],
          "ERROR": ["PAGE_ACCESS_ERR", "PAGE_NOT_FOUND"]
      },
      "API request": {
          "INFO": ["API_REQUEST_SUCCESS"],
          "WARNING": ["API_REQUEST_RATE_LIMITED"],
          "ERROR": ["API_REQUEST_ERR", "API_REQUEST_TIMEOUT"]
      },
      "cache miss": {
          "INFO": ["CACHE_MISS"],
          "WARNING": ["CACHE_MISS_HIGH_RATE"],
          "ERROR": ["CACHE_SERVER_ERR"]
      },
      "background job started": {
          "INFO": ["JOB_STARTED"],
          "WARNING": ["JOB_DELAYED"],
          "ERROR": ["JOB_FAILED"]
      }
  }

  error_code = random.choice(error_codes[action][log_level])
  message = f"{log_level}: User {user_id} - {action} {status} ({error_code})"

  return message

def log_generator():
  """Generates logs in the background."""
  while True:
    log_message = generate_log_message()
    logging.info(log_message)
    time.sleep(random.uniform(0.5, 3)) 

@app.route('/')
def index():
  return "Generating logs in the background..."

# Start the log generator in a separate thread
if __name__ == '__main__':
  thread = Thread(target=log_generator)
  thread.daemon = True  # Allow the app to exit even if the thread is running
  thread.start()
  app.run(debug=True)