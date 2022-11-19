## Run test and show coverage
```
docker-compose run --rm -p 8080:8080 django bash
coverage run -m pytest
coverage report -m
# If you see the files run:
coverage html
python -m http.server 8080
# Go to http://127.0.0.1:8080
```
