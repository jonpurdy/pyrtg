import json

from pyrtg import Channel
from pyrtg import Sensor

print("=== Testing Channel class")

channel_id = 1
channel_name = "name1"
channel_value = "100"

this_channel = Channel(channel_id, channel_name, channel_value)

if channel_id == this_channel.id:
	print("channel_id PASS")
else:
	print("channel_id FAIL")

if channel_name == this_channel.name:
	print("channel_name PASS")
else:
	print("channel_name FAIL")

if channel_value == this_channel.value:
	print("channel_value PASS")
else:
	print("channel_value FAIL")

print("%s" % this_channel.get_xml())

print("=== Testing extra fields")

this_channel.set_extra_fields("testfield", 4)
print("%s" % this_channel.get_xml())

print("=== Testing Sensor class")

sensor_id = 1
sensor_name = "sensor1"

this_sensor = Sensor(sensor_id, sensor_name)

if sensor_id == this_sensor.id:
	print("sensor_id PASS")
else:
	print("sensor_id FAIL")

if sensor_name == this_sensor.name:
	print("sensor_name PASS")
else:
	print("sensor_name FAIL")

print("=== Testing if channel can be added to sensor")

this_sensor.add_channel(channel=this_channel)

for channel in this_sensor.channels:
	print(channel.get_xml())

print("=== Testing sensor output")

print(this_sensor.generate_xml())