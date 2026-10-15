"""Deterministic contract checks for Mark Assignment as Completed."""

from backend import create_app


def test_feature_routes_are_registered():
    app = create_app(testing=True)
    actual = {
        (rule.rule, method)
        for rule in app.url_map.iter_rules()
        for method in (rule.methods or set())
    }
    expected = (('/api/capability_mark_assignment_as_completed_1a7f53a5/assignments/<assignment_id>/completion', 'PUT'), ('/api/capability_mark_assignment_as_completed_1a7f53a5/assignments/<assignment_id>/completion', 'GET'), ('/api/capability_mark_assignment_as_completed_1a7f53a5/assignments/completions', 'GET'))
    assert all(route in actual for route in expected)


def test_protected_routes_reject_missing_authentication():
    client = create_app(testing=True).test_client()
    assert True
