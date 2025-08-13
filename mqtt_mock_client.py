"""
mqtt_mock_client.py
Subscribes to mock MQTT stream for real-time updates.
"""
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"MQTT Update: {msg.topic} {msg.payload}")
    # Parse and apply updates to USD scene (mock)

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe("warehouse/update")
client.loop_start()

input("Press Enter to exit MQTT client...\n")
client.loop_stop()
client.disconnect()
