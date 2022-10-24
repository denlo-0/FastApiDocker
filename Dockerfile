FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app
RUN pip install -e .

EXPOSE 8080
