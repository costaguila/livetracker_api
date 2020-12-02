# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
# DOCKER TASKS
# Build the container
# TODO: When launching to production implment docker-build.yml
#build: ## Build the container release
#	docker-compose -f docker-build.yml build

# Build the container
build-nc: ## Build the container without caching
	docker-compose build --no-cache

# Build and run the container
up: ## Spin up the project
	docker-compose up --build

stop: ## Stop running containers
	docker-compose stop

down: ## Down running containers
	docker-compose down

clean: stop ## Stop and clean running containers
	docker-compose down -v
