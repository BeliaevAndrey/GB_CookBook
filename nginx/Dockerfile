FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx_https.conf /etc/nginx/conf.d
RUN mkdir -p /etc/nginx/certs
COPY ./certs/ /etc/nginx/certs/
