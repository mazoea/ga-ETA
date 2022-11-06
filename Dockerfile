FROM python:3.10-slim
COPY requirements.txt  /tmp
RUN pip3 install -r /tmp/requirements.txt --no-cache-dir && \
    rm /tmp/requirements.txt

COPY main.py /app

WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]