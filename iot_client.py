import requests
import time
import random

# URL till InfluxDB API
url = "http://influxdb:8086/api/v2/write?org=my-org&bucket=my-bucket&precision=s"
headers = {
    "Authorization": "Token GfvLcrbNLzCpxNpJeo6Ct2idHDoKB-26AypVnDzeWXQP5GfrgWpivoc9qxMa-ciJiGB-1s9wJvgJXf2BnJREEg==",
    "Content-Type": "text/plain"
}

def send_sensor_data():
    temperature = random.uniform(20.0, 30.0)
    payload = f"temperature,location=room1 value={temperature}"
    response = requests.post(url, headers=headers, data=payload)
    print(f"Sent data: {temperature} - Response: {response.status_code}")

while True:
    send_sensor_data()
    time.sleep(10)
