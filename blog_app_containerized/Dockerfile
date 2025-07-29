FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

WORKDIR /app

COPY /app . 


RUN uv venv
RUN uv pip install .

EXPOSE 1283

CMD ["uv", "run", "app.py"]


