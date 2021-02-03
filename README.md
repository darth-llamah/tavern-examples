# Tavern demo
Simple Docker image with Tavern and Flask (for the simple server) installed.
All changes done to files are 

## Available Makefile commands
1. To build the container:
```bash
make start
```
2. To stop the container:
```bash
make stop
```
3. To remove container:
```bash
make clean
```
4. To start a simple API server (Ctrl+C to quit):
```bash
make serve
```
5. To run Tavern tests
```bash
make test
```
6. To run Tavern test using a specific file:
* Docker can access only project directory and subdirectories
```bash
make test path/to/file.tavern.yaml
```

## Manual setup (without Docker)
### Install requirements:
```bash
python3 -m pip install -r requirements.txt --user
```

### Start simple server:
* server will be available at `http://localhost:5000/`, Ctrl+C to quit:
```bash
python3 server/server.py
```

### Run tests:
* all files in given directory:
```bash
pytest tavern/
```
* single file:
```bash
pytest path/to/file.tavern.yaml
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
