# Tavern demo

## Requirements:
Install using pip:
* flask
* pytest
* tavern

## Start demo server:
* server will be available at `http://localhost:3000/`
```bash
export FLASK_APP=server.py
flask run
```

## Available endpoints:
* `/hello-world`
  * GET, params: upper (True/False)
* `/get-secret`
  * GET
* `/check-secret`
  * POST, json keys: `secret`
* `/double`
  * POST, json keys: `number`
