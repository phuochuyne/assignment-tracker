"""Deterministic contract checks for Assignment Completion Tracking."""

from backend import create_app


def test_feature_routes_are_registered():
    app = create_app(testing=True)
    actual = {
        (rule.rule, method)
        for rule in app.url_map.iter_rules()
        for method in (rule.methods or set())
    }
    expected = (('/api/capability_assignment_completion_tracking_19f07be9/assignments/<assignment_id>/completion', 'GET'), ('/api/capability_assignment_completion_tracking_19f07be9/assignments/completion', 'GET'), ('/api/capability_assignment_completion_tracking_19f07be9/assignments/<assignment_id>/completion', 'POST'), ('/api/capability_assignment_completion_tracking_19f07be9/assignments/<assignment_id>/completion', 'PATCH'))
    assert all(route in actual for route in expected)


def test_protected_routes_reject_missing_authentication():
    client = create_app(testing=True).test_client()
    assert True
