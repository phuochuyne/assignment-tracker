"""Add Assignment feature module.

This module implements the capability for students to add assignments by entering
a title, unit code, and due date, and retrieve all assignments.
"""

from datetime import datetime
from uuid import uuid4

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from backend.core.db import get_engine

blueprint = Blueprint("capability_add_assignment_622b64dc", __name__)


@blueprint.post("/api/capability_add_assignment_622b64dc/assignments")
def create_assignment():
    """Create a new assignment.
    
    Accepts assignment data (title, unit code, due date) from the student,
    validates the input, generates a unique ID and timestamp, persists the
    assignment record to the database, and returns the created assignment.
    """
    data = request.get_json()
    
    # Validate required fields
    if not data:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Invalid input data"
            }
        }), 400
    
    title = data.get("title", "").strip() if isinstance(data.get("title"), str) else ""
    unit_code = data.get("unit_code", "").strip() if isinstance(data.get("unit_code"), str) else ""
    due_date = data.get("due_date", "").strip() if isinstance(data.get("due_date"), str) else ""
    
    # Validate title
    if not title or len(title) < 1 or len(title) > 500:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Invalid input data"
            }
        }), 400
    
    # Validate unit_code
    if not unit_code or len(unit_code) < 1 or len(unit_code) > 50:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Invalid input data"
            }
        }), 400
    
    # Validate due_date format (ISO 8601 date: YYYY-MM-DD)
    if not due_date:
        return jsonify({
            "error": {
                "code": "VALIDATION_ERROR",
                "message": "Invalid input data"
            }
        }), 400
    
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return jsonify({
            "error": {
                "code": "INVALID_DATE_FORMAT",
                "message": "Due date must be in YYYY-MM-DD format"
            }
        }), 400
    
    # Generate unique ID and timestamp
    assignment_id = str(uuid4())
    created_at = datetime.utcnow()
    
    # Persist to database
    try:
        with get_engine().begin() as connection:
            connection.execute(
                text("""
                    INSERT INTO f_622b64dc__assignments 
                    (id, title, unit_code, due_date, created_at)
                    VALUES (:id, :title, :unit_code, :due_date, :created_at)
                """),
                {
                    "id": assignment_id,
                    "title": title,
                    "unit_code": unit_code,
                    "due_date": parsed_date,
                    "created_at": created_at
                }
            )
    except Exception:
        return jsonify({
            "error": {
                "code": "DATABASE_ERROR",
                "message": "Failed to save assignment"
            }
        }), 500
    
    # Return created assignment
    return jsonify({
        "id": assignment_id,
        "title": title,
        "unit_code": unit_code,
        "due_date": due_date,
        "created_at": created_at.isoformat() + "Z"
    }), 201


@blueprint.get("/api/capability_add_assignment_622b64dc/assignments")
def get_assignments():
    """Retrieve all assignments.
    
    Retrieves all assignment records from the database to display on the
    dashboard after an assignment is added.
    """
    try:
        with get_engine().connect() as connection:
            result = connection.execute(
                text("""
                    SELECT id, title, unit_code, due_date, created_at
                    FROM f_622b64dc__assignments
                    ORDER BY created_at DESC
                """)
            )
            rows = result.mappings().all()
    except Exception:
        return jsonify({
            "error": {
                "code": "DATABASE_ERROR",
                "message": "Failed to retrieve assignments"
            }
        }), 500
    
    assignments = []
    for row in rows:
        assignment = {
            "id": row["id"],
            "title": row["title"],
            "unit_code": row["unit_code"],
            "due_date": row["due_date"].isoformat(),
            "created_at": row["created_at"].isoformat() + "Z"
        }
        assignments.append(assignment)
    
    return jsonify({
        "assignments": assignments
    }), 200
