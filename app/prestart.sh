#!/usr/bin/env bash

set -e

echo "Run apply migrations.."
alembic upgrade d41dd76b45c7
echo "Migrations applied!"

exec "$@"