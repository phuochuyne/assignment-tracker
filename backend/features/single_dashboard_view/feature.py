"""Single Dashboard View feature module.

Provides a single, distraction-free dashboard to view and manage all assignments in one place.
"""

from flask import Blueprint, jsonify
from sqlalchemy import text

from backend.core.db import get_engine

blueprint = Blueprint(
    "capability_single_dashboard_view_8bb5982d",
    __name__,
    url_prefix="/api/capability_single_dashboard_view_8bb5982d"
)


@blueprint.get("/dashboard/assignments")
def get_dashboard_assignments():
    """Retrieves all assignments sorted by due date (ascending) with secondary sort by created_at.
    
    Provides the complete dataset needed to render the single dashboard view with all
    assignments visible in one place.
    
    Returns:
        JSON response with assignments array containing all assignment records.
        
    Error Responses:
        500: Internal server error when database query fails
    """
    try:
        query = text("""
            SELECT 
                id,
                title,
                unit_code,
                due_date,
                is_completed,
                created_at
            FROM f_8bb5982d__assignments
            ORDER BY due_date ASC, created_at ASC
        """)
        
        with get_engine().connect() as connection:
            result = connection.execute(query)
            rows = result.mappings().all()
            
            assignments = []
            for row in rows:
                assignment = {
                    "id": row["id"],
                    "title": row["title"],
                    "unit_code": row["unit_code"],
                    "due_date": row["due_date"].isoformat(),
                    "is_completed": bool(row["is_completed"]),
                    "created_at": row["created_at"].isoformat()
                }
                assignments.append(assignment)
            
            return jsonify({"assignments": assignments}), 200
            
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500
