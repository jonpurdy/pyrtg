import json

# from pyrtg import Channel
# from pyrtg import Sensor

class Sensor(object):
    """ PRTG sensor. At this time, simply contains channels.
    """
    id = 0
    name = ""
    channels = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def add_channel(self, channel):
        self.channels.append(channel)

    def generate_xml(self):
        xml = "<prtg>\n"
        for channel in self.channels:
            xml += channel.get_xml()
        xml += "</prtg>"
        return xml

    def generate_json(self):
    	json_string = '{"prtg": {"result": ['
    	for channel in self.channels:
    		json_string += channel.get_json()
    	json_string += "]}}"
    	return json_string

class Channel(object):
    """ PRTG channel. These get added to Sensor objects.
    """

    id = 0
    name = ""
    value = 0
    extra_fields = {}

    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value

    # <LimitMinWarning>0.5</LimitMinWarning><LimitWarningMsg>Peer is not active.</LimitWarningMsg><LimitMode>1</LimitMode></result>
    def set_extra_fields(self, field_name, field_value):
        self.extra_fields[field_name] = field_value

    def get_xml(self):
        xml = "<result>"
        xml += "<channel>%s</channel><value>%s</value>" % \
              (self.name, self.value)
        # extra fields is used to set additiona stuff, ie. "LimitMinWarning"
        # without having to add all of it here
        for entry in self.extra_fields:
                xml += "<%s>%s</%s>" % (entry,self.extra_fields[entry],entry)
        xml += "</result>\n"
        return xml

    def get_json(self):
    	json_str = '{"channel": %s, "value": %s}' % (self.name, self.value)
    	return json_str

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

print(this_sensor.generate_json())
