# Architecture verification

These are contract and coverage checks, not executable application tests. Non-blocking findings describe issues intentionally retained in the generated files for you to inspect and repair. They do not mean the package is missing. Historical attempts may refer to an earlier scope; compare scope hashes.

## Findings and next steps

```json
{
  "finding": "cross_feature_table_concept_overlap",
  "code": "cross_feature_table_concept_overlap",
  "severity": "error",
  "blocking": false,
  "category": "database",
  "message": "Multiple features define separate tables for the same likely 'assignment' concept.",
  "affected_feature_ids": [
    "capability_add_assignment_622b64dc",
    "capability_localstorage_data_storage_c1936286",
    "capability_single_dashboard_view_8bb5982d"
  ],
  "components": [
    {
      "feature_id": "capability_add_assignment_622b64dc",
      "component_id": "capability_add_assignment_622b64dc.table.assignments",
      "name": "f_622b64dc__assignments"
    },
    {
      "feature_id": "capability_localstorage_data_storage_c1936286",
      "component_id": "capability_localstorage_data_storage_c1936286.table.assignments",
      "name": "f_c1936286__assignments"
    },
    {
      "feature_id": "capability_single_dashboard_view_8bb5982d",
      "component_id": "capability_single_dashboard_view_8bb5982d.table.assignments",
      "name": "f_8bb5982d__assignments"
    }
  ],
  "repair": "Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships."
}
```

Multiple features define separate tables for the same likely 'assignment' concept. Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships.

```json
{
  "finding": "cross_feature_table_concept_overlap",
  "code": "cross_feature_table_concept_overlap",
  "severity": "error",
  "blocking": false,
  "category": "database",
  "message": "Multiple features define separate tables for the same likely 'assignment completion' concept.",
  "affected_feature_ids": [
    "capability_assignment_completion_tracking_19f07be9",
    "capability_mark_assignment_as_completed_1a7f53a5"
  ],
  "components": [
    {
      "feature_id": "capability_assignment_completion_tracking_19f07be9",
      "component_id": "capability_assignment_completion_tracking_19f07be9.table.assignment_completion",
      "name": "f_19f07be9__assignment_completion"
    },
    {
      "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
      "component_id": "capability_mark_assignment_as_completed_1a7f53a5.table.assignment_completion",
      "name": "f_1a7f53a5__assignment_completion"
    }
  ],
  "repair": "Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships."
}
```

Multiple features define separate tables for the same likely 'assignment completion' concept. Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships.

```json
{
  "finding": "cross_feature_screen_route_collision",
  "code": "cross_feature_screen_route_collision",
  "severity": "error",
  "blocking": false,
  "category": "frontend",
  "message": "Multiple features define screens for the same route '/'.",
  "affected_feature_ids": [
    "capability_assignment_card_display_1b2057db",
    "capability_assignment_completion_tracking_19f07be9",
    "capability_automatic_deadline_sorting_2088096a",
    "capability_color_coded_status_labels_b6950121",
    "capability_mark_assignment_as_completed_1a7f53a5",
    "capability_overdue_assignment_highlighting_a3b2e567",
    "capability_responsive_design_507cc59c",
    "capability_single_dashboard_view_8bb5982d"
  ],
  "components": [
    {
      "feature_id": "capability_assignment_card_display_1b2057db",
      "component_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
      "name": "Dashboard Card View",
      "route": "/"
    },
    {
      "feature_id": "capability_assignment_completion_tracking_19f07be9",
      "component_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
      "name": "Dashboard Completion Display",
      "route": "/"
    },
    {
      "feature_id": "capability_automatic_deadline_sorting_2088096a",
      "component_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
      "name": "Assignment Dashboard",
      "route": "/"
    },
    {
      "feature_id": "capability_color_coded_status_labels_b6950121",
      "component_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
      "name": "Dashboard with Color-Coded Assignments",
      "route": "/"
    },
    {
      "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
      "component_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
      "name": "Assignment Dashboard with Completion Controls",
      "route": "/"
    },
    {
      "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
      "component_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
      "name": "Assignment Dashboard with Overdue Highlighting",
      "route": "/"
    },
    {
      "feature_id": "capability_responsive_design_507cc59c",
      "component_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
      "name": "Responsive Dashboard View",
      "route": "/"
    },
    {
      "feature_id": "capability_single_dashboard_view_8bb5982d",
      "component_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
      "name": "Dashboard",
      "route": "/"
    }
  ],
  "repair": "Decide whether these responsibilities belong on one shared screen. Merge the screen behavior or assign distinct routes, then update navigation and actions."
}
```

Multiple features define screens for the same route '/'. Decide whether these responsibilities belong on one shared screen. Merge the screen behavior or assign distinct routes, then update navigation and actions.

## Current blueprint
```json
{
  "source": {
    "scope_id": "scope_assignment_tracker_fbf1a7c1",
    "source_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
    "source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006"
  },
  "blueprint_hash": "1c0b448c2f56e00c6ee2e865161ecd441694c0d860e1a5f4ff8f457cb1c42a96",
  "assembly": {
    "valid": true,
    "status": "generated_with_issues",
    "errors": [],
    "non_blocking_errors": [
      {
        "code": "cross_feature_table_concept_overlap",
        "severity": "error",
        "blocking": false,
        "category": "database",
        "message": "Multiple features define separate tables for the same likely 'assignment' concept.",
        "affected_feature_ids": [
          "capability_add_assignment_622b64dc",
          "capability_localstorage_data_storage_c1936286",
          "capability_single_dashboard_view_8bb5982d"
        ],
        "components": [
          {
            "feature_id": "capability_add_assignment_622b64dc",
            "component_id": "capability_add_assignment_622b64dc.table.assignments",
            "name": "f_622b64dc__assignments"
          },
          {
            "feature_id": "capability_localstorage_data_storage_c1936286",
            "component_id": "capability_localstorage_data_storage_c1936286.table.assignments",
            "name": "f_c1936286__assignments"
          },
          {
            "feature_id": "capability_single_dashboard_view_8bb5982d",
            "component_id": "capability_single_dashboard_view_8bb5982d.table.assignments",
            "name": "f_8bb5982d__assignments"
          }
        ],
        "repair": "Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships."
      },
      {
        "code": "cross_feature_table_concept_overlap",
        "severity": "error",
        "blocking": false,
        "category": "database",
        "message": "Multiple features define separate tables for the same likely 'assignment completion' concept.",
        "affected_feature_ids": [
          "capability_assignment_completion_tracking_19f07be9",
          "capability_mark_assignment_as_completed_1a7f53a5"
        ],
        "components": [
          {
            "feature_id": "capability_assignment_completion_tracking_19f07be9",
            "component_id": "capability_assignment_completion_tracking_19f07be9.table.assignment_completion",
            "name": "f_19f07be9__assignment_completion"
          },
          {
            "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
            "component_id": "capability_mark_assignment_as_completed_1a7f53a5.table.assignment_completion",
            "name": "f_1a7f53a5__assignment_completion"
          }
        ],
        "repair": "Inspect whether these tables represent one shared entity. If they do, keep one canonical table and update the affected feature queries and relationships."
      },
      {
        "code": "cross_feature_screen_route_collision",
        "severity": "error",
        "blocking": false,
        "category": "frontend",
        "message": "Multiple features define screens for the same route '/'.",
        "affected_feature_ids": [
          "capability_assignment_card_display_1b2057db",
          "capability_assignment_completion_tracking_19f07be9",
          "capability_automatic_deadline_sorting_2088096a",
          "capability_color_coded_status_labels_b6950121",
          "capability_mark_assignment_as_completed_1a7f53a5",
          "capability_overdue_assignment_highlighting_a3b2e567",
          "capability_responsive_design_507cc59c",
          "capability_single_dashboard_view_8bb5982d"
        ],
        "components": [
          {
            "feature_id": "capability_assignment_card_display_1b2057db",
            "component_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
            "name": "Dashboard Card View",
            "route": "/"
          },
          {
            "feature_id": "capability_assignment_completion_tracking_19f07be9",
            "component_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
            "name": "Dashboard Completion Display",
            "route": "/"
          },
          {
            "feature_id": "capability_automatic_deadline_sorting_2088096a",
            "component_id": "capability_automatic_deadline_sorting_2088096a.screen.dashboard",
            "name": "Assignment Dashboard",
            "route": "/"
          },
          {
            "feature_id": "capability_color_coded_status_labels_b6950121",
            "component_id": "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments",
            "name": "Dashboard with Color-Coded Assignments",
            "route": "/"
          },
          {
            "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
            "component_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
            "name": "Assignment Dashboard with Completion Controls",
            "route": "/"
          },
          {
            "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
            "component_id": "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard",
            "name": "Assignment Dashboard with Overdue Highlighting",
            "route": "/"
          },
          {
            "feature_id": "capability_responsive_design_507cc59c",
            "component_id": "capability_responsive_design_507cc59c.screen.responsive_dashboard",
            "name": "Responsive Dashboard View",
            "route": "/"
          },
          {
            "feature_id": "capability_single_dashboard_view_8bb5982d",
            "component_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
            "name": "Dashboard",
            "route": "/"
          }
        ],
        "repair": "Decide whether these responsibilities belong on one shared screen. Merge the screen behavior or assign distinct routes, then update navigation and actions."
      }
    ],
    "non_blocking_error_count": 3
  },
  "coverage": {
    "valid": true,
    "features": {
      "covered": 10,
      "total": 10
    },
    "acceptance_criteria": {
      "covered": 30,
      "total": 30
    }
  },
  "features": [
    {
      "feature_id": "capability_add_assignment_622b64dc",
      "verification": {
        "valid": true,
        "feature_id": "capability_add_assignment_622b64dc",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_clicking_add_saves_the_assignment_and__3e019dcc",
            "table_ids": [
              "capability_add_assignment_622b64dc.table.assignments"
            ],
            "function_ids": [
              "capability_add_assignment_622b64dc.function.create_assignment",
              "capability_add_assignment_622b64dc.function.get_assignments"
            ],
            "screen_ids": [
              "capability_add_assignment_622b64dc.screen.add_assignment_form",
              "capability_add_assignment_622b64dc.screen.assignment_confirmation"
            ]
          },
          {
            "criterion_id": "criterion_done_when_i_can_enter_a_unit_code_in_a_text_fiel_28734703",
            "table_ids": [
              "capability_add_assignment_622b64dc.table.assignments"
            ],
            "function_ids": [
              "capability_add_assignment_622b64dc.function.create_assignment"
            ],
            "screen_ids": [
              "capability_add_assignment_622b64dc.screen.add_assignment_form"
            ]
          },
          {
            "criterion_id": "criterion_done_when_i_can_enter_an_assignment_title_in_a_t_8c26c66c",
            "table_ids": [
              "capability_add_assignment_622b64dc.table.assignments"
            ],
            "function_ids": [
              "capability_add_assignment_622b64dc.function.create_assignment"
            ],
            "screen_ids": [
              "capability_add_assignment_622b64dc.screen.add_assignment_form"
            ]
          },
          {
            "criterion_id": "criterion_done_when_i_can_select_a_due_date_using_a_date_p_07aaf56a",
            "table_ids": [
              "capability_add_assignment_622b64dc.table.assignments"
            ],
            "function_ids": [
              "capability_add_assignment_622b64dc.function.create_assignment"
            ],
            "screen_ids": [
              "capability_add_assignment_622b64dc.screen.add_assignment_form"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_add_assignment_622b64dc.screen.add_assignment_form",
            "action_id": "capability_add_assignment_622b64dc.screen-action.submit_assignment",
            "function_id": "capability_add_assignment_622b64dc.function.create_assignment",
            "table_ids": [
              "capability_add_assignment_622b64dc.table.assignments"
            ]
          },
          {
            "screen_id": "capability_add_assignment_622b64dc.screen.assignment_confirmation",
            "action_id": "capability_add_assignment_622b64dc.screen-action.load_assignments",
            "function_id": "capability_add_assignment_622b64dc.function.get_assignments",
            "table_ids": [
              "capability_add_assignment_622b64dc.table.assignments"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_localstorage_data_storage_c1936286",
      "verification": {
        "valid": true,
        "feature_id": "capability_localstorage_data_storage_c1936286",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_assignments_i_add_are_saved_to_browser_f33257aa",
            "table_ids": [
              "capability_localstorage_data_storage_c1936286.table.assignments"
            ],
            "function_ids": [
              "capability_localstorage_data_storage_c1936286.function.save_assignment"
            ],
            "screen_ids": [
              "capability_localstorage_data_storage_c1936286.screen.storage_error"
            ]
          },
          {
            "criterion_id": "criterion_done_when_changes_to_assignments_edits_deletions_366bf22b",
            "table_ids": [
              "capability_localstorage_data_storage_c1936286.table.assignments"
            ],
            "function_ids": [
              "capability_localstorage_data_storage_c1936286.function.save_assignment",
              "capability_localstorage_data_storage_c1936286.function.update_assignment",
              "capability_localstorage_data_storage_c1936286.function.delete_assignment"
            ],
            "screen_ids": [
              "capability_localstorage_data_storage_c1936286.screen.storage_error"
            ]
          },
          {
            "criterion_id": "criterion_done_when_i_can_close_the_browser_and_reopen_it__28977cbb",
            "table_ids": [
              "capability_localstorage_data_storage_c1936286.table.assignments"
            ],
            "function_ids": [
              "capability_localstorage_data_storage_c1936286.function.load_assignments"
            ],
            "screen_ids": [
              "capability_localstorage_data_storage_c1936286.screen.storage_error"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_automatic_deadline_sorting_2088096a",
      "verification": {
        "valid": true,
        "feature_id": "capability_automatic_deadline_sorting_2088096a",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_adding_a_new_assignment_automatically__1e1c534c",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_automatic_deadline_sorting_2088096a.screen.dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_assignments_are_displayed_with_the_ear_59ef5114",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_automatic_deadline_sorting_2088096a.screen.dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_sort_order_updates_automatically_w_7f138293",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_automatic_deadline_sorting_2088096a.screen.dashboard"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_single_dashboard_view_8bb5982d",
      "verification": {
        "valid": true,
        "feature_id": "capability_single_dashboard_view_8bb5982d",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_opening_the_app_shows_a_single_page_di_3c72cc1f",
            "table_ids": [
              "capability_single_dashboard_view_8bb5982d.table.assignments"
            ],
            "function_ids": [
              "capability_single_dashboard_view_8bb5982d.function.get_dashboard_assignments"
            ],
            "screen_ids": [
              "capability_single_dashboard_view_8bb5982d.screen.dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_dashboard_has_a_clean_minimalist_d_9cbdce4b",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_single_dashboard_view_8bb5982d.screen.dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_dashboard_is_the_main_view_where_i_ecbe19f6",
            "table_ids": [
              "capability_single_dashboard_view_8bb5982d.table.assignments"
            ],
            "function_ids": [
              "capability_single_dashboard_view_8bb5982d.function.get_dashboard_assignments"
            ],
            "screen_ids": [
              "capability_single_dashboard_view_8bb5982d.screen.dashboard"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_single_dashboard_view_8bb5982d.screen.dashboard",
            "action_id": "capability_single_dashboard_view_8bb5982d.screen-action.load_dashboard_assignments",
            "function_id": "capability_single_dashboard_view_8bb5982d.function.get_dashboard_assignments",
            "table_ids": [
              "capability_single_dashboard_view_8bb5982d.table.assignments"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
      "verification": {
        "valid": true,
        "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_clicking_the_button_toggles_the_assign_75a7e6c0",
            "table_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.table.assignment_completion"
            ],
            "function_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.function.toggle_assignment_completion"
            ],
            "screen_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_each_assignment_has_a_button_or_checkb_b32084b0",
            "table_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.table.assignment_completion"
            ],
            "function_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.function.get_assignment_completion",
              "capability_mark_assignment_as_completed_1a7f53a5.function.get_all_completions"
            ],
            "screen_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_completion_status_is_saved_and_per_2314b2a5",
            "table_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.table.assignment_completion"
            ],
            "function_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.function.toggle_assignment_completion",
              "capability_mark_assignment_as_completed_1a7f53a5.function.get_assignment_completion",
              "capability_mark_assignment_as_completed_1a7f53a5.function.get_all_completions"
            ],
            "screen_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
            "action_id": "capability_mark_assignment_as_completed_1a7f53a5.screen-action.load_all_completions",
            "function_id": "capability_mark_assignment_as_completed_1a7f53a5.function.get_all_completions",
            "table_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.table.assignment_completion"
            ]
          },
          {
            "screen_id": "capability_mark_assignment_as_completed_1a7f53a5.screen.dashboard",
            "action_id": "capability_mark_assignment_as_completed_1a7f53a5.screen-action.toggle_completion",
            "function_id": "capability_mark_assignment_as_completed_1a7f53a5.function.toggle_assignment_completion",
            "table_ids": [
              "capability_mark_assignment_as_completed_1a7f53a5.table.assignment_completion",
              "capability_mark_assignment_as_completed_1a7f53a5.table.assignment_completion"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_assignment_card_display_1b2057db",
      "verification": {
        "valid": true,
        "feature_id": "capability_assignment_card_display_1b2057db",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_cards_are_arranged_vertically_in_deadl_a2717ee0",
            "table_ids": [
              "capability_assignment_card_display_1b2057db.table.assignment_display_metadata"
            ],
            "function_ids": [
              "capability_assignment_card_display_1b2057db.function.get_assignment_cards",
              "capability_assignment_card_display_1b2057db.function.create_display_metadata",
              "capability_assignment_card_display_1b2057db.function.update_display_order"
            ],
            "screen_ids": [
              "capability_assignment_card_display_1b2057db.screen.dashboard_card_view"
            ]
          },
          {
            "criterion_id": "criterion_done_when_each_assignment_appears_as_a_distinct__b2a6003e",
            "table_ids": [
              "capability_assignment_card_display_1b2057db.table.assignment_display_metadata"
            ],
            "function_ids": [
              "capability_assignment_card_display_1b2057db.function.get_assignment_cards",
              "capability_assignment_card_display_1b2057db.function.create_display_metadata"
            ],
            "screen_ids": [
              "capability_assignment_card_display_1b2057db.screen.dashboard_card_view"
            ]
          },
          {
            "criterion_id": "criterion_done_when_each_card_displays_the_assignment_titl_feb6e0f5",
            "table_ids": [
              "capability_assignment_card_display_1b2057db.table.assignment_display_metadata"
            ],
            "function_ids": [
              "capability_assignment_card_display_1b2057db.function.get_assignment_cards"
            ],
            "screen_ids": [
              "capability_assignment_card_display_1b2057db.screen.dashboard_card_view"
            ]
          }
        ],
        "traces": [
          {
            "screen_id": "capability_assignment_card_display_1b2057db.screen.dashboard_card_view",
            "action_id": "capability_assignment_card_display_1b2057db.screen-action.load_assignment_cards",
            "function_id": "capability_assignment_card_display_1b2057db.function.get_assignment_cards",
            "table_ids": [
              "capability_assignment_card_display_1b2057db.table.assignment_display_metadata"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_assignment_completion_tracking_19f07be9",
      "verification": {
        "valid": true,
        "feature_id": "capability_assignment_completion_tracking_19f07be9",
        "criteria": [],
        "traces": [
          {
            "screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
            "action_id": "capability_assignment_completion_tracking_19f07be9.screen-action.load_all_completion_statuses",
            "function_id": "capability_assignment_completion_tracking_19f07be9.function.get_all_completion_statuses",
            "table_ids": [
              "capability_assignment_completion_tracking_19f07be9.table.assignment_completion"
            ]
          },
          {
            "screen_id": "capability_assignment_completion_tracking_19f07be9.screen.dashboard_completion_display",
            "action_id": "capability_assignment_completion_tracking_19f07be9.screen-action.toggle_assignment_completion",
            "function_id": "capability_assignment_completion_tracking_19f07be9.function.update_completion_status",
            "table_ids": [
              "capability_assignment_completion_tracking_19f07be9.table.assignment_completion",
              "capability_assignment_completion_tracking_19f07be9.table.assignment_completion"
            ]
          }
        ],
        "errors": []
      }
    },
    {
      "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
      "verification": {
        "valid": true,
        "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_assignments_with_due_dates_in_the_past_2c2ac3c9",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_completed_assignments_are_not_highligh_5c03b02a",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_red_highlighting_updates_automatic_da349185",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_overdue_assignment_highlighting_a3b2e567.screen.dashboard"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_responsive_design_507cc59c",
      "verification": {
        "valid": true,
        "feature_id": "capability_responsive_design_507cc59c",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_buttons_and_interactive_elements_are_l_2519bfbf",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_responsive_design_507cc59c.screen.responsive_dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_text_remains_readable_on_both_small_an_d3c21dd0",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_responsive_design_507cc59c.screen.responsive_dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_dashboard_layout_adapts_to_phone_s_6b496b70",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_responsive_design_507cc59c.screen.responsive_dashboard"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_dashboard_layout_works_on_laptop_s_c066738b",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_responsive_design_507cc59c.screen.responsive_dashboard"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    },
    {
      "feature_id": "capability_color_coded_status_labels_b6950121",
      "verification": {
        "valid": true,
        "feature_id": "capability_color_coded_status_labels_b6950121",
        "criteria": [
          {
            "criterion_id": "criterion_done_when_completed_assignments_are_displayed_wi_ba000881",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments"
            ]
          },
          {
            "criterion_id": "criterion_done_when_overdue_assignments_are_displayed_with_ae5a47fc",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments"
            ]
          },
          {
            "criterion_id": "criterion_done_when_the_color_updates_automatically_when_a_8e229aa1",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments"
            ]
          },
          {
            "criterion_id": "criterion_done_when_upcoming_assignments_not_yet_due_are_d_92623ec3",
            "table_ids": [],
            "function_ids": [],
            "screen_ids": [
              "capability_color_coded_status_labels_b6950121.screen.dashboard_with_color_coded_assignments"
            ]
          }
        ],
        "traces": [],
        "errors": []
      }
    }
  ]
}
```

## Historical validation attempts
```json
{
  "records": [
    {
      "feature_id": "capability_add_assignment_622b64dc",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:46:54",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_add_assignment_622b64dc",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "f5bf4012c19ac1d080d603cbf3e42e8e4a6ae15009a4b4618403be424a0ca399",
      "created_at": "2026-10-14 04:47:23",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_add_assignment_622b64dc",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "008d1d60a8662f5a6fa4eebd097e8bf30725f0a4900aa227f454f11b2d259655",
      "created_at": "2026-10-14 04:47:49",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_localstorage_data_storage_c1936286",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:48:18",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_localstorage_data_storage_c1936286",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "cb084ea402201f4742ceb54a9c7107e782e971f37818cbbd5f61c28ce004e6d4",
      "created_at": "2026-10-14 04:48:52",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_localstorage_data_storage_c1936286",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "525cc491f236e50c8c616e85b5d210fe6373762e1c8c9943e7770b9d96b57631",
      "created_at": "2026-10-14 04:49:13",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_automatic_deadline_sorting_2088096a",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:49:39",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_automatic_deadline_sorting_2088096a",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "1d4bbaeb837b4bd220d9db1b2469ec8772b36c0cba26e47244fd4c862b3d1df8",
      "created_at": "2026-10-14 04:50:01",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_automatic_deadline_sorting_2088096a",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-14 04:50:31",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_single_dashboard_view_8bb5982d",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:51:10",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_single_dashboard_view_8bb5982d",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "fbfec8dee11c57e3926e720c2fa7b7adfbfd7ccf08360450a0977778e6a40453",
      "created_at": "2026-10-14 04:51:37",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_single_dashboard_view_8bb5982d",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "71b2241d0d38917282dbd920bb0169d8bb9b17759af340a9ae8466f2c348fdef",
      "created_at": "2026-10-14 04:52:00",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:52:33",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "40207d1fe03f736c420c80ff1986150edb24137e354fcc4080f55995c17384d8",
      "created_at": "2026-10-14 04:53:15",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "ed3fd0118a8294833c6c932b2035d93b768a9743671488df40e26441a6af31b9",
      "created_at": "2026-10-14 04:53:34",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_assignment_card_display_1b2057db",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:54:16",
      "last_error_code": null,
      "attempts": [
        {
          "code": "invalid_feature_database",
          "status": "validation_failed",
          "attempt": 1,
          "retryable": true,
          "detail_categories": [
            "database_table_usage_required"
          ]
        },
        {
          "code": "invalid_feature_database",
          "status": "validation_failed",
          "attempt": 2,
          "retryable": true,
          "detail_categories": [
            "table_usage_field_unresolved",
            "table_usage_unresolved"
          ]
        },
        {
          "code": null,
          "status": "accepted",
          "attempt": 3,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_assignment_card_display_1b2057db",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "199cd5d1dd48cdf9907e50354fdc320c04706527db451790d5facfe060f8adae",
      "created_at": "2026-10-14 04:54:59",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_assignment_card_display_1b2057db",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "15a1443ee20dbed8bc659ad298340c4da9a2939d179b9423458e095ada39a4b6",
      "created_at": "2026-10-14 04:55:29",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_assignment_completion_tracking_19f07be9",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:56:03",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_assignment_completion_tracking_19f07be9",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "fc3b9cb3a6a6533dd7eb421652bfc22c9f44edc282860d1f7af0b89d2798a899",
      "created_at": "2026-10-14 04:56:38",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_assignment_completion_tracking_19f07be9",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "bd3c73d6f2259aeb9aa6093b799f32bd9ed84ad3238df67f781dc3690cb52462",
      "created_at": "2026-10-14 04:57:03",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:57:21",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "2a5cad0e44ad39b3eea94b24e49a1fe3cdc6b950244d1b3f90e915b68acb7620",
      "created_at": "2026-10-14 04:57:34",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-14 04:57:58",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_responsive_design_507cc59c",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:58:13",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_responsive_design_507cc59c",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "870f45f9d8d1e78e6861d09f0a559e39fbdcacd6a4302d55ff21b3c1ce111096",
      "created_at": "2026-10-14 04:58:25",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_responsive_design_507cc59c",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-14 04:58:46",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_color_coded_status_labels_b6950121",
      "stage": "database",
      "outcome": "succeeded",
      "scope_hash": "570878f318efd780897f77222f7442468c33b2053581ce9db2fa10b6f7151a54",
      "created_at": "2026-10-14 04:59:03",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_color_coded_status_labels_b6950121",
      "stage": "backend",
      "outcome": "succeeded",
      "scope_hash": "4ba2536d8a3bfab9f9afb43dd1c1b86d70fd711c04a6e6f1d524d17633ca5062",
      "created_at": "2026-10-14 04:59:17",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    },
    {
      "feature_id": "capability_color_coded_status_labels_b6950121",
      "stage": "screens",
      "outcome": "succeeded",
      "scope_hash": "0068dc9f1ae726d17d8c3e9c5318e4cbfc6337737d7475183017cf2817b8ed26",
      "created_at": "2026-10-14 04:59:37",
      "last_error_code": null,
      "attempts": [
        {
          "code": null,
          "status": "accepted",
          "attempt": 1,
          "retryable": null,
          "detail_categories": []
        }
      ]
    }
  ]
}
```

Use feature IDs and the recorded validation details to compare tables, functions and screens. A rejected candidate is not the finalized blueprint. Missing historical details cannot be recovered.
