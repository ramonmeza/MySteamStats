FROM python:3.12 AS builder

WORKDIR /app

RUN pip install poetry==1.7.0

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

ENV TAILWINDCSS_DIR=/opt/tailwindcss
RUN mkdir -p ${TAILWINDCSS_DIR}
RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64
RUN chmod +x tailwindcss-linux-x64
RUN mv tailwindcss-linux-x64 ${TAILWINDCSS_DIR}/tailwindcss


FROM python:3.12-slim AS runtime

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"
ENV TAILWINDCSS_DIR=/opt/tailwindcss

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=builder ${TAILWINDCSS_DIR} ${TAILWINDCSS_DIR}

COPY server ./server
COPY public ./public

COPY tailwind.config.js ./tailwind.config.js
COPY tailwind.css ./tailwind.css
RUN ${TAILWINDCSS_DIR}/tailwindcss -c ./tailwind.config.js -i ./tailwind.css -o ./public/css/styles.css

EXPOSE 8000/tcp

ENTRYPOINT ["uvicorn", "server.__main__:app", "--host", "0.0.0.0"]
