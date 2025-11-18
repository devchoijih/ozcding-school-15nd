poetry run black .
if(!$?) { throw }
poetry run ruff check --select I --fix
if(!$?) { throw }
poetry run ruff check --fix
if(!$?) { throw }
poetry run mypy .
if(!$?) { throw }
poetry run pytest .
if(!$?) { throw }
Write-Host "Done" -ForegroundColor Green