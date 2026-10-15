"""Automatic Deadline Sorting feature module.

This module provides functionality to automatically sort assignments by due date
to help students prioritize tasks.
"""

from flask import Blueprint, jsonify, request
from sqlalchemy import text
from backend.core.db import get_engine

blueprint = Blueprint("automatic_deadline_sorting", __name__, url_prefix="/api/assignments")


@blueprint.get("/sorted")
def get_sorted_assignments():
    """Get assignments sorted by due date (earliest first).
    
    Query parameters:
        - student_id (optional): Filter assignments for a specific student
        - include_completed (optional): Include completed assignments (default: false)
    
    Returns:
        JSON response with sorted assignments list
    """
    student_id = request.args.get("student_id", type=int)
    include_completed = request.args.get("include_completed", "false").lower() == "true"
    
    try:
        with get_engine().connect() as connection:
            # Build the query dynamically based on filters
            query = """
                SELECT 
                    a.id,
                    a.title,
                    a.description,
                    a.due_date,
                    a.status,
                    a.student_id,
                    a.course_id,
                    a.created_at,
                    a.updated_at
                FROM assignments a
                WHERE 1=1
            """
            params = {}
            
            if student_id is not None:
                query += " AND a.student_id = :student_id"
                params["student_id"] = student_id
            
            if not include_completed:
                query += " AND a.status != 'completed'"
            
            # Sort by due date (NULL values last), then by created date
            query += " ORDER BY a.due_date IS NULL, a.due_date ASC, a.created_at ASC"
            
            result = connection.execute(text(query), params)
            assignments = []
            
            for row in result.mappings():
                assignment = {
                    "id": row["id"],
                    "title": row["title"],
                    "description": row["description"],
                    "due_date": row["due_date"].isoformat() if row["due_date"] else None,
                    "status": row["status"],
                    "student_id": row["student_id"],
                    "course_id": row["course_id"],
                    "created_at": row["created_at"].isoformat() if row["created_at"] else None,
                    "updated_at": row["updated_at"].isoformat() if row["updated_at"] else None,
                }
                assignments.append(assignment)
            
            return jsonify({
                "success": True,
                "assignments": assignments,
                "count": len(assignments),
                "sorted_by": "due_date"
            }), 200
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Failed to retrieve sorted assignments",
            "message": str(e)
        }), 500


@blueprint.get("/upcoming")
def get_upcoming_assignments():
    """Get upcoming assignments sorted by due date.
    
    Only returns assignments with future due dates, sorted by earliest first.
    
    Query parameters:
        - student_id (optional): Filter assignments for a specific student
        - limit (optional): Maximum number of assignments to return (default: 10)
    
    Returns:
        JSON response with upcoming assignments
    """
    student_id = request.args.get("student_id", type=int)
    limit = request.args.get("limit", default=10, type=int)
    
    try:
        with get_engine().connect() as connection:
            query = """
                SELECT 
                    a.id,
                    a.title,
                    a.description,
                    a.due_date,
                    a.status,
                    a.student_id,
                    a.course_id,
                    a.created_at,
                    a.updated_at
                FROM assignments a
                WHERE a.due_date >= NOW()
                AND a.status != 'completed'
            """
            params = {"limit": limit}
            
            if student_id is not None:
                query += " AND a.student_id = :student_id"
                params["student_id"] = student_id
            
            query += " ORDER BY a.due_date ASC LIMIT :limit"
            
            result = connection.execute(text(query), params)
            assignments = []
            
            for row in result.mappings():
                assignment = {
                    "id": row["id"],
                    "title": row["title"],
                    "description": row["description"],
                    "due_date": row["due_date"].isoformat() if row["due_date"] else None,
                    "status": row["status"],
                    "student_id": row["student_id"],
                    "course_id": row["course_id"],
                    "created_at": row["created_at"].isoformat() if row["created_at"] else None,
                    "updated_at": row["updated_at"].isoformat() if row["updated_at"] else None,
                }
                assignments.append(assignment)
            
            return jsonify({
                "success": True,
                "assignments": assignments,
                "count": len(assignments),
                "sorted_by": "due_date"
            }), 200
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Failed to retrieve upcoming assignments",
            "message": str(e)
        }), 500


@blueprint.get("/overdue")
def get_overdue_assignments():
    """Get overdue assignments sorted by due date.
    
    Returns incomplete assignments with past due dates, sorted by most overdue first.
    
    Query parameters:
        - student_id (optional): Filter assignments for a specific student
    
    Returns:
        JSON response with overdue assignments
    """
    student_id = request.args.get("student_id", type=int)
    
    try:
        with get_engine().connect() as connection:
            query = """
                SELECT 
                    a.id,
                    a.title,
                    a.description,
                    a.due_date,
                    a.status,
                    a.student_id,
                    a.course_id,
                    a.created_at,
                    a.updated_at,
                    DATEDIFF(NOW(), a.due_date) as days_overdue
                FROM assignments a
                WHERE a.due_date < NOW()
                AND a.status != 'completed'
            """
            params = {}
            
            if student_id is not None:
                query += " AND a.student_id = :student_id"
                params["student_id"] = student_id
            
            query += " ORDER BY a.due_date ASC"
            
            result = connection.execute(text(query), params)
            assignments = []
            
            for row in result.mappings():
                assignment = {
                    "id": row["id"],
                    "title": row["title"],
                    "description": row["description"],
                    "due_date": row["due_date"].isoformat() if row["due_date"] else None,
                    "status": row["status"],
                    "student_id": row["student_id"],
                    "course_id": row["course_id"],
                    "created_at": row["created_at"].isoformat() if row["created_at"] else None,
                    "updated_at": row["updated_at"].isoformat() if row["updated_at"] else None,
                    "days_overdue": row["days_overdue"]
                }
                assignments.append(assignment)
            
            return jsonify({
                "success": True,
                "assignments": assignments,
                "count": len(assignments),
                "sorted_by": "due_date"
            }), 200
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Failed to retrieve overdue assignments",
            "message": str(e)
        }), 500
