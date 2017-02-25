import signal
import sys
import time
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

sense = SenseHat()

def on_connect(client, userdata, flags, rc):
    m="Connect flags"+str(flags)+"result code "+str(rc)+" client1_id"+str(client)
    print(m)

broker_address="192.168.1.47"
client1 = mqtt.Client("P1")
client1.on_connect = on_connect

def sigterm_handler(signal, frame):
    client1.disconnect()
    client1.loop_stop()
    print("exiting..")
    sys.exit(0)

signal.signal(signal.SIGINT, sigterm_handler)

client1.connect(broker_address)
client1.loop_start()
while True:
    client1.publish("sensors/temp1", sense.get_temperature())
    time.sleep(8)
client1.disconnect()
client1.loop_stop()
