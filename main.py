import network
import socket
from machine import Pin

# WiFi credentials
ssid = 'Your_WiFi_Name'
password = 'Your_WiFi_Password'

# LED connected to GPIO5
led = Pin(5, Pin.OUT)

# Connect ESP32 to WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

print("Connecting to WiFi...")

# Wait until connection is successful
while not wifi.isconnected():
    pass

print("Connected!")
print(wifi.ifconfig())

# Create Web Server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Server running...")

# Main loop
while True:

    # Wait for a client connection
    client, addr = server.accept()

    print('Client connected from', addr)

    # Receive browser request
    request = client.recv(1024)

    # Convert request to string
    request = str(request)

    print(request)

    # Turn LED ON
    if '/on' in request:
        led.on()

    # Turn LED OFF
    if '/off' in request:
        led.off()

    # HTML Web Page
    html = """
    <html>

    <head>
        <title>ESP32 Smart Home</title>
    </head>

    <body>
        <h1>ESP32 WiFi LED Control</h1>

        <a href="/on">
            <button>LED ON</button>
        </a>

        <a href="/off">
            <button>LED OFF</button>
        </a>

    </body>

    </html>
    """

    # Send webpage to browser
    client.send(html)

    # Close connection
    client.close()