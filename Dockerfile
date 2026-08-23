FROM python:3.14-slim

WORKDIR /app

#uv
COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /uvx /bin/

#copiar dependencias de uv
COPY pyproject.toml uv.lock ./

#instalar dependencias de uv
RUN uv sync --locked --no-install-project

COPY src ./src
COPY tests ./tests
COPY README.md ./

RUN uv sync --locked

CMD ["/app/.venv/bin/opswatch"]