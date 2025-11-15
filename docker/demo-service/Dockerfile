FROM python:3.13-slim
WORKDIR /app
RUN pip install --no-cache-dir flask prometheus_client
COPY ./server.py ./
EXPOSE 8081
CMD ["python", "server.py"]
