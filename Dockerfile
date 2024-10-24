FROM python:3.9-slim
RUN pip install requests
COPY iot_client.py /app/iot_client.py
CMD ["python", "/app/iot_client.py"]
