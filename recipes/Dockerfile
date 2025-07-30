FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN groupadd -g 1000 myuser && \
    useradd -u 1000 -g 1000 -m -d /app myuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chown -R myuser:myuser /app
USER myuser

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["/app/entrypoint.sh"]