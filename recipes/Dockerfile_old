FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y postgresql-client

RUN groupadd -g 1000 chef && \
    useradd -u 1000 -g 1000 -m -d /app chef

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown -R chef:chef /app
USER chef

ENTRYPOINT ["/app/entrypoint.sh"]
