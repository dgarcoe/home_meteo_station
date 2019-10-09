import board
import digitalio
import busio
import time
import adafruit_bme280
from influxdb import InfluxDBClient

json_body = [
    {
        "measurement": "home_meteo",
        "fields": {
            "temperature": 0,
            "pressure": 0,
            "humidity": 0
        }
    }
]

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c,address=0x76)

client = InfluxDBClient('influxdb', 8086, 'raspie', 'raspie', 'casa_meteo')

while True:
    
    json_body[0]["fields"]["temperature"] = bme280.temperature
    json_body[0]["fields"]["pressure"] = bme280.pressure
    json_body[0]["fields"]["humidity"] = bme280.humidity

    client.write_points(json_body)

    time.sleep(5*60)
