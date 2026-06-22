import requests
import json
from time import sleep
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# API key provided by the user
API_KEY = "cc8f6f7fe7e79680411db80687c286a49c811021"
BASE_URL = "https://api.todoist.com/rest/v2/tasks"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
MAX_RETRIES = 3

# Set up session with retry strategy
session = requests.Session()
retries = Retry(total=MAX_RETRIES, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))

# Function to make API request with retries
def make_request(method, url, headers=None, data=None, retries=0):
    try:
        response = session.request(method, url, headers=headers, data=data, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise Exception("Invalid API key. Please check or provide a new Todoist API key.")
        raise
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        if retries < MAX_RETRIES:
            sleep(2 ** retries)  # Exponential backoff
            return make_request(method, url, headers=headers, data=data, retries=retries + 1)
        raise

# Fetch all tasks to find "Study Hindi" and "Kshitij"
try:
    response = make_request("GET", BASE_URL, headers=HEADERS)
    tasks = response.json()
except Exception as e:
    print(f"Error fetching tasks: {str(e)}")
    exit()

hindi_task_id = None
kshitij_task_id = None

# Find "Study Hindi" and "Kshitij"
for task in tasks:
    if task["content"] == "Study Hindi" and not task.get("parent_id"):
        hindi_task_id = task["id"]
    if task["content"] == "Kshitij" and task.get("parent_id"):
        kshitij_task_id = task["id"]

# If "Study Hindi" doesn't exist, create it
if not hindi_task_id:
    hindi_data = {"content": "Study Hindi"}
    response = make_request("POST", BASE_URL, headers=HEADERS, data=json.dumps(hindi_data))
    hindi_task = response.json()
    hindi_task_id = hindi_task["id"]

# If "Kshitij" doesn't exist, create it under "Study Hindi"
if not kshitij_task_id:
    kshitij_data = {"content": "Kshitij", "parent_id": hindi_task_id}
    response = make_request("POST", BASE_URL, headers=HEADERS, data=json.dumps(kshitij_data))
    kshitij_task = response.json()
    kshitij_task_id = kshitij_task["id"]

# Add Kshitij chapters as sub-subtasks with chapter numbers
kshitij_chapters = [
    "Chapter 1: सूरदास – सूर के पद",
    "Chapter 2: तुलसीदास – राम-लक्ष्मण-परशुराम संवाद",
    "Chapter 3: मंगलेश डबराल – संगतकार",
    "Chapter 4: सियारामशरण गुप्त – आत्मत्राण",
    "Chapter 5: सुमित्रानंदन पंत – परवत प्रदेश में पावस",
    "Chapter 6: रवींद्रनाथ ठाकुर – आत्मकथन",
    "Chapter 7: प्रेमचंद – बड़े भाई साहब",
    "Chapter 8: सीताराम सेकसरिया – डायरी का एक पन्ना",
    "Chapter 9: तताँरा-वामीरो कथा"
]
for chapter in kshitij_chapters:
    chapter_data = {"content": chapter, "parent_id": kshitij_task_id}
    make_request("POST", BASE_URL, headers=HEADERS, data=json.dumps(chapter_data))

print("Successfully added Kshitij chapters under 'Study Hindi' in Todoist Inbox!")