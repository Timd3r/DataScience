# ex01 — Postgres (Docker)

A small guide to start the PostgreSQL service with Docker Compose and connect to the `piscineds` database.

## Prerequisites

- Docker and Docker Compose installed
- The compose file in this folder (`docker-compose.yml`) configured to create a container named `postgres_db` with a user `tde-raev` and a database `piscineds`.

## Start the services

Run the containers in detached mode:

```bash
docker-compose up -d
```

view the logs
```bash
docker logs -f postgres_db
```


## Connect to the database

Open a shell into the Postgres container and start `psql` as user `tde-raev`:

```bash
docker exec -it postgres_db psql -U tde-raev -d piscineds -h localhost -W
```

You will be prompted for the user's password.

Alternatively run a single command from the host (useful for quick queries):

```bash
docker exec -i postgres_db psql -U tde-raev -d piscineds -c "SELECT * FROM data_2022_oct LIMIT 10;"
```

## Example: view first 10 rows

Inside `psql`, run:

```sql
SELECT * FROM data_2022_oct LIMIT 10;
```

## Stop and clean up

Stop and remove containers created by Compose:

```bash
docker-compose down
```

## Notes

- If the container name differs from `postgres_db`, adjust the `docker exec` command accordingly.
- Ensure the CSV data has been loaded into the `data_2022_oct` table before running the sample query.