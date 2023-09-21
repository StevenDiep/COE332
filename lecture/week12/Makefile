NAME ?= wallen

all: ps-me im-me

im-me:
	docker images | grep ${NAME}

ps-me:
	docker ps -a | grep ${NAME}


