FROM python:3.7-alpine

RUN adduser -D sse_project

WORKDIR /home/sse_project

COPY . .

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache --virtual .build-deps linux-headers
RUN apk add redis

RUN python3 -m venv venv
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN chmod +x boot.sh

ENV SSE_PROJECT notifications.py

RUN chown -R sse_project:sse_project ./
USER sse_project

EXPOSE 5000

CMD ["./boot.sh"]