FROM python:3.10.12

RUN apt-get update && apt-get install -y python3-dev libc-dev gcc musl-dev wkhtmltopdf

WORKDIR /app

RUN pip install --upgrade pip setuptools
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./ /app/shop_garden

RUN chmod +x /app/shop_garden/docker/shop_garden/server-entrypoint.sh
RUN chmod +x /app/shop_garden/docker/shop_garden/worker-entrypoint.sh
