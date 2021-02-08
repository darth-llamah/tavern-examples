
start:
	docker-compose up -d

stop:
	docker-compose stop

clean:
	docker-compose down --rmi all --volumes 2>/dev/null

bash:
	docker-compose exec -e COLUMNS="`tput cols`" -e LINES="`tput lines`" app bash

serve:
	docker-compose exec app python server/server.py

TEST_PATH=tavern/
test:
	docker-compose exec app pytest $(TEST_PATH)
