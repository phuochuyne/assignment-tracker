"""Whole-application smoke tests."""

from backend import create_app


def test_health_endpoint():
    app = create_app(testing=True)
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["ok"] is True


def test_expected_function_inventory_is_frozen():
    expected = ('capability_add_assignment_622b64dc.function.create_assignment', 'capability_add_assignment_622b64dc.function.get_assignments', 'capability_localstorage_data_storage_c1936286.function.save_assignment', 'capability_localstorage_data_storage_c1936286.function.load_assignments', 'capability_localstorage_data_storage_c1936286.function.update_assignment', 'capability_localstorage_data_storage_c1936286.function.delete_assignment', 'capability_single_dashboard_view_8bb5982d.function.get_dashboard_assignments', 'capability_mark_assignment_as_completed_1a7f53a5.function.toggle_assignment_completion', 'capability_mark_assignment_as_completed_1a7f53a5.function.get_assignment_completion', 'capability_mark_assignment_as_completed_1a7f53a5.function.get_all_completions', 'capability_assignment_card_display_1b2057db.function.get_assignment_cards', 'capability_assignment_card_display_1b2057db.function.create_display_metadata', 'capability_assignment_card_display_1b2057db.function.update_display_order', 'capability_assignment_completion_tracking_19f07be9.function.get_assignment_completion_status', 'capability_assignment_completion_tracking_19f07be9.function.get_all_completion_statuses', 'capability_assignment_completion_tracking_19f07be9.function.create_completion_record', 'capability_assignment_completion_tracking_19f07be9.function.update_completion_status')
    assert len(expected) == 17
