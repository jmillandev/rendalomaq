## Run test and show coverage
```
docker compose build
docker compose run --rm -p 8080:8080 django bash
coverage run -m pytest
coverage report -m
# If you see the files run:
coverage html
python -m http.server 8080
# Go to http://127.0.0.1:8080
```

## Run Server:
`docker compose build; docker compose up`

## See API documentation
1. Run server
2. Go to http://127.0.0.1:8080/redoc

## TODOs
[] TODO: Change apps structure: Move main to apps/products

[] TODO: Add Linter

[] TODO: Create a docker-compose for each enviroment(local, prod, etc)

[] TODO: Implement JSON:API

[] TODO: Add creator component instead use serializer.save()

[] TODO: Use DRF serializers as APIs contracts
