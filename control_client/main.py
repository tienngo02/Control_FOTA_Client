import sys
from Adafruit_IO import MQTTClient
import time
import keyboard

AIO_FEED_IDs = ["fota-test.run", "fota-test.run-backward", "fota-test.turn-left", "fota-test.turn-right"]
AIO_USERNAME = "nvtien"
AIO_KEY = "...."

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)


def message(client, feed_id, payload):
    print()
    print("Received command: " + payload)
    # if feed_id == "button1":
    #     if payload == "0":
    #         writeData("1")
    #         sendCheck("1")
    #     else:
    #         writeData("2")
    #         sendCheck("2")
    # if feed_id == "button2":
    #     if payload == "0":
    #         writeData("3")
    #         sendCheck("3")
    #     else:
    #         writeData("4")
    #         sendCheck("4")


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


while True:
    if keyboard.is_pressed('w'):
        client.publish("fota-test.run", 1)
        # print("Published '1' to fota-test.run")
        # time.sleep(0.5)  # Debounce delay

    if keyboard.is_pressed('s'):
        client.publish("fota-test.run", 2)
        # print("Published '1' to fota-test.run-backward")
        time.sleep(0.5)  # Debounce delay

    if keyboard.is_pressed('a'):
        client.publish("fota-test.run", 3)
        # print("Published '1' to fota-test.turn-left")
        time.sleep(0.5)  # Debounce delay

    if keyboard.is_pressed('d'):
        client.publish("fota-test.run", 4)
        # print("Published '1' to fota-test.turn-right")
        time.sleep(0.5)  # Debounce delay

    # time.sleep(0.5)
