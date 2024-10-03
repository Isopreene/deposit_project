FROM python:3.12

RUN apt-get update \
    && apt-get install -y gcc python3-dev musl-dev libmagic1 libffi-dev netcat-traditional \
    build-essential libpq-dev

COPY pyproject.toml poetry.lock /
RUN pip3 install poetry
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Copy entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app
COPY . /app
EXPOSE 8000

ENTRYPOINT ["bash", "/app/entrypoint.sh"]