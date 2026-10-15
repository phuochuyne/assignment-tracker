"""Overdue Assignment Highlighting feature module.

This module provides functionality to highlight overdue assignments in red color.
It checks assignment due dates against the current date and marks them as overdue.
"""

from datetime import datetime
from flask import Blueprint, jsonify, request
from sqlalchemy import text

from backend.core.db import get_engine

blueprint = Blueprint("overdue_assignment_highlighting", __name__, url_prefix="/api/overdue-assignments")


@blueprint.get("/check")
def check_overdue_assignments():
    """Check and return all overdue assignments with highlighting information.
    
    Returns:
        JSON response with list of overdue assignments and their highlighting status.
    """
    try:
        with get_engine().begin() as connection:
            # Query assignments that are past their due date
            query = text("""
                SELECT 
                    id,
                    title,
                    description,
                    due_date,
                    status,
                    CASE 
                        WHEN due_date < NOW() AND status != 'completed' THEN 'red'
                        ELSE 'default'
                    END as highlight_color,
                    CASE 
                        WHEN due_date < NOW() AND status != 'completed' THEN TRUE
                        ELSE FALSE
                    END as is_overdue
                FROM assignments
                WHERE status != 'completed'
                ORDER BY due_date ASC
            """)
            
            result = connection.execute(query)
            assignments = []
            
            for row in result.mappings():
                assignments.append({
                    "id": row["id"],
                    "title": row["title"],
                    "description": row["description"],
                    "due_date": row["due_date"].isoformat() if row["due_date"] else None,
                    "status": row["status"],
                    "highlight_color": row["highlight_color"],
                    "is_overdue": bool(row["is_overdue"])
                })
            
            return jsonify({
                "success": True,
                "assignments": assignments,
                "total_overdue": sum(1 for a in assignments if a["is_overdue"])
            }), 200
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@blueprint.get("/assignments/<int:assignment_id>/highlight")
def get_assignment_highlight_status(assignment_id):
    """Get the highlight status for a specific assignment.
    
    Args:
        assignment_id: The ID of the assignment to check.
        
    Returns:
        JSON response with highlighting information for the assignment.
    """
    try:
        with get_engine().begin() as connection:
            query = text("""
                SELECT 
                    id,
                    title,
                    due_date,
                    status,
                    CASE 
                        WHEN due_date < NOW() AND status != 'completed' THEN 'red'
                        ELSE 'default'
                    END as highlight_color,
                    CASE 
                        WHEN due_date < NOW() AND status != 'completed' THEN TRUE
                        ELSE FALSE
                    END as is_overdue,
                    TIMESTAMPDIFF(DAY, NOW(), due_date) as days_until_due
                FROM assignments
                WHERE id = :assignment_id
            """)
            
            result = connection.execute(query, {"assignment_id": assignment_id})
            row = result.mappings().first()
            
            if not row:
                return jsonify({
                    "success": False,
                    "error": "Assignment not found"
                }), 404
            
            return jsonify({
                "success": True,
                "assignment": {
                    "id": row["id"],
                    "title": row["title"],
                    "due_date": row["due_date"].isoformat() if row["due_date"] else None,
                    "status": row["status"],
                    "highlight_color": row["highlight_color"],
                    "is_overdue": bool(row["is_overdue"]),
                    "days_until_due": row["days_until_due"]
                }
            }), 200
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@blueprint.get("/summary")
def get_overdue_summary():
    """Get a summary of overdue assignments statistics.
    
    Returns:
        JSON response with summary statistics of overdue assignments.
    """
    try:
        with get_engine().begin() as connection:
            query = text("""
                SELECT 
                    COUNT(*) as total_assignments,
                    SUM(CASE WHEN due_date < NOW() AND status != 'completed' THEN 1 ELSE 0 END) as overdue_count,
                    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed_count,
                    SUM(CASE WHEN due_date >= NOW() AND status != 'completed' THEN 1 ELSE 0 END) as upcoming_count
                FROM assignments
            """)
            
            result = connection.execute(query)
            row = result.mappings().first()
            
            return jsonify({
                "success": True,
                "summary": {
                    "total_assignments": row["total_assignments"] or 0,
                    "overdue_count": row["overdue_count"] or 0,
                    "completed_count": row["completed_count"] or 0,
                    "upcoming_count": row["upcoming_count"] or 0,
                    "highlight_enabled": True
                }
            }), 200
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@blueprint.post("/bulk-check")
def bulk_check_overdue_status():
    """Check overdue status for multiple assignments by their IDs.
    
    Expects JSON body with:
        assignment_ids: List of assignment IDs to check
        
    Returns:
        JSON response with highlighting information for each assignment.
    """
    try:
        data = request.get_json()
        
        if not data or "assignment_ids" not in data:
            return jsonify({
                "success": False,
                "error": "assignment_ids is required"
            }), 400
        
        assignment_ids = data["assignment_ids"]
        
        if not isinstance(assignment_ids, list) or not assignment_ids:
            return jsonify({
                "success": False,
                "error": "assignment_ids must be a non-empty list"
            }), 400
        
        with get_engine().begin() as connection:
            # Create placeholders for IN clause
            placeholders = ",".join([f":id_{i}" for i in range(len(assignment_ids))])
            params = {f"id_{i}": aid for i, aid in enumerate(assignment_ids)}
            
            query = text(f"""
                SELECT 
                    id,
                    title,
                    due_date,
                    status,
                    CASE 
                        WHEN due_date < NOW() AND status != 'completed' THEN 'red'
                        ELSE 'default'
                    END as highlight_color,
                    CASE 
                        WHEN due_date < NOW() AND status != 'completed' THEN TRUE
                        ELSE FALSE
                    END as is_overdue
                FROM assignments
                WHERE id IN ({placeholders})
            """)
            
            result = connection.execute(query, params)
            assignments = []
            
            for row in result.mappings():
                assignments.append({
                    "id": row["id"],
                    "title": row["title"],
                    "due_date": row["due_date"].isoformat() if row["due_date"] else None,
                    "status": row["status"],
                    "highlight_color": row["highlight_color"],
                    "is_overdue": bool(row["is_overdue"])
                })
            
            return jsonify({
                "success": True,
                "assignments": assignments,
                "checked_count": len(assignments)
            }), 200
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
