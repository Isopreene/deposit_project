FROM python:3.12

RUN apt-get update && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip -r app/requirements.txt

COPY . /app

RUN pip install --upgrade pip -r app/requirements.txt

EXPOSE 8000

WORKDIR /app
ENTRYPOINT ["bash", "/app/entrypoint.sh"]