from pathlib import Path

from fullstack import create_app


ROOT = Path(__file__).resolve().parents[1]


def test_fullstack_routes_are_served():
    client = create_app(testing=True).test_client()
    page = client.get("/")

    assert page.status_code == 200
    assert b"Add Assignment" in page.data
    assert b"Upcoming Deadlines" in page.data
    assert b"Assignment Status Tracking" in page.data
    assert b"Overdue" in page.data
    assert client.get("/app.css").status_code == 200
    assert client.get("/app.js").status_code == 200
    assert client.get("/health").get_json()["ok"] is True


def test_frontend_uses_local_storage_and_only_mvp_interactions():
    javascript = (ROOT / "frontend" / "app.js").read_text()
    html = (ROOT / "frontend" / "index.html").read_text()

    assert "localStorage" in javascript
    assert "assignment-tracker:assignments:v1" in javascript
    assert "isOverdue" in javascript
    assert "sortByDeadline" in javascript
    assert "completion-toggle" in html
    assert 'type="search"' not in html.lower()
    assert "deleteassignment" not in javascript.lower()
