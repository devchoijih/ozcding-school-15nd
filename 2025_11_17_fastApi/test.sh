#!/usr/bin/env bash
set -eo pipefail

COLOR_GREEN='tput setaf 2;'
COLOR_NC='tput sgr0'

# black = 코드 이쁘게 만들어 주는 도구
echo "Starting black"
poetry run black .
echo "OK"

# ruff = 사용하지 않는 import나 변수를 제거 해준다
echo "Starting ruff"
poetry run ruff check --select I --fix
poetry run ruff check --fix
echo "OK"

# mypy Python 타입 검사기이다 return 이나 이런걸 명시하지 않은것을 잡아줌 -> static
echo "Starting mypy"
poetry run mypy .
echo "OK"

# coverage
echo "Starting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html

echo "${COLOR_GREEN}All tests passed successfully!${COLOR_NC}"