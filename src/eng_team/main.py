import sys
import warnings

from datetime import datetime
import textwrap

from eng_team.crew import EngTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


requirements = textwrap.dedent("""\
A system to manage book lending for a small library.
The system should be able to add new books to the inventory (title, author, ISBN).
The system should be able to register new library members (name, member_id).
The system should allow a member to check out a book.
A due date should be set for 14 days from checkout.
The system should allow a member to return a book.
The system should be able to list all books currently checked out by a specific member.
The system should be able to list all available books in the inventory.
The system should calculate overdue fines for books returned after their due date (e.g., $0.25 per day).
The system must prevent a member from checking out a book that is already on loan.
The system must prevent a member from checking out more than 5 books at one time.
The system should be able to report a member's total outstanding fines.
""").strip()
module_name = "library.py"
class_name = "LibrarySystem"


def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'module_name': module_name,
        'class_name': class_name
    }

    # Create and run the crew
    result = EngTeam().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        EngTeam().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        EngTeam().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        EngTeam().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = EngTeam().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
