import debug
from paho.mqtt import client as mqtt_client

class MQTT(object):
    def __init__(self, data, matrix,scheduler):
        self.data = data
        if self.data.config.mqtt_enabled:
            self.data.mqtt_client = self.connect_mqtt()
            self.data.mqtt_client.loop_start()

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                debug.info("Connected to MQTT Broker!")
            else:
                debug.info("Failed to connect to MQTT Broker! return code %d\n", rc)

        client = mqtt_client.Client("NHL-LED-SCOREBOARD")
        client.username_pw_set(self.data.config.mqtt_username, self.data.config.mqtt_password)
        client.on_connect = on_connect
        client.connect(self.data.config.mqtt_broker_host, self.data.config.mqtt_broker_port)
        return client
