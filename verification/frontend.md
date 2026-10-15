# Frontend generation verification

Foundation and screen generation validate their contracts and compiled output. These are not browser interaction or end-to-end business tests. The retained check records below identify successful output by file hash and retain earlier rejection details.

## Packaged screens
```json
[
  {
    "feature_id": "capability_add_assignment_622b64dc",
    "screen_id": "capability_add_assignment_622b64dc.screen.add_assignment_form",
    "route": "/add-assignment",
    "html_path": "frontend/features/add_assignment/add_assignment_form.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Container must have content"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_add_assignment_622b64dc.screen.add_assignment_form",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_add_assignment_622b64dc.screen-action.submit_assignment"
        ],
        "unavailable_capabilities": [
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_add_assignment_622b64dc",
    "screen_id": "capability_add_assignment_622b64dc.screen.assignment_confirmation",
    "route": "/assignment-added",
    "html_path": "frontend/features/add_assignment/assignment_confirmation.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_add_assignment_622b64dc.screen.assignment_confirmation",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_add_assignment_622b64dc.screen-action.load_assignments"
        ],
        "unavailable_capabilities": [
          "collection",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_localstorage_data_storage_c1936286",
    "screen_id": "capability_localstorage_data_storage_c1936286.screen.storage_error",
    "route": "/storage-error",
    "html_path": "frontend/features/localstorage_data_storage/storage_error.html",
    "output_hash": null,
    "generation_issues": []
  },
  {
    "feature_id": "capability_automatic_deadline_sorting_2088096a",
    "screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "route": "/",
    "html_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unknown configured action"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_single_dashboard_view_8bb5982d",
    "screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
    "route": "/",
    "html_path": "frontend/features/single_dashboard_view/dashboard.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_single_dashboard_view_8bb5982d.screen-action.load_dashboard_assignments"
        ],
        "unavailable_capabilities": [
          "collection",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
    "screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
    "route": "/",
    "html_path": "frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Required API route inputs have no source"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_mark_assignment_as_completed_1a7f53a5.screen-action.load_all_completions",
          "capability_mark_assignment_as_completed_1a7f53a5.screen-action.toggle_completion"
        ],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_assignment_card_display_1b2057db",
    "screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
    "route": "/",
    "html_path": "frontend/features/assignment_card_display/dashboard_card_view.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Collection requires a response scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_assignment_card_display_1b2057db.screen-action.load_assignment_cards"
        ],
        "unavailable_capabilities": [
          "collection"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_assignment_completion_tracking_19f07be9",
    "screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
    "route": "/",
    "html_path": "frontend/features/assignment_completion_tracking/dashboard_completion_display.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_assignment_completion_tracking_19f07be9.screen-action.load_all_completion_statuses",
          "capability_assignment_completion_tracking_19f07be9.screen-action.toggle_assignment_completion"
        ],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
    "screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
    "route": "/",
    "html_path": "frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unknown configured action"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_responsive_design_507cc59c",
    "screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
    "route": "/",
    "html_path": "frontend/features/responsive_design/responsive_dashboard_view.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unknown configured action"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_color_coded_status_labels_b6950121",
    "screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
    "route": "/",
    "html_path": "frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.html",
    "output_hash": null,
    "generation_issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unknown configured action"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ]
      }
    ]
  }
]
```

## Logged screen limitations
```json
[
  {
    "feature_id": "capability_add_assignment_622b64dc",
    "screen_id": "capability_add_assignment_622b64dc.screen.add_assignment_form",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Container must have content"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_add_assignment_622b64dc.screen.add_assignment_form",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_add_assignment_622b64dc.screen-action.submit_assignment"
        ],
        "unavailable_capabilities": [
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_add_assignment_622b64dc",
    "screen_id": "capability_add_assignment_622b64dc.screen.assignment_confirmation",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_add_assignment_622b64dc.screen.assignment_confirmation",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_add_assignment_622b64dc.screen-action.load_assignments"
        ],
        "unavailable_capabilities": [
          "collection",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_automatic_deadline_sorting_2088096a",
    "screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unknown configured action"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_single_dashboard_view_8bb5982d",
    "screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_single_dashboard_view_8bb5982d.screen-action.load_dashboard_assignments"
        ],
        "unavailable_capabilities": [
          "collection",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
    "screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Required API route inputs have no source"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_mark_assignment_as_completed_1a7f53a5.screen-action.load_all_completions",
          "capability_mark_assignment_as_completed_1a7f53a5.screen-action.toggle_completion"
        ],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_assignment_card_display_1b2057db",
    "screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Collection requires a response scope"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_assignment_card_display_1b2057db.screen-action.load_assignment_cards"
        ],
        "unavailable_capabilities": [
          "collection"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_assignment_completion_tracking_19f07be9",
    "screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [
          "capability_assignment_completion_tracking_19f07be9.screen-action.load_all_completion_statuses",
          "capability_assignment_completion_tracking_19f07be9.screen-action.toggle_assignment_completion"
        ],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
    "screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unknown configured action"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_responsive_design_507cc59c",
    "screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unknown configured action"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ]
      }
    ]
  },
  {
    "feature_id": "capability_color_coded_status_labels_b6950121",
    "screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
    "issues": [
      {
        "code": "frontend_screen_static_fallback",
        "details": [
          "Unknown configured action"
        ],
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid",
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ]
      }
    ]
  }
]
```

## Workflow limitations
## Findings and next steps

```json
{
  "finding": "frontend_workflow_state_unavailable",
  "code": "frontend_workflow_state_unavailable",
  "screen_id": "capability_localstorage_data_storage_c1936286.screen.storage_error",
  "missing_state": [
    "error_message"
  ],
  "message": "This screen requires workflow values with no generating interaction in the delivered application."
}
```

This screen requires workflow values with no generating interaction in the delivered application. Inspect the recorded components and correct the underlying contract or generated files.

```json
{
  "finding": "frontend_screen_route_collision",
  "route": "/",
  "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
  "unregistered_screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
  "unregistered_path": "frontend/features/single_dashboard_view/dashboard.html",
  "code": "frontend_screen_route_collision",
  "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
  "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
}
```

Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path. Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check.

```json
{
  "finding": "frontend_screen_route_collision",
  "route": "/",
  "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
  "unregistered_screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
  "unregistered_path": "frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.html",
  "code": "frontend_screen_route_collision",
  "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
  "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
}
```

Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path. Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check.

```json
{
  "finding": "frontend_screen_route_collision",
  "route": "/",
  "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
  "unregistered_screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
  "unregistered_path": "frontend/features/assignment_card_display/dashboard_card_view.html",
  "code": "frontend_screen_route_collision",
  "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
  "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
}
```

Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path. Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check.

```json
{
  "finding": "frontend_screen_route_collision",
  "route": "/",
  "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
  "unregistered_screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
  "unregistered_path": "frontend/features/assignment_completion_tracking/dashboard_completion_display.html",
  "code": "frontend_screen_route_collision",
  "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
  "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
}
```

Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path. Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check.

```json
{
  "finding": "frontend_screen_route_collision",
  "route": "/",
  "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
  "unregistered_screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
  "unregistered_path": "frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.html",
  "code": "frontend_screen_route_collision",
  "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
  "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
}
```

Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path. Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check.

```json
{
  "finding": "frontend_screen_route_collision",
  "route": "/",
  "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
  "unregistered_screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
  "unregistered_path": "frontend/features/responsive_design/responsive_dashboard_view.html",
  "code": "frontend_screen_route_collision",
  "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
  "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
}
```

Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path. Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check.

```json
{
  "finding": "frontend_screen_route_collision",
  "route": "/",
  "registered_screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "registered_path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
  "unregistered_screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
  "unregistered_path": "frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.html",
  "code": "frontend_screen_route_collision",
  "message": "Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path.",
  "repair": "Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check."
}
```

Completed pages share this route. The registered page is served; the other page remains in the package at its recorded path. Assign a unique route to the unregistered page in fullstack.py, update its links, and repeat the route check.

## Generation and repair history

Failed attempts below are historical, not automatically defects in these files. A matching file hash identifies a checked output retained in this package. Earlier discarded evidence cannot be reconstructed. An empty history does not mean every attempt passed.

### Checked output matches packaged files

```json
{
  "stage": "frontend foundation",
  "feature": null,
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "frontend foundation",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Foundation contract and files",
      "status": "passed",
      "files": [
        {
          "path": "frontend/shared/ui/library.css",
          "sha256": "31c3fb1a227be18e738bb73a9c453cd02a92dc613e7a96c47e88c712672ea58c"
        },
        {
          "path": "frontend/shared/ui/library.js",
          "sha256": "6a828731b69d0b0948ae6fa0afb4d52dcce347007e3d5e2fd603170ee27a70dc"
        },
        {
          "path": "frontend/shared/ui/runtime.js",
          "sha256": "e57339ddadbcf27a3765612e2cdcd151881edad302f78bd92d1ce846b93feeec"
        },
        {
          "path": "frontend/shared/ui/shell.html",
          "sha256": "51d72b3ce6b7543d744ffdd97629e608946ae7cce037751aa589498fa7b24414"
        },
        {
          "path": "frontend/shared/ui/auth.html",
          "sha256": "800e84d26cc057f3ab466cd725d584178e0da8d4a320388ef4d805690d890954"
        },
        {
          "path": "frontend/shared/ui/catalogue.json",
          "sha256": "19c87004cc9f026d5368bf9efba46d2727355bfb3467f83c91513469dff8725a"
        },
        {
          "path": "frontend/shared/ui/screen-templates.json",
          "sha256": "76c01145d20d88dc2aa96db9685462ec42edf17adfdfff4cd6b6f884de5c5239"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:39:08.366337+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": null,
  "screen_id": null,
  "expected_workspace_version": 1,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_source_hash": "2b110ce6083c2641a49ba6779b614346bb62958ab4b9b7975eaa51b43293352f"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:39:30.002891+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_add_assignment_622b64dc",
  "screen": "capability_add_assignment_622b64dc.screen.add_assignment_form",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Container must have content"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_add_assignment_622b64dc.screen.add_assignment_form",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Container must have content"
        ],
        "unavailable_action_ids": [
          "capability_add_assignment_622b64dc.screen-action.submit_assignment"
        ],
        "unavailable_capabilities": [
          "feedback"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/add_assignment/add_assignment_form.html",
          "sha256": "f76a5318ea7bd3fab73cb1e6b98e92419561606cc92f3518846a6d80f7de0e24"
        },
        {
          "path": "frontend/features/add_assignment/add_assignment_form.js",
          "sha256": "71e9959e6d97c0238df1c2c010a6e8dfb69a5b8eefa0a2116998d17ca0a74232"
        },
        {
          "path": "frontend/features/add_assignment/add_assignment_form.screen.json",
          "sha256": "b2af8fb7486b2f51ad732a5274838a9d0cab22ecd1db6209a0fa24011510987c"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:39:33.487113+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_add_assignment_622b64dc",
  "screen_id": "capability_add_assignment_622b64dc.screen.add_assignment_form",
  "expected_workspace_version": 2,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "6188b756f9abe614698f77a17f73eda2c84902ebaed9e32c838d2a80e2382691",
    "backend_code_hash": "0ba189e5c56c9809255b7678242c7e29a9ac597a74e562e5a156b5558d46b467",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:39:42.739053+00:00"
}
```

### Historical attempt; not evidence of a current defect

```json
{
  "stage": "frontend screen",
  "feature": "capability_localstorage_data_storage_c1936286",
  "screen": "capability_localstorage_data_storage_c1936286.screen.storage_error",
  "outcome": "failed"
}
```

## Findings and next steps

```json
{
  "finding": "UnboundLocalError"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "screen_generation_failed"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "UnboundLocalError",
      "details": [],
      "message": "cannot access local variable 'type' where it is not associated with a value"
    }
  ],
  "started_at": "2026-10-15T04:39:51.118531+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_localstorage_data_storage_c1936286",
  "screen_id": "capability_localstorage_data_storage_c1936286.screen.storage_error",
  "expected_workspace_version": 4,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "9caefb26a8fae71f131f7fe30d8994935fefea067599c43d2511e31dc16af7a3",
    "backend_code_hash": "9d27be52807b840b6337750d684dbf78a3d488bfa8786d906f9e2cd875286f79",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "failed",
  "error": {
    "code": "screen_generation_failed",
    "details": [],
    "message": "screen_generation_failed",
    "cause": {
      "type": "UnboundLocalError",
      "message": "cannot access local variable 'type' where it is not associated with a value"
    }
  },
  "finished_at": "2026-10-15T04:40:01.999226+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_localstorage_data_storage_c1936286",
  "screen": "capability_localstorage_data_storage_c1936286.screen.storage_error",
  "outcome": "completed"
}
```

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/localstorage_data_storage/storage_error.html",
          "sha256": "d033bfb302e93034b767f4b28afce49520bb684e9ab63bd20b28ceeca3cee9cd"
        },
        {
          "path": "frontend/features/localstorage_data_storage/storage_error.js",
          "sha256": "5dbfe5b660929c6420bc22e49fe3a7db5956ad62bd6a583cbc7642ddab2bb584"
        },
        {
          "path": "frontend/features/localstorage_data_storage/storage_error.screen.json",
          "sha256": "9568f25a92e8900021938e462c24bdff8ffb0a75135dd2948461341ca2c2a27f"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:40:07.575291+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_localstorage_data_storage_c1936286",
  "screen_id": "capability_localstorage_data_storage_c1936286.screen.storage_error",
  "expected_workspace_version": 4,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "9caefb26a8fae71f131f7fe30d8994935fefea067599c43d2511e31dc16af7a3",
    "backend_code_hash": "9d27be52807b840b6337750d684dbf78a3d488bfa8786d906f9e2cd875286f79",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:40:16.084392+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_add_assignment_622b64dc",
  "screen": "capability_add_assignment_622b64dc.screen.assignment_confirmation",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Required interaction capability missing: feedback"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_add_assignment_622b64dc.screen.assignment_confirmation",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "unavailable_action_ids": [
          "capability_add_assignment_622b64dc.screen-action.load_assignments"
        ],
        "unavailable_capabilities": [
          "collection",
          "feedback"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/add_assignment/assignment_confirmation.html",
          "sha256": "5d12f26241fd709605ea8cdd91adcd6e1b2473ff099c1e1ab58ca30265086d19"
        },
        {
          "path": "frontend/features/add_assignment/assignment_confirmation.js",
          "sha256": "a973d663d6ca5669c31512d61b5e2f696405552003d43950f4dbeb9f83b929f8"
        },
        {
          "path": "frontend/features/add_assignment/assignment_confirmation.screen.json",
          "sha256": "297386cae2ffdc970eb201ec9484e18461b8fd73268ddba3db59217de9aef256"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:40:21.277116+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_add_assignment_622b64dc",
  "screen_id": "capability_add_assignment_622b64dc.screen.assignment_confirmation",
  "expected_workspace_version": 6,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "6188b756f9abe614698f77a17f73eda2c84902ebaed9e32c838d2a80e2382691",
    "backend_code_hash": "0ba189e5c56c9809255b7678242c7e29a9ac597a74e562e5a156b5558d46b467",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:40:34.605033+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_automatic_deadline_sorting_2088096a",
  "screen": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Unknown configured action"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Unknown configured action"
        ],
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.html",
          "sha256": "9ebc05ee8d87939b5d64b65e8e8b4f3289fec8ec596075db346fe9466d2cb6bb"
        },
        {
          "path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.js",
          "sha256": "7b1e49f67ef62bbad8c40dffb3ac0269bba2488b971514a11d2a023b176d3ab9"
        },
        {
          "path": "frontend/features/automatic_deadline_sorting/assignment_dashboard.screen.json",
          "sha256": "9f923ff4da4da4bd5505cf68809ad87f5dc029caf75cd5d021de3d46eaae527d"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:40:43.059594+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_automatic_deadline_sorting_2088096a",
  "screen_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
  "expected_workspace_version": 8,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "ce19ecc3ba79db5cf8105f025e3b46a68d9de7d20b34ff4c67dea11e6440857b",
    "backend_code_hash": "8f3d8410946e5b20d459e39365a78277bba03d791649031b4b6d88e23f15a508",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:40:52.045197+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_single_dashboard_view_8bb5982d",
  "screen": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Required interaction capability missing: feedback"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "unavailable_action_ids": [
          "capability_single_dashboard_view_8bb5982d.screen-action.load_dashboard_assignments"
        ],
        "unavailable_capabilities": [
          "collection",
          "feedback"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/single_dashboard_view/dashboard.html",
          "sha256": "88c83244d1cd99e8063f5a2b6307e8bd8c3484768c4a269cc5fb3147a6361bca"
        },
        {
          "path": "frontend/features/single_dashboard_view/dashboard.js",
          "sha256": "7b1e49f67ef62bbad8c40dffb3ac0269bba2488b971514a11d2a023b176d3ab9"
        },
        {
          "path": "frontend/features/single_dashboard_view/dashboard.screen.json",
          "sha256": "29e0722707d8af92b50153738045a881f5925ae48a5271baac84062531e3e2d3"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:40:57.568473+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_single_dashboard_view_8bb5982d",
  "screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
  "expected_workspace_version": 10,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "b62b045d53a911cd22b7152bb6152293633fd574255876e51611acd7ea13aa5b",
    "backend_code_hash": "6f5692f5cb5bc52333290e50f49e914d400af4464d94b6f5cc2afe19c13ed19a",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:41:05.872982+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_mark_assignment_as_completed_1a7f53a5",
  "screen": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Required API route inputs have no source"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Required API route inputs have no source"
        ],
        "unavailable_action_ids": [
          "capability_mark_assignment_as_completed_1a7f53a5.screen-action.load_all_completions",
          "capability_mark_assignment_as_completed_1a7f53a5.screen-action.toggle_completion"
        ],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.html",
          "sha256": "2f7a2b1c61e1521d630d0827533d2fa2a7c89c61021927bc2f4be0a88d843a26"
        },
        {
          "path": "frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.js",
          "sha256": "7b1e49f67ef62bbad8c40dffb3ac0269bba2488b971514a11d2a023b176d3ab9"
        },
        {
          "path": "frontend/features/mark_assignment_as_completed/assignment_dashboard_with_completion_controls.screen.json",
          "sha256": "0c14cfd8d7d5d6d32ebb8b155c92f07afe689eceabc0c5365b23a78c35743fdc"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:41:10.426918+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
  "screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
  "expected_workspace_version": 12,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "b4b2b07d75c690c6eaff57158a1c48e31beb7da1c37312f53a0a5e33180d1f45",
    "backend_code_hash": "80e6aa6ed7028f0ea8c188cb516b1056a6687b0283c2fc2cde9d9b55c6d65e56",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:41:19.715771+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_assignment_card_display_1b2057db",
  "screen": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Collection requires a response scope"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Collection requires a response scope"
        ],
        "unavailable_action_ids": [
          "capability_assignment_card_display_1b2057db.screen-action.load_assignment_cards"
        ],
        "unavailable_capabilities": [
          "collection"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/assignment_card_display/dashboard_card_view.html",
          "sha256": "4a63c7e8c7a7a8c9967e72a2b67caccb42417a30b79466ed5071da0b92de5179"
        },
        {
          "path": "frontend/features/assignment_card_display/dashboard_card_view.js",
          "sha256": "7b1e49f67ef62bbad8c40dffb3ac0269bba2488b971514a11d2a023b176d3ab9"
        },
        {
          "path": "frontend/features/assignment_card_display/dashboard_card_view.screen.json",
          "sha256": "5aaf659ff6673985ad93eb0a1b12b6cd4a0d5bfc7ffce774b3bbe31d727187d6"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:41:32.251172+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_assignment_card_display_1b2057db",
  "screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
  "expected_workspace_version": 14,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "08cf82b3633482e2b01412205b792603b9650e113f381995acbf1b61fc7071d9",
    "backend_code_hash": "01c4faf391010e87652f017e87d641701e122f232c3dabbd4a5d38dc8b2529c4",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:41:40.042770+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_assignment_completion_tracking_19f07be9",
  "screen": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Required interaction capability missing: feedback"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Required interaction capability missing: feedback"
        ],
        "unavailable_action_ids": [
          "capability_assignment_completion_tracking_19f07be9.screen-action.load_all_completion_statuses",
          "capability_assignment_completion_tracking_19f07be9.screen-action.toggle_assignment_completion"
        ],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/assignment_completion_tracking/dashboard_completion_display.html",
          "sha256": "c218c7dc3a089c4d352e5d34613c8a62fd4c60ff401c23e1a5a01d402a60a4e2"
        },
        {
          "path": "frontend/features/assignment_completion_tracking/dashboard_completion_display.js",
          "sha256": "7b1e49f67ef62bbad8c40dffb3ac0269bba2488b971514a11d2a023b176d3ab9"
        },
        {
          "path": "frontend/features/assignment_completion_tracking/dashboard_completion_display.screen.json",
          "sha256": "71810638115e32ce3c3031af485ae89921d32c636c42b97c0c95a2da254c16cc"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:41:44.518914+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_assignment_completion_tracking_19f07be9",
  "screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
  "expected_workspace_version": 16,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "256c8618a39063ab7786542f5fba0dffe410df0a64cbc4b3fc7420a76222db6b",
    "backend_code_hash": "5ae86f2b1b67e6f389c9e82e52a1bba9b53349fe72f3c9e04ab832683f82800a",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:41:54.760722+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_overdue_assignment_highlighting_a3b2e567",
  "screen": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Unknown configured action"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Unknown configured action"
        ],
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.html",
          "sha256": "c9681d6ad9ec9006d103f9f3535b0e4dde1d53ced9548e89fa231b8a2a51f674"
        },
        {
          "path": "frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.js",
          "sha256": "7b1e49f67ef62bbad8c40dffb3ac0269bba2488b971514a11d2a023b176d3ab9"
        },
        {
          "path": "frontend/features/overdue_assignment_highlighting/assignment_dashboard_with_overdue_highlighting.screen.json",
          "sha256": "7fca6f3ebdf290d7d56cc24d2a35cbfedafbac2639cb3d7f63c1c27ef15c428c"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:41:59.350524+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
  "screen_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
  "expected_workspace_version": 18,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "a67e0667649372658825df89983a0651ed49e1c8f3b7743948b89a55d875b36c",
    "backend_code_hash": "e739a078021e01e6b2cd7feb421860ac893817e944764a02772c616bf3b08d31",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:42:07.425626+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_responsive_design_507cc59c",
  "screen": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Unknown configured action"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Unknown configured action"
        ],
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection",
          "item_action",
          "feedback"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/responsive_design/responsive_dashboard_view.html",
          "sha256": "cc6ab1579911eada477e839934a6cf010fc490cf7b50496b25a44ad29b5616f8"
        },
        {
          "path": "frontend/features/responsive_design/responsive_dashboard_view.js",
          "sha256": "7b1e49f67ef62bbad8c40dffb3ac0269bba2488b971514a11d2a023b176d3ab9"
        },
        {
          "path": "frontend/features/responsive_design/responsive_dashboard_view.screen.json",
          "sha256": "02c1ca25349c0966cd44c83b34fe3bc7d1bdd7b2edde68a872db236bdec6df0d"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:42:11.838916+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_responsive_design_507cc59c",
  "screen_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
  "expected_workspace_version": 20,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "631a36024a05629f48e4dd033983d3e08115cf8ef6ac5b49f4c6c022ea4d6dfc",
    "backend_code_hash": "85e93fd170de8f3ea92853f0f2f8b9d8a6630f8ee135f31791995843e1893261",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:42:22.599372+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "frontend screen",
  "feature": "capability_color_coded_status_labels_b6950121",
  "screen": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
  "outcome": "completed_with_warnings"
}
```

## Findings and next steps

```json
{
  "finding": "screen_composition_invalid"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "finding": "frontend_screen_static_fallback"
}
```

The frontend screen check recorded this finding. Use its identifiers and evidence below to locate the affected contract/file and compare the expected and actual values. No more specific cause was recorded.

```json
{
  "stage": "frontend screen",
  "tool_slug": "frontend-generator",
  "checks": [
    {
      "check": "Screen completeness and compiled output",
      "status": "failed",
      "code": "screen_composition_invalid",
      "details": [
        "Unknown configured action"
      ],
      "message": "screen_composition_invalid"
    },
    {
      "check": "Static screen fallback",
      "status": "warning",
      "code": "frontend_screen_static_fallback",
      "details": {
        "code": "frontend_screen_static_fallback",
        "screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
        "message": "This screen was completed as a static interface because no safe interactive composition was available.",
        "details": [
          "Unknown configured action"
        ],
        "unavailable_action_ids": [],
        "unavailable_capabilities": [
          "collection"
        ],
        "resolution": "The static screen is complete; unavailable interactions are recorded here as generation limitations.",
        "source_error_code": "screen_composition_invalid"
      }
    },
    {
      "check": "Static screen completeness and compiled output",
      "status": "passed",
      "files": [
        {
          "path": "frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.html",
          "sha256": "f320cc8386fc7a214f1c2757dbbbcc32540f53b2dfb37b8638602c41ab71fc19"
        },
        {
          "path": "frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.js",
          "sha256": "7b1e49f67ef62bbad8c40dffb3ac0269bba2488b971514a11d2a023b176d3ab9"
        },
        {
          "path": "frontend/features/color_coded_status_labels/dashboard_with_color_coded_assignments.screen.json",
          "sha256": "f3648b80ba05223a8e0be1668a4c43baa19f4685f1232f8da14fd2188f55181a"
        }
      ]
    }
  ],
  "started_at": "2026-10-15T04:42:27.112963+00:00",
  "workspace_id": "5a9dff17-22e6-4896-8823-6ad5f18cf313",
  "feature_id": "capability_color_coded_status_labels_b6950121",
  "screen_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
  "expected_workspace_version": 22,
  "session_id": "068cf4e6-9cad-48be-aa18-21065e6d0b9b",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_screens_hash": "b44af2aae59fb455eb9d9589db78f8aaa7df056bb7d0aa2005cdee48c7603f94",
    "backend_code_hash": "a93a686fe6c6e3faf7f98714be01c0c69502ac4dc32b9aa38b6b17ccd4e0bf79",
    "foundation_hash": "3cedbe791d82de2805b56c05c0fff2cf86953b840bcc91a719497cafd265d69a"
  },
  "outcome": "completed_with_warnings",
  "finished_at": "2026-10-15T04:42:36.005971+00:00"
}
```
