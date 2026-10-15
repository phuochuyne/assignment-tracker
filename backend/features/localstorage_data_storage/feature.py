"""LocalStorage Data Storage feature module.

This module provides CRUD operations for assignments stored in MySQL,
designed to work with a frontend that uses LocalStorage for client-side persistence.
"""

from datetime import datetime
from uuid import uuid4

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from backend.core.db import get_engine

blueprint = Blueprint(
    "capability_localstorage_data_storage_c1936286",
    __name__,
    url_prefix="/api/capability_localstorage_data_storage_c1936286"
)


def _validate_assignment_data(data, require_all=True):
    """Validate assignment data fields.
    
    Args:
        data: Dictionary containing assignment data
        require_all: If True, all required fields must be present
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    required_fields = ["title", "unit_code", "due_date", "completed"]
    
    if require_all:
        for field in required_fields:
            if field not in data:
                return False, f"Missing required field: {field}"
    
    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            return False, "Title must be a non-empty string"
        if len(data["title"]) > 500:
            return False, "Title must not exceed 500 characters"
    
    if "unit_code" in data:
        if not isinstance(data["unit_code"], str) or not data["unit_code"].strip():
            return False, "Unit code must be a non-empty string"
        if len(data["unit_code"]) > 50:
            return False, "Unit code must not exceed 50 characters"
    
    if "due_date" in data:
        if not isinstance(data["due_date"], str):
            return False, "Due date must be a string in YYYY-MM-DD format"
        try:
            datetime.strptime(data["due_date"], "%Y-%m-%d")
        except ValueError:
            return False, "Due date must be in YYYY-MM-DD format"
    
    if "completed" in data:
        if not isinstance(data["completed"], bool):
            return False, "Completed must be a boolean"
    
    return True, None


def _format_assignment(row):
    """Format a database row as an assignment dictionary.
    
    Args:
        row: Database row mapping
        
    Returns:
        Dictionary with formatted assignment data
    """
    return {
        "id": row["id"],
        "title": row["title"],
        "unit_code": row["unit_code"],
        "due_date": row["due_date"].strftime("%Y-%m-%d") if hasattr(row["due_date"], "strftime") else row["due_date"],
        "completed": bool(row["completed"]),
        "created_at": row["created_at"].isoformat() if hasattr(row["created_at"], "isoformat") else row["created_at"],
        "updated_at": row["updated_at"].isoformat() if hasattr(row["updated_at"], "isoformat") else row["updated_at"]
    }


@blueprint.post("/assignments")
def save_assignment():
    """Persists a new or updated assignment to the database.
    
    Returns:
        JSON response with the saved assignment data
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error": "INVALID_REQUEST",
                "message": "Request validation failed: missing or invalid required fields"
            }), 400
        
        # Validate required fields
        is_valid, error_message = _validate_assignment_data(data, require_all=True)
        if not is_valid:
            return jsonify({
                "error": "INVALID_REQUEST",
                "message": f"Request validation failed: {error_message}"
            }), 400
        
        # Generate UUID if not provided
        assignment_id = data.get("id", str(uuid4()))
        
        # Validate UUID format if provided
        if "id" in data:
            try:
                # Basic UUID format validation
                if not isinstance(data["id"], str) or len(data["id"]) != 36:
                    raise ValueError("Invalid UUID format")
            except (ValueError, AttributeError):
                return jsonify({
                    "error": "INVALID_REQUEST",
                    "message": "Request validation failed: invalid UUID format"
                }), 400
        
        now = datetime.utcnow()
        
        with get_engine().begin() as connection:
            # Insert the assignment
            insert_query = text("""
                INSERT INTO f_c1936286__assignments 
                (id, title, unit_code, due_date, completed, created_at, updated_at)
                VALUES (:id, :title, :unit_code, :due_date, :completed, :created_at, :updated_at)
            """)
            
            connection.execute(insert_query, {
                "id": assignment_id,
                "title": data["title"],
                "unit_code": data["unit_code"],
                "due_date": data["due_date"],
                "completed": data["completed"],
                "created_at": now,
                "updated_at": now
            })
            
            # Retrieve the inserted assignment
            select_query = text("""
                SELECT id, title, unit_code, due_date, completed, created_at, updated_at
                FROM f_c1936286__assignments
                WHERE id = :id
            """)
            
            result = connection.execute(select_query, {"id": assignment_id})
            row = result.mappings().one()
            
            return jsonify(_format_assignment(row)), 201
    
    except Exception as e:
        return jsonify({
            "error": "STORAGE_ERROR",
            "message": "Failed to save assignment to LocalStorage"
        }), 500


@blueprint.get("/assignments")
def load_assignments():
    """Retrieves all assignments from the database.
    
    Returns:
        JSON response with array of all assignments
    """
    try:
        with get_engine().connect() as connection:
            query = text("""
                SELECT id, title, unit_code, due_date, completed, created_at, updated_at
                FROM f_c1936286__assignments
                ORDER BY due_date ASC, created_at DESC
            """)
            
            result = connection.execute(query)
            rows = result.mappings().all()
            
            assignments = [_format_assignment(row) for row in rows]
            
            return jsonify({"assignments": assignments}), 200
    
    except Exception as e:
        return jsonify({
            "error": "STORAGE_ERROR",
            "message": "Failed to load assignments from LocalStorage"
        }), 500


@blueprint.put("/assignments/<id>")
def update_assignment(id):
    """Updates an existing assignment in the database.
    
    Args:
        id: UUID of the assignment to update
        
    Returns:
        JSON response with the updated assignment data
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({
                "error": "INVALID_REQUEST",
                "message": "Request validation failed: missing or invalid required fields"
            }), 400
        
        # Validate required fields
        is_valid, error_message = _validate_assignment_data(data, require_all=True)
        if not is_valid:
            return jsonify({
                "error": "INVALID_REQUEST",
                "message": f"Request validation failed: {error_message}"
            }), 400
        
        now = datetime.utcnow()
        
        with get_engine().begin() as connection:
            # Check if assignment exists
            check_query = text("""
                SELECT id FROM f_c1936286__assignments WHERE id = :id
            """)
            result = connection.execute(check_query, {"id": id})
            if result.mappings().first() is None:
                return jsonify({
                    "error": "ASSIGNMENT_NOT_FOUND",
                    "message": "Assignment with the specified ID does not exist"
                }), 404
            
            # Update the assignment
            update_query = text("""
                UPDATE f_c1936286__assignments
                SET title = :title,
                    unit_code = :unit_code,
                    due_date = :due_date,
                    completed = :completed,
                    updated_at = :updated_at
                WHERE id = :id
            """)
            
            connection.execute(update_query, {
                "id": id,
                "title": data["title"],
                "unit_code": data["unit_code"],
                "due_date": data["due_date"],
                "completed": data["completed"],
                "updated_at": now
            })
            
            # Retrieve the updated assignment
            select_query = text("""
                SELECT id, title, unit_code, due_date, completed, created_at, updated_at
                FROM f_c1936286__assignments
                WHERE id = :id
            """)
            
            result = connection.execute(select_query, {"id": id})
            row = result.mappings().one()
            
            return jsonify(_format_assignment(row)), 200
    
    except Exception as e:
        # Check if it's a 404 error we already returned
        if hasattr(e, 'code') and e.code == 404:
            raise
        return jsonify({
            "error": "STORAGE_ERROR",
            "message": "Failed to update assignment in LocalStorage"
        }), 500


@blueprint.delete("/assignments/<id>")
def delete_assignment(id):
    """Removes an assignment from the database.
    
    Args:
        id: UUID of the assignment to delete
        
    Returns:
        JSON response confirming deletion
    """
    try:
        with get_engine().begin() as connection:
            # Check if assignment exists
            check_query = text("""
                SELECT id FROM f_c1936286__assignments WHERE id = :id
            """)
            result = connection.execute(check_query, {"id": id})
            if result.mappings().first() is None:
                return jsonify({
                    "error": "ASSIGNMENT_NOT_FOUND",
                    "message": "Assignment with the specified ID does not exist"
                }), 404
            
            # Delete the assignment
            delete_query = text("""
                DELETE FROM f_c1936286__assignments WHERE id = :id
            """)
            
            connection.execute(delete_query, {"id": id})
            
            return jsonify({
                "success": True,
                "id": id
            }), 200
    
    except Exception as e:
        # Check if it's a 404 error we already returned
        if hasattr(e, 'code') and e.code == 404:
            raise
        return jsonify({
            "error": "STORAGE_ERROR",
            "message": "Failed to delete assignment from LocalStorage"
        }), 500
