import logging
import json
import paho.mqtt.client as mqtt
from .setups import exam_setup

log = logging.basicConfig()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("alg/cmd")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    msg = msg.payload.decode("utf-8")

    try:
        msg_json = json.loads(msg)
    except json.JSONDecodeError as e:
        log.error("Error when decoding json: %s", e)
        return

    if msg_json["cmd"] != "calculate_movements":
        return

    # A JSON message in the following response is expected:
    # { "cmd": "calculate_movements", "payload": { "cc": "id", "setup": "...", "table_positions": [ ] } }
    client.publish(topic="cc/" + msg_json["payload"]["cc"] + "/status", payload="busy", qos=1)

    if msg_json["payload"]["setup"] == "exam":
        exam_setup.ExamSetup(client).execute()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect("localhost", 1883, 60)
except ConnectionError as e:
    log.error("Error when connecting to the MQTT broker: %s", e)
    exit(1)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
