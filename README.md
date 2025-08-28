# DevOps Dashboard: CI/CD Pipeline with Linting, Testing & Notifications

This starter repo sets up:
- Python sample app
- Pytest unit tests
- Pylint linting
- GitHub Actions CI
- (Optional) Slack notifications
- (Optional) Prometheus + Grafana (Docker) — add later

## Quick start
1) Create a GitHub repo and push this template.
2) Add a repository secret `SLACK_WEBHOOK_URL` (optional).
3) Commit a change — CI runs `pylint` and `pytest` automatically.
