ARG PYTHON_VERSION=3.11
FROM python:$PYTHON_VERSION
ARG PIPX_VERSION=1.2.0 POETRY_VERSION=1.5.1
ENV PATH=/opt/pipx/bin:/app/.venv/bin:$PATH PIPX_BIN_DIR=/opt/pipx/bin PIPX_HOME=/opt/pipx/home POETRY_VIRTUALENVS_IN_PROJECT=true
COPY poetry.lock pyproject.toml /app/
WORKDIR /app
RUN python -m pip install --no-cache-dir --upgrade pip "pipx==$PIPX_VERSION" && \
  pipx install "poetry==$POETRY_VERSION" && \
  poetry install --no-dev --no-interaction --no-root
COPY telegram_bot /app/telegram_bot
ENTRYPOINT ["python"]
CMD ["-m", "telegram_bot"]