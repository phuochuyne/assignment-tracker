# Full-stack verification

These checks use a temporary directory and verification configuration, not your deployment. The smoke command requests registered pages and JavaScript assets; it does not exercise form submissions or database business operations.

## Findings and next steps
No issues were recorded by these checks. This does not cover checks that were not run.

## Static assembly evidence
```json
{
  "application_contract_version": "frontend-experience-1",
  "application_contract_hash": "e894756a54b73c73bc556e26ac3a4900ea1a0239e0d33bbbc25e153fa78fa4d0",
  "screen_contracts_valid": true,
  "declared_interactions_valid": false,
  "static_screen_ids": [
    "capability_add_assignment_622b64dc.screen.add_assignment_form",
    "capability_add_assignment_622b64dc.screen.assignment_confirmation",
    "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
    "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
    "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
    "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
    "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
    "capability_responsive_design_507cc59c.screen.responsive_dashboard",
    "capability_single_dashboard_view_8bb5982d.screen.dashboard"
  ],
  "non_blocking_errors": [
    {
      "code": "frontend_workflow_state_unavailable",
      "screen_id": "capability_localstorage_data_storage_c1936286.screen.storage_error",
      "missing_state": [
        "error_message"
      ],
      "message": "This screen requires workflow values with no generating interaction in the delivered application."
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
      "unregistered_path": "frontend/features/single_dashboard_view/dashboard.html",
      "code": "frontend_screen_route_collision",
      "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
      "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
      "unregistered_path": "frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.html",
      "code": "frontend_screen_route_collision",
      "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
      "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
      "unregistered_path": "frontend/features/assignment_card_display/dashboard_card_view.html",
      "code": "frontend_screen_route_collision",
      "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
      "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
      "unregistered_path": "frontend/features/assignment_completion_tracking/dashboard_completion_display.html",
      "code": "frontend_screen_route_collision",
      "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
      "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
      "unregistered_path": "frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.html",
      "code": "frontend_screen_route_collision",
      "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
      "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
      "unregistered_path": "frontend/features/responsive_design/responsive_dashboard_view.html",
      "code": "frontend_screen_route_collision",
      "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
      "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
      "unregistered_path": "frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.html",
      "code": "frontend_screen_route_collision",
      "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
      "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
    }
  ],
  "journeys_verified": false,
  "verification_level": "contracts_and_page_serving",
  "static_valid": true,
  "backend_package_reused_unchanged": true,
  "backend_application_import_normalized_paths": [],
  "route_collisions_absent": false,
  "route_collisions": [
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
      "unregistered_path": "frontend/features/single_dashboard_view/dashboard.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
      "unregistered_path": "frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
      "unregistered_path": "frontend/features/assignment_card_display/dashboard_card_view.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
      "unregistered_path": "frontend/features/assignment_completion_tracking/dashboard_completion_display.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
      "unregistered_path": "frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
      "unregistered_path": "frontend/features/responsive_design/responsive_dashboard_view.html"
    },
    {
      "route": "/",
      "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
      "unregistered_screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
      "unregistered_path": "frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.html"
    }
  ],
  "screen_files_present": true,
  "self_contained_frontend": true,
  "legacy_runtime_normalized_paths": [],
  "source_snapshot_hash": "455e7cda10362668a08aaff0050feeeb96e391559366f3e82c24b77c284d4fc0",
  "errors": []
}
```

## Routes needing attention
The first page registered at a URL is served; additional pages remain in the ZIP. Choose unique routes for the unregistered paths in `fullstack.py`, update page links and rerun the route smoke check.
```json
[
  {
    "route": "/",
    "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
    "unregistered_screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
    "unregistered_path": "frontend/features/single_dashboard_view/dashboard.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
    "unregistered_screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
    "unregistered_path": "frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
    "unregistered_screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
    "unregistered_path": "frontend/features/assignment_card_display/dashboard_card_view.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
    "unregistered_screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
    "unregistered_path": "frontend/features/assignment_completion_tracking/dashboard_completion_display.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
    "unregistered_screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
    "unregistered_path": "frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
    "unregistered_screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
    "unregistered_path": "frontend/features/responsive_design/responsive_dashboard_view.html"
  },
  {
    "route": "/",
    "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
    "unregistered_screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
    "unregistered_path": "frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.html"
  }
]
```

## Runtime commands and captured results
```json
{
  "valid": true,
  "passes": {
    "compile": true,
    "application_start": true,
    "screen_routes": true,
    "self_contained_frontend": true,
    "frontend_assets": true
  },
  "commands": [
    {
      "command": [
        "/home/ubuntu/zorentia-app/venv/bin/python",
        "-m",
        "compileall",
        "-q",
        "backend",
        "frontend",
        "fullstack.py"
      ],
      "returncode": 0,
      "stdout": "",
      "stderr": "",
      "timed_out": false
    },
    {
      "command": [
        "/home/ubuntu/zorentia-app/venv/bin/python",
        "-c",
        "from fullstack import create_app;app=create_app(testing=True);client=app.test_client();routes=['/add-assignment', '/assignment-added', '/storage-error', '/'];responses=[client.get(route) for route in routes];print({'route_checks':[{'route':route,'status':response.status_code,'html_doctype':b'<!doctype html' in response.data.lower(),'compiler_marker':b'data-zorentia-compiler' in response.data} for route,response in zip(routes,responses)]},flush=True);assert responses and all(response.status_code==200 for response in responses);assert all(b'<!doctype html' in response.data.lower() for response in responses);assert all(b'data-zorentia-compiler' in response.data for response in responses);assets=['/__frontend_assets/frontend/shared/ui/library.js', '/__frontend_assets/frontend/shared/ui/runtime.js', '/__frontend_assets/frontend/features/add_assignment/add_assignment_form.js', '/__frontend_assets/frontend/features/add_assignment/assignment_confirmation.js', '/__frontend_assets/frontend/features/localstorage_data_storage/storage_error.js', '/__frontend_assets/frontend/features/automatic_deadline_sorting/assignment_dashboard.js', '/__frontend_assets/frontend/features/single_dashboard_view/dashboard.js', '/__frontend_assets/frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.js', '/__frontend_assets/frontend/features/assignment_card_display/dashboard_card_view.js', '/__frontend_assets/frontend/features/assignment_completion_tracking/dashboard_completion_display.js', '/__frontend_assets/frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.js', '/__frontend_assets/frontend/features/responsive_design/responsive_dashboard_view.js', '/__frontend_assets/frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.js'];asset_responses=[client.get(asset) for asset in assets];print({'asset_checks':[{'path':asset,'status':response.status_code,'content_type':response.content_type} for asset,response in zip(assets,asset_responses)]},flush=True);assert all(response.status_code==200 for response in asset_responses);assert all('javascript' in response.content_type for response in asset_responses);print({'routes':[(route,response.status_code) for route,response in zip(routes,responses)],'assets':[(asset,response.status_code) for asset,response in zip(assets,asset_responses)]})"
      ],
      "returncode": 0,
      "stdout": "{'route_checks': [{'route': '/add-assignment', 'status': 200, 'html_doctype': True, 'compiler_marker': True}, {'route': '/assignment-added', 'status': 200, 'html_doctype': True, 'compiler_marker': True}, {'route': '/storage-error', 'status': 200, 'html_doctype': True, 'compiler_marker': True}, {'route': '/', 'status': 200, 'html_doctype': True, 'compiler_marker': True}]}\n{'asset_checks': [{'path': '/__frontend_assets/frontend/shared/ui/library.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/shared/ui/runtime.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/add_assignment/add_assignment_form.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/add_assignment/assignment_confirmation.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/localstorage_data_storage/storage_error.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/automatic_deadline_sorting/assignment_dashboard.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/single_dashboard_view/dashboard.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/assignment_card_display/dashboard_card_view.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/assignment_completion_tracking/dashboard_completion_display.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/responsive_design/responsive_dashboard_view.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}, {'path': '/__frontend_assets/frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.js', 'status': 200, 'content_type': 'text/javascript; charset=utf-8'}]}\n{'routes': [('/add-assignment', 200), ('/assignment-added', 200), ('/storage-error', 200), ('/', 200)], 'assets': [('/__frontend_assets/frontend/shared/ui/library.js', 200), ('/__frontend_assets/frontend/shared/ui/runtime.js', 200), ('/__frontend_assets/frontend/features/add_assignment/add_assignment_form.js', 200), ('/__frontend_assets/frontend/features/add_assignment/assignment_confirmation.js', 200), ('/__frontend_assets/frontend/features/localstorage_data_storage/storage_error.js', 200), ('/__frontend_assets/frontend/features/automatic_deadline_sorting/assignment_dashboard.js', 200), ('/__frontend_assets/frontend/features/single_dashboard_view/dashboard.js', 200), ('/__frontend_assets/frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.js', 200), ('/__frontend_assets/frontend/features/assignment_card_display/dashboard_card_view.js', 200), ('/__frontend_assets/frontend/features/assignment_completion_tracking/dashboard_completion_display.js', 200), ('/__frontend_assets/frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.js', 200), ('/__frontend_assets/frontend/features/responsive_design/responsive_dashboard_view.js', 200), ('/__frontend_assets/frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.js', 200)]}\n",
      "stderr": "",
      "timed_out": false
    }
  ],
  "errors": [],
  "execution_scope": {
    "compile": "executed",
    "application_start_and_route_asset_smoke": "executed",
    "not_run": [
      "MySQL schema execution",
      "pytest",
      "browser interaction",
      "end-to-end business behavior",
      "deployment verification"
    ],
    "output_limit": "Each command retains the last 8000 characters of stdout/stderr; earlier output may be unavailable."
  }
}
```

Reproduce a failure using the recorded command from the package root after following README-FULLSTACK.md. For the smoke command, use your environment's Python executable. Compare the traceback, file/line and exit code; a timeout does not establish a code defect.
