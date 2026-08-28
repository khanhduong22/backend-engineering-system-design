#!/usr/bin/env bash
set -e

# ==============================================================================
# SonarQube Universal Scanner Runner (Contabo VPS Integration)
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Auto-load .env from repo root if it exists
if [ -f "$REPO_ROOT/.env" ]; then
  set -a
  source "$REPO_ROOT/.env"
  set +a
elif [ -f ".env" ]; then
  set -a
  source ".env"
  set +a
fi

SONAR_HOST_URL="${SONAR_HOST_URL:-https://sonar.khanhdp.com}"
SONAR_TOKEN="${SONAR_TOKEN:-}"

if [ -z "$SONAR_TOKEN" ]; then
  echo "❌ Error: SONAR_TOKEN is not set."
  echo "👉 Please create a .env file (copy from .env.example) or export SONAR_TOKEN=\"<your_token>\""
  exit 1
fi

TARGET_DIR="${1:-.}"
PROJECT_KEY="${2:-}"

if [ ! -d "$TARGET_DIR" ]; then
  echo "❌ Error: Target directory '$TARGET_DIR' does not exist."
  exit 1
fi

cd "$TARGET_DIR"

if [ -z "$PROJECT_KEY" ]; then
  # Auto-derive project key from package.json or folder basename
  if [ -f "package.json" ]; then
    PROJECT_KEY=$(node -p "try { require('./package.json').name } catch(e) { '' }" 2>/dev/null || true)
  fi
  if [ -z "$PROJECT_KEY" ]; then
    PROJECT_KEY=$(basename "$(pwd)")
  fi
fi

echo "🔍 Starting SonarQube Scan for Project: [$PROJECT_KEY] in $(pwd)..."
echo "🌐 Server: $SONAR_HOST_URL"

# Run sonar-scanner via npx
npx -y sonarqube-scanner \
  -Dsonar.host.url="$SONAR_HOST_URL" \
  -Dsonar.token="$SONAR_TOKEN" \
  -Dsonar.projectKey="$PROJECT_KEY" \
  -Dsonar.projectName="$PROJECT_KEY" \
  -Dsonar.sources=src \
  -Dsonar.sourceEncoding=UTF-8 \
  -Dsonar.exclusions="**/node_modules/**,**/dist/**,**/*.spec.ts,**/*.test.ts,**/build/**,**/.next/**"

echo "✅ Scan completed! View results at: $SONAR_HOST_URL/dashboard?id=$PROJECT_KEY"
