from todoist_api_python.api import TodoistAPI

# REPLACE 'your_token_here' with your actual API token
api = TodoistAPI("https://ext.todoist.com/export/ical/todoist?user_id=54059731&ical_token=c84b6ce0941643fbd6063d240b0ab6e2b7899811172c45753f0dc27ee5bf1ebe&r_factor=5707")

chapters = [
    "Real Numbers", "Polynomials", "Pair of Linear Equations in Two Variables",
    "Quadratic Equations", "Arithmetic Progressions", "Triangles",
    "Coordinate Geometry", "Introduction to Trigonometry", "Some Applications of Trigonometry",
    "Circles", "Areas Related to Circles", "Surface Areas and Volumes",
    "Statistics", "Probability"
]

try:
    # 1. Create the main parent task in the Inbox
    parent_task = api.add_task(content="Maths Exam")
    
    # 2. Add each chapter as a subtask
    for chapter in chapters:
        api.add_task(
            content=chapter,
            parent_id=parent_task.id
        )
    print("Successfully added Maths Exam and all subtasks!")
    
except Exception as error:
    print(f"An error occurred: {error}")