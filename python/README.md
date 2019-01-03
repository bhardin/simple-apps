# Python simple app

An app that only responds to a root request.

```
GET /

{
"code": 200,
"status": "success"
}
```

Anything else, results in 404.

## Docker

This app is containerized using Docker.

```bash
docker-compose up
```

Once this process runs, open localhost:8000.
