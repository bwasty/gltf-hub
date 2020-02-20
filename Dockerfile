FROM python:3.8-buster as base

RUN apt-get update && apt-get install -y \
    postgresql-client \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install
COPY . .

RUN groupadd -r -g 1000 appuser && \
    useradd --no-log-init -r -u 1000 -g appuser appuser --create-home
USER appuser

WORKDIR /app/gltf_hub
EXPOSE 8000

FROM base as dev
RUN echo 'source /app/aliases.sh' >> /home/appuser/.bashrc
CMD ["python", "manage.py", "runserver", "0:8000"]

FROM base as prod
USER root
RUN chmod 777 static
USER appuser
RUN python manage.py collectstatic --noinput

# TODO!: config file? log format?
CMD ["uvicorn", "--host", "0", "gltf_hub.asgi:application"]
