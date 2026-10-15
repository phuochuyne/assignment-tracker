# Database verification

SQL assembly concatenates the approved feature SQL into `database/schema.sql`. Generation checks table coverage and SQL structure; it does not execute the schema against MySQL. Constraints, migrations and queries have not been proven by these checks.

```json
{
  "records": [
    {
      "session_id": "3f846ac6-028e-46ae-b76e-855d451a1857",
      "source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "state": "completed",
      "manifest_hash": "799c02cc201738895392ee1865eec83157db0530c30c22dfb933c1dc1e504b2d"
    }
  ]
}
```

## Current SQL revisions

```json
{
  "records": [
    {
      "feature_id": "capability_add_assignment_622b64dc",
      "state": "approved",
      "revision": 1,
      "last_run_id": "2edf335f-5aa5-42e3-a187-d3600727495b",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_localstorage_data_storage_c1936286",
      "state": "approved",
      "revision": 1,
      "last_run_id": "a912858c-40ae-438e-a92a-765b7d5e2b74",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_automatic_deadline_sorting_2088096a",
      "state": "approved",
      "revision": 1,
      "last_run_id": "c288eb35-bf7d-433e-91b1-f3cc93a7da91",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_single_dashboard_view_8bb5982d",
      "state": "approved",
      "revision": 1,
      "last_run_id": "ab092b3e-b769-4c57-9593-d95be82a480a",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
      "state": "approved",
      "revision": 1,
      "last_run_id": "df062681-ae58-43b1-aac8-b38d3f18c69c",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_assignment_card_display_1b2057db",
      "state": "approved",
      "revision": 1,
      "last_run_id": "6a33840b-f1bb-4bfb-9908-2c0adcf51c47",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_assignment_completion_tracking_19f07be9",
      "state": "approved",
      "revision": 1,
      "last_run_id": "26e08959-cdb4-4e57-b029-6629507d6d6c",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
      "state": "approved",
      "revision": 1,
      "last_run_id": "e30c4f21-88d8-40de-bfcc-614afde55ac0",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_responsive_design_507cc59c",
      "state": "approved",
      "revision": 1,
      "last_run_id": "71656fd1-f7c0-480d-9bab-79baaf620c15",
      "last_error_code": null,
      "last_error_details": null
    },
    {
      "feature_id": "capability_color_coded_status_labels_b6950121",
      "state": "approved",
      "revision": 1,
      "last_run_id": "e571fe7e-d81c-49eb-8519-9dffeb0227ff",
      "last_error_code": null,
      "last_error_details": null
    }
  ]
}
```

## Run history
Compare each feature's last_run_id with these run IDs. Failed/superseded runs are historical; compare source hashes.

```json
{
  "records": [
    {
      "id": "2edf335f-5aa5-42e3-a187-d3600727495b",
      "scope_key": "feature:capability_add_assignment_622b64dc",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:32:53",
      "finished_at": "2026-10-15 04:32:55",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 2314,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "a912858c-40ae-438e-a92a-765b7d5e2b74",
      "scope_key": "feature:capability_localstorage_data_storage_c1936286",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:33:09",
      "finished_at": "2026-10-15 04:33:11",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 2545,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "c288eb35-bf7d-433e-91b1-f3cc93a7da91",
      "scope_key": "feature:capability_automatic_deadline_sorting_2088096a",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:33:18",
      "finished_at": "2026-10-15 04:33:18",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "ab092b3e-b769-4c57-9593-d95be82a480a",
      "scope_key": "feature:capability_single_dashboard_view_8bb5982d",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:33:30",
      "finished_at": "2026-10-15 04:33:33",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 2664,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "df062681-ae58-43b1-aac8-b38d3f18c69c",
      "scope_key": "feature:capability_mark_assignment_as_completed_1a7f53a5",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:33:40",
      "finished_at": "2026-10-15 04:33:43",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 2557,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "6a33840b-f1bb-4bfb-9908-2c0adcf51c47",
      "scope_key": "feature:capability_assignment_card_display_1b2057db",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:33:48",
      "finished_at": "2026-10-15 04:33:52",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 3191,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "26e08959-cdb4-4e57-b029-6629507d6d6c",
      "scope_key": "feature:capability_assignment_completion_tracking_19f07be9",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:33:58",
      "finished_at": "2026-10-15 04:34:01",
      "error_code": null,
      "error_details": [],
      "provider_attempts": [
        {
          "phase": "initial",
          "outcome": "candidate",
          "provider": "openai",
          "duration_ms": 2459,
          "stop_reason": "tool_use",
          "timeout_seconds": 70
        }
      ]
    },
    {
      "id": "e30c4f21-88d8-40de-bfcc-614afde55ac0",
      "scope_key": "feature:capability_overdue_assignment_highlighting_a3b2e567",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:34:08",
      "finished_at": "2026-10-15 04:34:08",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "71656fd1-f7c0-480d-9bab-79baaf620c15",
      "scope_key": "feature:capability_responsive_design_507cc59c",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:34:13",
      "finished_at": "2026-10-15 04:34:14",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    },
    {
      "id": "e571fe7e-d81c-49eb-8519-9dffeb0227ff",
      "scope_key": "feature:capability_color_coded_status_labels_b6950121",
      "kind": "feature_generate",
      "status": "succeeded",
      "expected_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
      "created_at": "2026-10-15 04:34:18",
      "finished_at": "2026-10-15 04:34:18",
      "error_code": null,
      "error_details": [],
      "provider_attempts": []
    }
  ]
}
```


For a recorded table/SQL error, inspect the identified table in `database/schema.sql` and the run details. Apply the schema to a local MySQL database following the README to obtain actual database execution results. If no cause or location was captured, it is unknown; missing history is not a pass.
