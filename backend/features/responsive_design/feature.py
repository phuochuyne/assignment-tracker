"""Responsive Design feature module.

This module provides endpoints to serve responsive design metadata and configuration
for the frontend to ensure the interface works on both phones and laptops.
"""

from flask import Blueprint, jsonify

blueprint = Blueprint("responsive_design", __name__, url_prefix="/api/responsive-design")


@blueprint.get("/config")
def get_responsive_config():
    """Get responsive design configuration for the frontend.
    
    Returns viewport settings, breakpoints, and device-specific configurations
    to ensure proper responsive behavior across devices.
    """
    config = {
        "viewport": {
            "width": "device-width",
            "initial_scale": 1.0,
            "minimum_scale": 1.0,
            "maximum_scale": 5.0,
            "user_scalable": True
        },
        "breakpoints": {
            "mobile": {
                "min": 0,
                "max": 767,
                "columns": 4,
                "gutter": 16
            },
            "tablet": {
                "min": 768,
                "max": 1023,
                "columns": 8,
                "gutter": 24
            },
            "laptop": {
                "min": 1024,
                "max": 1439,
                "columns": 12,
                "gutter": 24
            },
            "desktop": {
                "min": 1440,
                "max": None,
                "columns": 12,
                "gutter": 32
            }
        },
        "font_scaling": {
            "mobile": {
                "base": 14,
                "scale": 1.125
            },
            "tablet": {
                "base": 15,
                "scale": 1.2
            },
            "laptop": {
                "base": 16,
                "scale": 1.25
            },
            "desktop": {
                "base": 16,
                "scale": 1.333
            }
        },
        "touch_targets": {
            "mobile": {
                "min_size": 44,
                "spacing": 8
            },
            "laptop": {
                "min_size": 32,
                "spacing": 4
            }
        }
    }
    
    return jsonify(config), 200


@blueprint.get("/device-info")
def get_device_recommendations():
    """Get device-specific recommendations and best practices.
    
    Returns information about optimal layouts, interaction patterns,
    and performance considerations for different device types.
    """
    recommendations = {
        "mobile": {
            "layout": "single-column",
            "navigation": "bottom-tab-bar",
            "gestures": ["swipe", "tap", "long-press"],
            "image_quality": "medium",
            "lazy_loading": True,
            "infinite_scroll": True
        },
        "tablet": {
            "layout": "adaptive-two-column",
            "navigation": "side-drawer",
            "gestures": ["swipe", "tap", "pinch-zoom"],
            "image_quality": "high",
            "lazy_loading": True,
            "infinite_scroll": False
        },
        "laptop": {
            "layout": "multi-column",
            "navigation": "top-bar",
            "gestures": ["click", "hover"],
            "image_quality": "high",
            "lazy_loading": False,
            "infinite_scroll": False,
            "keyboard_shortcuts": True
        },
        "desktop": {
            "layout": "wide-multi-column",
            "navigation": "top-bar-with-sidebar",
            "gestures": ["click", "hover", "drag-drop"],
            "image_quality": "ultra",
            "lazy_loading": False,
            "infinite_scroll": False,
            "keyboard_shortcuts": True
        }
    }
    
    return jsonify(recommendations), 200


@blueprint.get("/health")
def health_check():
    """Health check endpoint for responsive design service."""
    return jsonify({
        "status": "healthy",
        "service": "responsive_design",
        "version": "1.0.0"
    }), 200
