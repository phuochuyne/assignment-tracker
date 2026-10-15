# Backend verification

Static checks inspect Python syntax, internal import paths, declared routes/functions, file integrity and credential patterns. `database_contract` means the schema file exists; `dependency_resolution` means requirements.txt exists, not that installation succeeded. `file_integrity` is the verifier's aggregate static result. The raw evidence identifies individual errors. The checked-input package hash below covers the files before reports were added.

## Findings and next steps
No issues were recorded by these checks. This does not cover checks that were not run.

## Check evidence and coverage
```json
{
  "schema_version": "assembled-backend-verification",
  "source": {
    "architecture_session_id": "51340238-5ec3-4ffd-ae23-007949d24ae7",
    "architecture_id": "architecture:scope_assignment_tracker_fbf1a7c1:eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006",
    "architecture_source_hash": "eaff296be4ece877eaa35314c93d4cf5236fa09070aa6d0e75a931f8652b8006"
  },
  "package_hash": "4559446e8aa39f862a120576bd28031771561c1aac6583de8729fc841731028a",
  "static_valid": true,
  "passes": {
    "file_integrity": true,
    "imports": true,
    "route_map": true,
    "function_coverage": true,
    "database_contract": true,
    "dependency_resolution": true,
    "secret_scan": "[redacted]"
  },
  "features": {
    "covered": 10,
    "total": 10
  },
  "functions": {
    "covered": 17,
    "total": 17
  },
  "errors": [],
  "warnings": [],
  "non_blocking_errors": [],
  "report_hash": "8ec836e5b890d0e79c44402174dbe3aff5a882723e5491d745c6b93dd20855d3",
  "not_run": [
    "database execution",
    "dependency installation",
    "application startup",
    "pytest",
    "integration tests",
    "business behavior"
  ]
}
```

## Feature sources
```json
[
  {
    "feature_id": "capability_add_assignment_622b64dc",
    "state": "complete",
    "architecture_backend_hash": "9f2463f70506f00b70fe2726a75a49fd9804152c49c0d51f9def20e1fa9a658b",
    "database_feature_sql_hash": "06b848de58517d8bfe1fb39b58d59d30c5dfd13c584678d726e40d290f92678e",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_localstorage_data_storage_c1936286",
    "state": "complete",
    "architecture_backend_hash": "b16925d2ec5c7b4013f29bf4a83d7a7e0173f09d974a371bc2eb8b81e25dc760",
    "database_feature_sql_hash": "c5e21205190cc0a7640d62faaec29b52288ddaefef23d11c4f0bed1965b4e021",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_automatic_deadline_sorting_2088096a",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "59c9a4d5cefe79b9c2124869698cfd71ffea6b18d7529b59731c75fdb3529e06",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_single_dashboard_view_8bb5982d",
    "state": "complete",
    "architecture_backend_hash": "1b15c3b3d2ea9de8a3714a1e21d87c4d422b56e82fa6d19e9b46e7ce5f8a4c44",
    "database_feature_sql_hash": "8b4640bae4b4bf9097f605fb707b4d8cc42a3fe2e3b21e9358d79826d1d53c9f",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
    "state": "complete",
    "architecture_backend_hash": "ec86e7294862ca0314a3d028a744b6c0f3f75a46c904d18ec9c7635cad8eecbd",
    "database_feature_sql_hash": "4ca2c2552bee3ae39493eedabda85299d0ddc951c5d3d5f7b9d1bdd3d4f3c8ae",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_assignment_card_display_1b2057db",
    "state": "complete",
    "architecture_backend_hash": "74da78015b8a7b32b53abafb935c0f462b7987d658444473efa19027c1b84587",
    "database_feature_sql_hash": "6d853cf1b3554e22f4cfa60210f7f1da7984295b131d48199ccbcddeaaf3bfb5",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_assignment_completion_tracking_19f07be9",
    "state": "complete",
    "architecture_backend_hash": "b7dbf4cc854144ebf7bf8de725a9b7bf9d012cc59c80d603ed36943f54a83f9d",
    "database_feature_sql_hash": "1628c5a874c48ee7bdc78c967ae57b35a5c31aaabbb298cd8d1ff60ab33c66b7",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "2bdb824f26540e8e95a6a89e2971fd9e4accb568f69eeff8f029523ed522495b",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_responsive_design_507cc59c",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "c85a2914775192d879d0ae394aded9d6d7d71322f80f0f08b69994a1541bf35c",
    "last_error_code": null,
    "last_error_details": []
  },
  {
    "feature_id": "capability_color_coded_status_labels_b6950121",
    "state": "complete",
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "4b43e9e0a7a4cc2d4e414461caba7f7626caf48d1170a9a563d565b9a3a524a0",
    "last_error_code": null,
    "last_error_details": []
  }
]
```

## Expected feature routes and functions
```json
[
  {
    "feature_id": "capability_add_assignment_622b64dc",
    "functions": [
      {
        "id": "capability_add_assignment_622b64dc.function.create_assignment",
        "name": "create_assignment",
        "http_method": "POST",
        "route": "/api/capability_add_assignment_622b64dc/assignments",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_add_assignment_622b64dc.function.get_assignments",
        "name": "get_assignments",
        "http_method": "GET",
        "route": "/api/capability_add_assignment_622b64dc/assignments",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_localstorage_data_storage_c1936286",
    "functions": [
      {
        "id": "capability_localstorage_data_storage_c1936286.function.save_assignment",
        "name": "save_assignment",
        "http_method": "POST",
        "route": "/api/capability_localstorage_data_storage_c1936286/assignments",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_localstorage_data_storage_c1936286.function.load_assignments",
        "name": "load_assignments",
        "http_method": "GET",
        "route": "/api/capability_localstorage_data_storage_c1936286/assignments",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_localstorage_data_storage_c1936286.function.update_assignment",
        "name": "update_assignment",
        "http_method": "PUT",
        "route": "/api/capability_localstorage_data_storage_c1936286/assignments/{id}",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_localstorage_data_storage_c1936286.function.delete_assignment",
        "name": "delete_assignment",
        "http_method": "DELETE",
        "route": "/api/capability_localstorage_data_storage_c1936286/assignments/{id}",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_automatic_deadline_sorting_2088096a",
    "functions": []
  },
  {
    "feature_id": "capability_single_dashboard_view_8bb5982d",
    "functions": [
      {
        "id": "capability_single_dashboard_view_8bb5982d.function.get_dashboard_assignments",
        "name": "get_dashboard_assignments",
        "http_method": "GET",
        "route": "/api/capability_single_dashboard_view_8bb5982d/dashboard/assignments",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
    "functions": [
      {
        "id": "capability_mark_assignment_as_completed_1a7f53a5.function.toggle_assignment_completion",
        "name": "toggle_assignment_completion",
        "http_method": "PUT",
        "route": "/api/capability_mark_assignment_as_completed_1a7f53a5/assignments/{assignment_id}/completion",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_mark_assignment_as_completed_1a7f53a5.function.get_assignment_completion",
        "name": "get_assignment_completion",
        "http_method": "GET",
        "route": "/api/capability_mark_assignment_as_completed_1a7f53a5/assignments/{assignment_id}/completion",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_mark_assignment_as_completed_1a7f53a5.function.get_all_completions",
        "name": "get_all_completions",
        "http_method": "GET",
        "route": "/api/capability_mark_assignment_as_completed_1a7f53a5/assignments/completions",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_assignment_card_display_1b2057db",
    "functions": [
      {
        "id": "capability_assignment_card_display_1b2057db.function.get_assignment_cards",
        "name": "get_assignment_cards",
        "http_method": "GET",
        "route": "/api/capability_assignment_card_display_1b2057db/assignment-cards",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_assignment_card_display_1b2057db.function.create_display_metadata",
        "name": "create_display_metadata",
        "http_method": "POST",
        "route": "/api/capability_assignment_card_display_1b2057db/assignment-cards",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_assignment_card_display_1b2057db.function.update_display_order",
        "name": "update_display_order",
        "http_method": "PATCH",
        "route": "/api/capability_assignment_card_display_1b2057db/assignment-cards/{id}",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_assignment_completion_tracking_19f07be9",
    "functions": [
      {
        "id": "capability_assignment_completion_tracking_19f07be9.function.get_assignment_completion_status",
        "name": "get_assignment_completion_status",
        "http_method": "GET",
        "route": "/api/capability_assignment_completion_tracking_19f07be9/assignments/{assignment_id}/completion",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_assignment_completion_tracking_19f07be9.function.get_all_completion_statuses",
        "name": "get_all_completion_statuses",
        "http_method": "GET",
        "route": "/api/capability_assignment_completion_tracking_19f07be9/assignments/completion",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_assignment_completion_tracking_19f07be9.function.create_completion_record",
        "name": "create_completion_record",
        "http_method": "POST",
        "route": "/api/capability_assignment_completion_tracking_19f07be9/assignments/{assignment_id}/completion",
        "trigger_type": "user_action"
      },
      {
        "id": "capability_assignment_completion_tracking_19f07be9.function.update_completion_status",
        "name": "update_completion_status",
        "http_method": "PATCH",
        "route": "/api/capability_assignment_completion_tracking_19f07be9/assignments/{assignment_id}/completion",
        "trigger_type": "user_action"
      }
    ]
  },
  {
    "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
    "functions": []
  },
  {
    "feature_id": "capability_responsive_design_507cc59c",
    "functions": []
  },
  {
    "feature_id": "capability_color_coded_status_labels_b6950121",
    "functions": []
  }
]
```

## Generation and repair history

Failed attempts below are historical, not automatically defects in these files. A matching file hash identifies a checked output retained in this package. Earlier discarded evidence cannot be reconstructed. An empty history does not mean every attempt passed.

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_add_assignment_622b64dc",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/add_assignment/feature.py",
          "sha256": "5c2c5c1141f269f11446aa2479efcc8ee5da7db4980b6dc31e7856527a30f18c"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_add_assignment_622b64dc",
        "file_count": 1,
        "function_ids": [
          "capability_add_assignment_622b64dc.function.create_assignment",
          "capability_add_assignment_622b64dc.function.get_assignments"
        ],
        "function_names": [
          "create_assignment",
          "get_assignments"
        ],
        "route_count": 2,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "93c7668bb32f557585ef737b9afe7c3bb8108be1796d89ecc519018aeb8ee299"
      }
    }
  ],
  "started_at": "2026-10-15T04:35:19.016116+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_add_assignment_622b64dc",
  "screen_id": null,
  "expected_workspace_version": 1,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "9f2463f70506f00b70fe2726a75a49fd9804152c49c0d51f9def20e1fa9a658b",
    "database_feature_sql_hash": "06b848de58517d8bfe1fb39b58d59d30c5dfd13c584678d726e40d290f92678e"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:35:31.468829+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_localstorage_data_storage_c1936286",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/localstorage_data_storage/feature.py",
          "sha256": "60554449469860e46e26719dee1321e1274e3ade05c7483c341433a936b90c4d"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_localstorage_data_storage_c1936286",
        "file_count": 1,
        "function_ids": [
          "capability_localstorage_data_storage_c1936286.function.delete_assignment",
          "capability_localstorage_data_storage_c1936286.function.load_assignments",
          "capability_localstorage_data_storage_c1936286.function.save_assignment",
          "capability_localstorage_data_storage_c1936286.function.update_assignment"
        ],
        "function_names": [
          "delete_assignment",
          "load_assignments",
          "save_assignment",
          "update_assignment"
        ],
        "route_count": 4,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "7f06bf68a727a02f05889a1f938c9fab403902443dd62c8e92c7648b947039c6"
      }
    }
  ],
  "started_at": "2026-10-15T04:35:36.286508+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_localstorage_data_storage_c1936286",
  "screen_id": null,
  "expected_workspace_version": 3,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "b16925d2ec5c7b4013f29bf4a83d7a7e0173f09d974a371bc2eb8b81e25dc760",
    "database_feature_sql_hash": "c5e21205190cc0a7640d62faaec29b52288ddaefef23d11c4f0bed1965b4e021"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:36:00.812289+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_automatic_deadline_sorting_2088096a",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/automatic_deadline_sorting/feature.py",
          "sha256": "7940434a9e44e82e5062efcad89d063dd7eaa95b7c5458f51ed483332ee4c619"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_automatic_deadline_sorting_2088096a",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 3,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "0d92010aeed83e1517c148d237f46bb4fc26b39e6183dbb2de07d04c04c91acd"
      }
    }
  ],
  "started_at": "2026-10-15T04:36:05.691967+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_automatic_deadline_sorting_2088096a",
  "screen_id": null,
  "expected_workspace_version": 5,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "59c9a4d5cefe79b9c2124869698cfd71ffea6b18d7529b59731c75fdb3529e06"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:36:23.594811+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_single_dashboard_view_8bb5982d",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/single_dashboard_view/feature.py",
          "sha256": "edf17ede3cd6b51b9c2bcef22fb340983573dcd90f881fdfec29c129f060eed7"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_single_dashboard_view_8bb5982d",
        "file_count": 1,
        "function_ids": [
          "capability_single_dashboard_view_8bb5982d.function.get_dashboard_assignments"
        ],
        "function_names": [
          "get_dashboard_assignments"
        ],
        "route_count": 1,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "0f681b899ab9509a4e545331a23bf4fdcd5d9c474327ec0e09e35c4ef6358e0a"
      }
    }
  ],
  "started_at": "2026-10-15T04:36:28.041176+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_single_dashboard_view_8bb5982d",
  "screen_id": null,
  "expected_workspace_version": 7,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "1b15c3b3d2ea9de8a3714a1e21d87c4d422b56e82fa6d19e9b46e7ce5f8a4c44",
    "database_feature_sql_hash": "8b4640bae4b4bf9097f605fb707b4d8cc42a3fe2e3b21e9358d79826d1d53c9f"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:36:33.831968+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_mark_assignment_as_completed_1a7f53a5",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/mark_assignment_as_completed/feature.py",
          "sha256": "1e0f592d0ae5a1b908069c887532be4558de3ea19ce64398272ddb92048a56e9"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
        "file_count": 1,
        "function_ids": [
          "capability_mark_assignment_as_completed_1a7f53a5.function.get_all_completions",
          "capability_mark_assignment_as_completed_1a7f53a5.function.get_assignment_completion",
          "capability_mark_assignment_as_completed_1a7f53a5.function.toggle_assignment_completion"
        ],
        "function_names": [
          "get_all_completions",
          "get_assignment_completion",
          "toggle_assignment_completion"
        ],
        "route_count": 3,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "fc0f69cbd4e8faf7c4ba7ea56a9a9e351cfe5fd2c1a9919e6de6f8d45686e57d"
      }
    }
  ],
  "started_at": "2026-10-15T04:36:37.458161+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_mark_assignment_as_completed_1a7f53a5",
  "screen_id": null,
  "expected_workspace_version": 9,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "ec86e7294862ca0314a3d028a744b6c0f3f75a46c904d18ec9c7635cad8eecbd",
    "database_feature_sql_hash": "4ca2c2552bee3ae39493eedabda85299d0ddc951c5d3d5f7b9d1bdd3d4f3c8ae"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:36:51.807861+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_assignment_card_display_1b2057db",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/assignment_card_display/feature.py",
          "sha256": "1d9c7f16318ddd8865ee513e9bdac2132168ef90beb94354c2a060033104f794"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_assignment_card_display_1b2057db",
        "file_count": 1,
        "function_ids": [
          "capability_assignment_card_display_1b2057db.function.create_display_metadata",
          "capability_assignment_card_display_1b2057db.function.get_assignment_cards",
          "capability_assignment_card_display_1b2057db.function.update_display_order"
        ],
        "function_names": [
          "create_display_metadata",
          "get_assignment_cards",
          "update_display_order"
        ],
        "route_count": 3,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "419f4699d1bde4a36c2495b47809ec2e9784a3587c85a131e44bd5094592ee06"
      }
    }
  ],
  "started_at": "2026-10-15T04:36:55.924141+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_assignment_card_display_1b2057db",
  "screen_id": null,
  "expected_workspace_version": 11,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "74da78015b8a7b32b53abafb935c0f462b7987d658444473efa19027c1b84587",
    "database_feature_sql_hash": "6d853cf1b3554e22f4cfa60210f7f1da7984295b131d48199ccbcddeaaf3bfb5"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:37:15.421952+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_assignment_completion_tracking_19f07be9",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/assignment_completion_tracking/feature.py",
          "sha256": "0a1a0894546bcb30b919d14d3e9a3141c00e88193645333b22e2e2069b46551e"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_assignment_completion_tracking_19f07be9",
        "file_count": 1,
        "function_ids": [
          "capability_assignment_completion_tracking_19f07be9.function.create_completion_record",
          "capability_assignment_completion_tracking_19f07be9.function.get_all_completion_statuses",
          "capability_assignment_completion_tracking_19f07be9.function.get_assignment_completion_status",
          "capability_assignment_completion_tracking_19f07be9.function.update_completion_status"
        ],
        "function_names": [
          "create_completion_record",
          "get_all_completion_statuses",
          "get_assignment_completion_status",
          "update_completion_status"
        ],
        "route_count": 4,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "0a75353fbea4c1ae8d45d12b1a404deab9e14a66695bff06f25a35dbe4bf69ad"
      }
    }
  ],
  "started_at": "2026-10-15T04:37:20.809550+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_assignment_completion_tracking_19f07be9",
  "screen_id": null,
  "expected_workspace_version": 13,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "b7dbf4cc854144ebf7bf8de725a9b7bf9d012cc59c80d603ed36943f54a83f9d",
    "database_feature_sql_hash": "1628c5a874c48ee7bdc78c967ae57b35a5c31aaabbb298cd8d1ff60ab33c66b7"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:37:35.773791+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_overdue_assignment_highlighting_a3b2e567",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/overdue_assignment_highlighting/feature.py",
          "sha256": "60901258a285e889525bedc621260b4918229882fc055a3a273dc8c69315ccd8"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 4,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "dd8eda38d5228911f60951cee3fbbf9dd1a870583d636429a95dcb31d9b276e2"
      }
    }
  ],
  "started_at": "2026-10-15T04:37:40.640949+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_overdue_assignment_highlighting_a3b2e567",
  "screen_id": null,
  "expected_workspace_version": 15,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "2bdb824f26540e8e95a6a89e2971fd9e4accb568f69eeff8f029523ed522495b"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:38:00.388054+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_responsive_design_507cc59c",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/responsive_design/feature.py",
          "sha256": "fa20c11cc1fb7c423bc470d637693721c9cba9ef91b156210e47cc5cc2386285"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_responsive_design_507cc59c",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 3,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "c1dc8526770a79f8e2f602d32a5ee29db385b8b37cbf427a16022255a165e65e"
      }
    }
  ],
  "started_at": "2026-10-15T04:38:05.260611+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_responsive_design_507cc59c",
  "screen_id": null,
  "expected_workspace_version": 17,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "c85a2914775192d879d0ae394aded9d6d7d71322f80f0f08b69994a1541bf35c"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:38:17.840205+00:00"
}
```

### Checked output matches packaged files

```json
{
  "stage": "backend feature",
  "feature": "capability_color_coded_status_labels_b6950121",
  "screen": null,
  "outcome": "completed"
}
```

```json
{
  "stage": "backend feature",
  "tool_slug": "backend-generator",
  "checks": [
    {
      "check": "Backend syntax, functions and routes",
      "status": "passed",
      "files": [
        {
          "path": "backend/features/color_coded_status_labels/feature.py",
          "sha256": "c7e11e646a912d39dbb8925237451a6b5b2fbf1bad0597584006df9cf3b9da20"
        }
      ],
      "result": {
        "valid": true,
        "feature_id": "capability_color_coded_status_labels_b6950121",
        "file_count": 1,
        "function_ids": [],
        "function_names": [],
        "route_count": 3,
        "database_imports_valid": true,
        "non_blocking_errors": [],
        "verification_hash": "b5c849a7e778c23685a4eeaf78351eb04dadcd620450353f0a2c5f5a110bfbc4"
      }
    }
  ],
  "started_at": "2026-10-15T04:38:22.325907+00:00",
  "workspace_id": "4fa741e5-089d-4689-bc89-7a676f88e80c",
  "feature_id": "capability_color_coded_status_labels_b6950121",
  "screen_id": null,
  "expected_workspace_version": 19,
  "session_id": "33efba8f-f96e-47eb-af7e-de2bbd8afe29",
  "mvp_session_id": "aa84c450-2c65-4101-9edb-fe58b11965e7",
  "source": {
    "architecture_backend_hash": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "database_feature_sql_hash": "4b43e9e0a7a4cc2d4e414461caba7f7626caf48d1170a9a563d565b9a3a524a0"
  },
  "outcome": "completed",
  "finished_at": "2026-10-15T04:38:42.106634+00:00"
}
```
