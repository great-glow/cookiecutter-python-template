main: fix-isort fix-yapf check-code-style test check-fixtures

test:
	poetry run py.test --ff --cov {{cookiecutter.project_name}}

test-report:
	poetry run py.test --ff --cov {{cookiecutter.project_name}} --html=report.html --self-contained-html

check-fixtures:
	poetry run py.test {{cookiecutter.project_name}} --dead-fixtures --dup-fixtures

check-yapf:
	poetry run yapf -d -r -p {{cookiecutter.project_name}}

fix-yapf:
	poetry run yapf -i -r -p {{cookiecutter.project_name}}

check-isort:
	poetry run isort -c {{cookiecutter.project_name}}

fix-isort:
	poetry run isort {{cookiecutter.project_name}}

reformat-files: fix-yapf fix-isort

check-code-style: check-isort check-yapf
	poetry run flake8 {{cookiecutter.project_name}}

{%- if cookiecutter.upload_badge_to_minio_host == 'y' %}
badge:
	poetry run coverage-badge -o ./coverage.svg
	poetry run s3cmd -P -s --mime-type=image/svg+xml --host=$$MINIO_HOST --host-bucket=$$MINIO_HOST --access_key=$$MINIO_KEY --secret_key=$$MINIO_SECRET --signature-v2 --no-check-certificate --check-hostname put ./coverage.svg s3://coverage/$${GITHUB_REPOSITORY}/coverage.svg
{%- endif %}

release:
	git checkout develop
	git pull
	make test
	make check-fixtures
	make check-code-style
	poetry version patch
	git add pyproject.toml
	git commit -m "Bump version"
	git flow release start -F "v$$(poetry version --short)"
	git flow release finish -m "v$$(poetry version --short)" -F -D -p

publish:
	poetry publish --build --username=__token__ --password=$$PYPI_TOKEN
