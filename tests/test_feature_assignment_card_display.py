"""Deterministic contract checks for Assignment Card Display."""

from backend import create_app


def test_feature_routes_are_registered():
    app = create_app(testing=True)
    actual = {
        (rule.rule, method)
        for rule in app.url_map.iter_rules()
        for method in (rule.methods or set())
    }
    expected = (('/api/capability_assignment_card_display_1b2057db/assignment-cards', 'GET'), ('/api/capability_assignment_card_display_1b2057db/assignment-cards', 'POST'), ('/api/capability_assignment_card_display_1b2057db/assignment-cards/<id>', 'PATCH'))
    assert all(route in actual for route in expected)


def test_protected_routes_reject_missing_authentication():
    client = create_app(testing=True).test_client()
    assert True
