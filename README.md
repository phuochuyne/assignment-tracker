# assignment-tracker

Simple, private assignment tracking for students. Assignment data stays in the
user's browser through LocalStorage; no usage analytics or personal data are
sent to the server.

MVP scope:

- Add Assignment
- Upcoming Deadlines
- Assignment Status Tracking
- Overdue Assignment Indicator

## Run locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/gunicorn --bind 127.0.0.1:5055 'fullstack:create_app()'
```

Open <http://127.0.0.1:5055>.

## Verify

```bash
.venv/bin/python -m pytest -q
```
