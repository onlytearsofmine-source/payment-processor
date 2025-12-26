import logging
import json
import os
import uuid

from datetime import datetime

logger = logging.getLogger(__name__)

def generate_unique_id():
    return str(uuid.uuid4())

def is_json_valid(data):
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False

def get_current_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_user_agent():
    return os.environ.get('HTTP_USER_AGENT', 'Unknown')

def generate_payment_id():
    return f"PP-{generate_unique_id()}"