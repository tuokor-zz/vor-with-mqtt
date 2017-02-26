# MQTT support for Vör
Project purpose is to change Vör to use mqtt protocol instead of
socket.io since it's much more suitable for embedded devices and
we can leverage mqtt brokers to do heavy lifting.

## Current state
 - Vör backend has support for mqtt via mqtt.js
 - raspberrypi demo that uses raspi 3 with sensehat and sends mqtt temp reading

## Local setup

Follow Vör README but also:
 1. Install mosquitto mqtt broker
 2. In raspberry pi install sensehat python module https://pythonhosted.org/sense-hat/
 3. Make sure ip address in python script points to mosquitto
 4. start mosquitto (default settings should be enough)
 5. start Vör ```npm run server```
 6. start raspberry script ```python3 mqtt-test.py```

## Next steps
 - Remove socket.io completely and update mobile apps
 - Maybe create nice dashboard in backend to show sensor readings