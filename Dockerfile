FROM python:3.8-buster

RUN apt-get update && apt-get install -y \
    postgresql-client \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir poetry \
 && poetry config virtualenvs.create false

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY . .

RUN groupadd -r -g 1000 appuser && \
    useradd --no-log-init -r -u 1000 -g appuser appuser --create-home
USER appuser
RUN echo 'source /app/aliases.sh' >> /home/appuser/.bashrc

WORKDIR /app/gltf_hub

# TODO!!: uvicorn or whatever...
CMD [ "python", "manage.py", "runserver", "0:8000" ]
