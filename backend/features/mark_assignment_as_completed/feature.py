"""Mark Assignment as Completed feature module."""

from datetime import datetime
from uuid import uuid4

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from backend.core.db import get_engine

blueprint = Blueprint(
    "capability_mark_assignment_as_completed_1a7f53a5",
    __name__,
    url_prefix="/api/capability_mark_assignment_as_completed_1a7f53a5"
)


@blueprint.put("/assignments/<assignment_id>/completion")
def toggle_assignment_completion(assignment_id):
    """Toggle the completion status of an assignment."""
    data = request.get_json()
    
    if data is None or "is_completed" not in data:
        return jsonify({
            "code": "INVALID_REQUEST",
            "message": "Request body must include is_completed boolean field"
        }), 400
    
    if not isinstance(data["is_completed"], bool):
        return jsonify({
            "code": "INVALID_REQUEST",
            "message": "Request body must include is_completed boolean field"
        }), 400
    
    is_completed = data["is_completed"]
    
    try:
        with get_engine().begin() as connection:
            # Check if completion record exists
            check_query = text("""
                SELECT id, is_completed, completed_at, updated_at
                FROM f_1a7f53a5__assignment_completion
                WHERE assignment_id = :assignment_id
            """)
            result = connection.execute(
                check_query,
                {"assignment_id": assignment_id}
            )
            existing = result.mappings().first()
            
            now = datetime.utcnow()
            completed_at = now if is_completed else None
            
            if existing:
                # Update existing record
                update_query = text("""
                    UPDATE f_1a7f53a5__assignment_completion
                    SET is_completed = :is_completed,
                        completed_at = :completed_at,
                        updated_at = :updated_at
                    WHERE assignment_id = :assignment_id
                """)
                connection.execute(
                    update_query,
                    {
                        "is_completed": is_completed,
                        "completed_at": completed_at,
                        "updated_at": now,
                        "assignment_id": assignment_id
                    }
                )
                record_id = existing["id"]
            else:
                # Create new record
                record_id = str(uuid4())
                insert_query = text("""
                    INSERT INTO f_1a7f53a5__assignment_completion
                    (id, assignment_id, is_completed, completed_at, updated_at)
                    VALUES (:id, :assignment_id, :is_completed, :completed_at, :updated_at)
                """)
                connection.execute(
                    insert_query,
                    {
                        "id": record_id,
                        "assignment_id": assignment_id,
                        "is_completed": is_completed,
                        "completed_at": completed_at,
                        "updated_at": now
                    }
                )
            
            return jsonify({
                "id": record_id,
                "assignment_id": assignment_id,
                "is_completed": is_completed,
                "completed_at": completed_at.isoformat() if completed_at else None,
                "updated_at": now.isoformat()
            }), 200
            
    except Exception as e:
        return jsonify({
            "code": "INTERNAL_ERROR",
            "message": "An unexpected error occurred while updating completion status"
        }), 500


@blueprint.get("/assignments/<assignment_id>/completion")
def get_assignment_completion(assignment_id):
    """Retrieve the current completion status for a specific assignment."""
    try:
        with get_engine().connect() as connection:
            query = text("""
                SELECT id, assignment_id, is_completed, completed_at, updated_at
                FROM f_1a7f53a5__assignment_completion
                WHERE assignment_id = :assignment_id
            """)
            result = connection.execute(
                query,
                {"assignment_id": assignment_id}
            )
            record = result.mappings().first()
            
            if record:
                return jsonify({
                    "id": record["id"],
                    "assignment_id": record["assignment_id"],
                    "is_completed": bool(record["is_completed"]),
                    "completed_at": record["completed_at"].isoformat() if record["completed_at"] else None,
                    "updated_at": record["updated_at"].isoformat() if record["updated_at"] else None
                }), 200
            else:
                # No record exists, return default state
                return jsonify({
                    "id": None,
                    "assignment_id": assignment_id,
                    "is_completed": False,
                    "completed_at": None,
                    "updated_at": None
                }), 200
                
    except Exception as e:
        return jsonify({
            "code": "INTERNAL_ERROR",
            "message": "An unexpected error occurred while retrieving completion status"
        }), 500


@blueprint.get("/assignments/completions")
def get_all_completions():
    """Retrieve completion status for all assignments."""
    try:
        with get_engine().connect() as connection:
            query = text("""
                SELECT id, assignment_id, is_completed, completed_at, updated_at
                FROM f_1a7f53a5__assignment_completion
            """)
            result = connection.execute(query)
            records = result.mappings().all()
            
            completions = []
            for record in records:
                completions.append({
                    "id": record["id"],
                    "assignment_id": record["assignment_id"],
                    "is_completed": bool(record["is_completed"]),
                    "completed_at": record["completed_at"].isoformat() if record["completed_at"] else None,
                    "updated_at": record["updated_at"].isoformat() if record["updated_at"] else None
                })
            
            return jsonify({
                "completions": completions
            }), 200
            
    except Exception as e:
        return jsonify({
            "code": "INTERNAL_ERROR",
            "message": "An unexpected error occurred while retrieving completion statuses"
        }), 500
