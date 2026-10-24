#!/usr/bin/env bash

set -euo pipefail

BASE_URL="${1:-http://127.0.0.1:8000}"
BASE_URL="${BASE_URL%/}"

echo "Checking API at $BASE_URL"

echo "1. Testing application and database health..."

curl -fsS --max-time 10 "$BASE_URL/health" |
python3 -c '
import json
import sys

response = json.load(sys.stdin)

assert response.get("status") == "healthy"
assert response.get("database") == "connected"

print("PASS: API and database healthy")
'

echo "2. Testing incidents endpoint..."

curl -fsS --max-time 10 "$BASE_URL/incidents" |
python3 -c '
import json
import sys

incidents = json.load(sys.stdin)

assert isinstance(incidents, list)

print(f"PASS: {len(incidents)} incidents retrieved")
'

echo "All smoke tests passed."
