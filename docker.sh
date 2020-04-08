#!/usr/bin/env bash
docker stop $(docker ps -q)
docker run -e APP_SETTINGS=config.ProductionConfig -e DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/notifications -p 5000:5000 sse-project