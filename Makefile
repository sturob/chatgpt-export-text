help: ## Show this help
	@echo "\nSpecify a command. The choices are:\n"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[0;36m%-12s\033[m %s\n", $$1, $$2}'
	@echo ""
.PHONY: help

clean: ## clean up everything
	@rm -rf json-data/
	@rm -rf chats/
.PHONY: clean

extract: ## extract the zip file from OpenAI
	@unzip *.zip -d json-data/
.PHONY: extract

format-json: ## not needed but useful for debugging 
	@jq . json-data/conversations.json > json-data/formatted-conversations.json
.PHONY: format-json

parse: ## json2text - output goes in chats/
	@python3 parse.py
.PHONY: parse
