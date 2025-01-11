from datetime import datetime

EXPECTED_TOKEN_STORAGE_AFTER_OWNER_QUERY: list[tuple[str, datetime]] = [
    ("not_expired_token", datetime(2025, 1, 6, 0, 0, 0)),
    ("92f3dcfc-6457-4248-8a29-18b164a2a29a", datetime(2025, 1, 7, 12, 0, 0)),
]
EXPECTED_TOKEN_STORAGE_AFTER_NOT_OWNER_QUERY: list[tuple[str, datetime]] = [
    ("not_expired_token", datetime(2025, 1, 6)),
    ("92f3dcfc-6457-4248-8a29-18b164a2a29", datetime(2025, 1, 1)),
    ("expired_token", datetime(2025, 1, 3))
]