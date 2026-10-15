"""Color-Coded Status Labels feature module.

This module provides utility functions and API endpoints for determining
color-coded status labels for assignments based on their due dates and
completion status.

Color coding:
- Orange: Upcoming assignments (not yet due and not completed)
- Red: Overdue assignments (past due and not completed)
- Green: Completed assignments
"""

from datetime import datetime, timezone
from flask import Blueprint, jsonify, request

blueprint = Blueprint("color_coded_status_labels", __name__, url_prefix="/api/status-labels")


def get_status_color(due_date, is_completed, current_time=None):
    """Determine the color code for an assignment based on its status.
    
    Args:
        due_date: datetime object or ISO format string representing the due date
        is_completed: boolean indicating if the assignment is completed
        current_time: optional datetime for testing; defaults to current UTC time
    
    Returns:
        str: Color code - 'green', 'orange', or 'red'
    """
    if current_time is None:
        current_time = datetime.now(timezone.utc)
    
    # Ensure current_time is timezone-aware
    if current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=timezone.utc)
    
    # Parse due_date if it's a string
    if isinstance(due_date, str):
        due_date = datetime.fromisoformat(due_date.replace('Z', '+00:00'))
    
    # Ensure due_date is timezone-aware
    if due_date.tzinfo is None:
        due_date = due_date.replace(tzinfo=timezone.utc)
    
    # Green for completed assignments
    if is_completed:
        return 'green'
    
    # Red for overdue assignments
    if current_time > due_date:
        return 'red'
    
    # Orange for upcoming assignments
    return 'orange'


def get_status_label(due_date, is_completed, current_time=None):
    """Get a human-readable status label for an assignment.
    
    Args:
        due_date: datetime object or ISO format string representing the due date
        is_completed: boolean indicating if the assignment is completed
        current_time: optional datetime for testing; defaults to current UTC time
    
    Returns:
        str: Status label - 'Completed', 'Overdue', or 'Upcoming'
    """
    color = get_status_color(due_date, is_completed, current_time)
    
    if color == 'green':
        return 'Completed'
    elif color == 'red':
        return 'Overdue'
    else:
        return 'Upcoming'


@blueprint.route("/color", methods=["POST"])
def get_color_for_assignment():
    """API endpoint to get the color code for an assignment.
    
    Request body:
        {
            "due_date": "2024-12-31T23:59:59Z",
            "is_completed": false,
            "current_time": "2024-12-01T00:00:00Z"  // optional
        }
    
    Response:
        {
            "color": "orange",
            "label": "Upcoming"
        }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    
    due_date = data.get("due_date")
    is_completed = data.get("is_completed")
    current_time = data.get("current_time")
    
    if due_date is None:
        return jsonify({"error": "due_date is required"}), 400
    
    if is_completed is None:
        return jsonify({"error": "is_completed is required"}), 400
    
    try:
        # Parse current_time if provided
        parsed_current_time = None
        if current_time:
            parsed_current_time = datetime.fromisoformat(current_time.replace('Z', '+00:00'))
        
        color = get_status_color(due_date, is_completed, parsed_current_time)
        label = get_status_label(due_date, is_completed, parsed_current_time)
        
        return jsonify({
            "color": color,
            "label": label
        }), 200
    
    except (ValueError, AttributeError) as e:
        return jsonify({"error": f"Invalid date format: {str(e)}"}), 400


@blueprint.route("/batch", methods=["POST"])
def get_colors_batch():
    """API endpoint to get color codes for multiple assignments.
    
    Request body:
        {
            "assignments": [
                {
                    "id": "assignment_1",
                    "due_date": "2024-12-31T23:59:59Z",
                    "is_completed": false
                },
                {
                    "id": "assignment_2",
                    "due_date": "2024-11-01T23:59:59Z",
                    "is_completed": true
                }
            ],
            "current_time": "2024-12-01T00:00:00Z"  // optional
        }
    
    Response:
        {
            "results": [
                {
                    "id": "assignment_1",
                    "color": "orange",
                    "label": "Upcoming"
                },
                {
                    "id": "assignment_2",
                    "color": "green",
                    "label": "Completed"
                }
            ]
        }
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body is required"}), 400
    
    assignments = data.get("assignments")
    current_time = data.get("current_time")
    
    if not assignments:
        return jsonify({"error": "assignments array is required"}), 400
    
    if not isinstance(assignments, list):
        return jsonify({"error": "assignments must be an array"}), 400
    
    try:
        # Parse current_time if provided
        parsed_current_time = None
        if current_time:
            parsed_current_time = datetime.fromisoformat(current_time.replace('Z', '+00:00'))
        
        results = []
        for assignment in assignments:
            assignment_id = assignment.get("id")
            due_date = assignment.get("due_date")
            is_completed = assignment.get("is_completed")
            
            if due_date is None or is_completed is None:
                results.append({
                    "id": assignment_id,
                    "error": "due_date and is_completed are required"
                })
                continue
            
            try:
                color = get_status_color(due_date, is_completed, parsed_current_time)
                label = get_status_label(due_date, is_completed, parsed_current_time)
                
                results.append({
                    "id": assignment_id,
                    "color": color,
                    "label": label
                })
            except (ValueError, AttributeError) as e:
                results.append({
                    "id": assignment_id,
                    "error": f"Invalid date format: {str(e)}"
                })
        
        return jsonify({"results": results}), 200
    
    except (ValueError, AttributeError) as e:
        return jsonify({"error": f"Invalid date format: {str(e)}"}), 400


@blueprint.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint for the color-coded status labels feature.
    
    Response:
        {
            "status": "healthy",
            "feature": "color_coded_status_labels"
        }
    """
    return jsonify({
        "status": "healthy",
        "feature": "color_coded_status_labels"
    }), 200
