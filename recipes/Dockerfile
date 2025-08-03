FROM python:3.11-slim-bookworm as basic

#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y postgresql-client

FROM basic as environment

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM environment as settings


# RUN python manage.py collectstatic --clear --noinput

# RUN cp -r ./custom_data_css_img/* ./static/


# RUN groupadd -g 1000 chef && \
#    useradd -u 1000 -g 1000 -m -d /app chef

RUN if [ ! -d "/app/log" ]; then mkdir "./log"; fi \
    if [ ! -d "/app/media" ]; then mkdir "./media"; fi

RUN chown -R www-data:www-data /app

RUN chown -R www-data:www-data ./static

RUN chown -R www-data:www-data /app/log

RUN chown -R www-data:www-data /app/media

USER www-data
