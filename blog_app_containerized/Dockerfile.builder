FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim AS builder

WORKDIR /app

COPY /app .
RUN uv venv
RUN pip install .

FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

WORKDIR /app

COPY --from=builder /app .

EXPOSE 1283

CMD ["uv","run","app.py"]
