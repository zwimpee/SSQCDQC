FROM python:3.7.2-alpine3.9 as base

# Path: Dockerfile
FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

# Path: Dockerfile
FROM base

COPY --from=builder /install /usr/local

COPY . /app

WORKDIR /app

CMD ["python", "main.py"]

    
