"""Assignment Completion Tracking feature module."""

import uuid
from datetime import datetime

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from backend.core.db import get_engine

blueprint = Blueprint(
    "capability_assignment_completion_tracking_19f07be9",
    __name__,
    url_prefix="/api/capability_assignment_completion_tracking_19f07be9"
)


def _serialize_completion_record(row):
    """Serialize a completion record row to a dictionary."""
    return {
        "id": row["id"],
        "assignment_id": row["assignment_id"],
        "is_completed": bool(row["is_completed"]),
        "completed_at": row["completed_at"].isoformat() if row["completed_at"] else None,
        "created_at": row["created_at"].isoformat(),
        "updated_at": row["updated_at"].isoformat()
    }


@blueprint.get("/assignments/<assignment_id>/completion")
def get_assignment_completion_status(assignment_id):
    """Retrieves the completion status for a specific assignment to display whether it is completed or unfinished."""
    query = text("""
        SELECT id, assignment_id, is_completed, completed_at, created_at, updated_at
        FROM f_19f07be9__assignment_completion
        WHERE assignment_id = :assignment_id
    """)
    
    with get_engine().connect() as connection:
        result = connection.execute(query, {"assignment_id": assignment_id})
        row = result.mappings().first()
        
        if not row:
            return jsonify({"error": "Assignment completion record not found"}), 404
        
        return jsonify(_serialize_completion_record(row)), 200


@blueprint.get("/assignments/completion")
def get_all_completion_statuses():
    """Retrieves completion status for all assignments to enable the dashboard to display which assignments are completed versus unfinished."""
    query = text("""
        SELECT id, assignment_id, is_completed, completed_at, created_at, updated_at
        FROM f_19f07be9__assignment_completion
        ORDER BY created_at DESC
    """)
    
    with get_engine().connect() as connection:
        result = connection.execute(query)
        rows = result.mappings().all()
        
        completions = [_serialize_completion_record(row) for row in rows]
        
        return jsonify({"completions": completions}), 200


@blueprint.post("/assignments/<assignment_id>/completion")
def create_completion_record(assignment_id):
    """Creates a new completion tracking record when an assignment is added, initializing it as unfinished."""
    data = request.get_json() or {}
    
    # Validate that assignment_id in path matches body if provided
    if "assignment_id" in data and data["assignment_id"] != assignment_id:
        return jsonify({"error": "Assignment ID mismatch"}), 400
    
    # Check if record already exists
    check_query = text("""
        SELECT id FROM f_19f07be9__assignment_completion
        WHERE assignment_id = :assignment_id
    """)
    
    with get_engine().begin() as connection:
        result = connection.execute(check_query, {"assignment_id": assignment_id})
        existing = result.mappings().first()
        
        if existing:
            return jsonify({"error": "Completion record already exists for this assignment"}), 409
        
        # Create new record
        record_id = str(uuid.uuid4())
        now = datetime.utcnow()
        
        insert_query = text("""
            INSERT INTO f_19f07be9__assignment_completion
            (id, assignment_id, is_completed, completed_at, created_at, updated_at)
            VALUES (:id, :assignment_id, :is_completed, :completed_at, :created_at, :updated_at)
        """)
        
        connection.execute(insert_query, {
            "id": record_id,
            "assignment_id": assignment_id,
            "is_completed": False,
            "completed_at": None,
            "created_at": now,
            "updated_at": now
        })
        
        # Fetch the created record
        select_query = text("""
            SELECT id, assignment_id, is_completed, completed_at, created_at, updated_at
            FROM f_19f07be9__assignment_completion
            WHERE id = :id
        """)
        
        result = connection.execute(select_query, {"id": record_id})
        row = result.mappings().one()
        
        return jsonify(_serialize_completion_record(row)), 201


@blueprint.patch("/assignments/<assignment_id>/completion")
def update_completion_status(assignment_id):
    """Updates the completion status of an assignment when a student marks it as completed or reverts it to unfinished."""
    data = request.get_json() or {}
    
    if "is_completed" not in data:
        return jsonify({"error": "is_completed field is required"}), 400
    
    is_completed = data["is_completed"]
    
    if not isinstance(is_completed, bool):
        return jsonify({"error": "is_completed must be a boolean"}), 400
    
    # Check if record exists
    check_query = text("""
        SELECT id FROM f_19f07be9__assignment_completion
        WHERE assignment_id = :assignment_id
    """)
    
    with get_engine().begin() as connection:
        result = connection.execute(check_query, {"assignment_id": assignment_id})
        existing = result.mappings().first()
        
        if not existing:
            return jsonify({"error": "Assignment completion record not found"}), 404
        
        # Update the record
        now = datetime.utcnow()
        completed_at = now if is_completed else None
        
        update_query = text("""
            UPDATE f_19f07be9__assignment_completion
            SET is_completed = :is_completed,
                completed_at = :completed_at,
                updated_at = :updated_at
            WHERE assignment_id = :assignment_id
        """)
        
        connection.execute(update_query, {
            "is_completed": is_completed,
            "completed_at": completed_at,
            "updated_at": now,
            "assignment_id": assignment_id
        })
        
        # Fetch the updated record
        select_query = text("""
            SELECT id, assignment_id, is_completed, completed_at, created_at, updated_at
            FROM f_19f07be9__assignment_completion
            WHERE assignment_id = :assignment_id
        """)
        
        result = connection.execute(select_query, {"assignment_id": assignment_id})
        row = result.mappings().one()
        
        return jsonify(_serialize_completion_record(row)), 200
