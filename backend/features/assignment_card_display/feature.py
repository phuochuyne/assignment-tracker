"""Assignment Card Display feature module.

This module implements assignment card display functionality with deadline-based sorting.
"""

import uuid
from datetime import datetime
from typing import Any, Dict, List

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from backend.core.db import get_engine

blueprint = Blueprint(
    "capability_assignment_card_display_1b2057db",
    __name__,
    url_prefix="/api/capability_assignment_card_display_1b2057db"
)


@blueprint.get("/assignment-cards")
def get_assignment_cards():
    """Retrieves all assignment cards with their display metadata, sorted by deadline order.
    
    Returns:
        JSON response with cards array sorted by display_order
    """
    try:
        with get_engine().begin() as connection:
            result = connection.execute(
                text("""
                    SELECT id, assignment_reference, display_order, last_rendered_at
                    FROM f_1b2057db__assignment_display_metadata
                    ORDER BY display_order ASC
                """)
            )
            
            cards = []
            for row in result.mappings():
                card = {
                    "id": row["id"],
                    "assignment_reference": row["assignment_reference"],
                    "display_order": row["display_order"],
                    "last_rendered_at": row["last_rendered_at"].isoformat() if row["last_rendered_at"] else None
                }
                cards.append(card)
            
            return jsonify({"cards": cards}), 200
            
    except Exception as e:
        return jsonify({
            "code": "INTERNAL_ERROR",
            "message": "Failed to retrieve assignment cards"
        }), 500


@blueprint.post("/assignment-cards")
def create_display_metadata():
    """Creates display metadata for a new assignment card.
    
    Returns:
        JSON response with created display metadata record
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or "assignment_reference" not in data or "display_order" not in data:
            return jsonify({
                "code": "INVALID_REQUEST",
                "message": "Missing or invalid assignment_reference or display_order"
            }), 400
        
        assignment_reference = data["assignment_reference"]
        display_order = data["display_order"]
        
        # Validate types and constraints
        if not isinstance(assignment_reference, str):
            return jsonify({
                "code": "INVALID_REQUEST",
                "message": "Missing or invalid assignment_reference or display_order"
            }), 400
        
        if not isinstance(display_order, int) or display_order < 0:
            return jsonify({
                "code": "INVALID_REQUEST",
                "message": "Missing or invalid assignment_reference or display_order"
            }), 400
        
        # Validate UUID format
        try:
            uuid.UUID(assignment_reference)
        except (ValueError, AttributeError):
            return jsonify({
                "code": "INVALID_REQUEST",
                "message": "Missing or invalid assignment_reference or display_order"
            }), 400
        
        with get_engine().begin() as connection:
            # Check for duplicate
            check_result = connection.execute(
                text("""
                    SELECT id FROM f_1b2057db__assignment_display_metadata
                    WHERE assignment_reference = :assignment_reference
                """),
                {"assignment_reference": assignment_reference}
            )
            
            if check_result.fetchone():
                return jsonify({
                    "code": "DUPLICATE_METADATA",
                    "message": "Display metadata already exists for this assignment"
                }), 409
            
            # Create new record
            new_id = str(uuid.uuid4())
            connection.execute(
                text("""
                    INSERT INTO f_1b2057db__assignment_display_metadata
                    (id, assignment_reference, display_order, last_rendered_at)
                    VALUES (:id, :assignment_reference, :display_order, NULL)
                """),
                {
                    "id": new_id,
                    "assignment_reference": assignment_reference,
                    "display_order": display_order
                }
            )
            
            return jsonify({
                "id": new_id,
                "assignment_reference": assignment_reference,
                "display_order": display_order,
                "last_rendered_at": None
            }), 201
            
    except Exception as e:
        # Check if it's already a handled error response
        if hasattr(e, 'code'):
            raise
        return jsonify({
            "code": "INTERNAL_ERROR",
            "message": "Failed to create display metadata"
        }), 500


@blueprint.patch("/assignment-cards/<id>")
def update_display_order(id: str):
    """Updates the display order and last rendered timestamp for assignment cards.
    
    Args:
        id: The display metadata record ID
        
    Returns:
        JSON response with updated display metadata record
    """
    try:
        data = request.get_json()
        
        # Validate at least one property is provided
        if not data or len(data) == 0:
            return jsonify({
                "code": "INVALID_REQUEST",
                "message": "Invalid display_order or last_rendered_at format"
            }), 400
        
        # Validate display_order if provided
        if "display_order" in data:
            display_order = data["display_order"]
            if not isinstance(display_order, int) or display_order < 0:
                return jsonify({
                    "code": "INVALID_REQUEST",
                    "message": "Invalid display_order or last_rendered_at format"
                }), 400
        
        # Validate last_rendered_at if provided
        if "last_rendered_at" in data:
            last_rendered_at = data["last_rendered_at"]
            if not isinstance(last_rendered_at, str):
                return jsonify({
                    "code": "INVALID_REQUEST",
                    "message": "Invalid display_order or last_rendered_at format"
                }), 400
            try:
                datetime.fromisoformat(last_rendered_at.replace('Z', '+00:00'))
            except (ValueError, AttributeError):
                return jsonify({
                    "code": "INVALID_REQUEST",
                    "message": "Invalid display_order or last_rendered_at format"
                }), 400
        
        with get_engine().begin() as connection:
            # Check if record exists
            check_result = connection.execute(
                text("""
                    SELECT id FROM f_1b2057db__assignment_display_metadata
                    WHERE id = :id
                """),
                {"id": id}
            )
            
            if not check_result.fetchone():
                return jsonify({
                    "code": "NOT_FOUND",
                    "message": "Display metadata record not found"
                }), 404
            
            # Build dynamic update query
            update_fields = []
            params = {"id": id}
            
            if "display_order" in data:
                update_fields.append("display_order = :display_order")
                params["display_order"] = data["display_order"]
            
            if "last_rendered_at" in data:
                update_fields.append("last_rendered_at = :last_rendered_at")
                params["last_rendered_at"] = data["last_rendered_at"]
            
            if update_fields:
                update_query = f"""
                    UPDATE f_1b2057db__assignment_display_metadata
                    SET {', '.join(update_fields)}
                    WHERE id = :id
                """
                connection.execute(text(update_query), params)
            
            # Fetch updated record
            result = connection.execute(
                text("""
                    SELECT id, assignment_reference, display_order, last_rendered_at
                    FROM f_1b2057db__assignment_display_metadata
                    WHERE id = :id
                """),
                {"id": id}
            )
            
            row = result.mappings().one()
            
            return jsonify({
                "id": row["id"],
                "assignment_reference": row["assignment_reference"],
                "display_order": row["display_order"],
                "last_rendered_at": row["last_rendered_at"].isoformat() if row["last_rendered_at"] else None
            }), 200
            
    except Exception as e:
        # Check if it's already a handled error response
        if hasattr(e, 'code'):
            raise
        return jsonify({
            "code": "INTERNAL_ERROR",
            "message": "Failed to update display metadata"
        }), 500
