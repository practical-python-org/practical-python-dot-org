.PHONY: run, strict, pre-commit

all: run

run:
	uv run zensical serve

strict:
	uv run zensical build --strict

pre-commit:
	uv run --dev pre-commit run --all-files
