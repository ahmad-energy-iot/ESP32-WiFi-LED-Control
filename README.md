# ESP32 WiFi LED Control

## Smart Home IoT Projekt mit ESP32 und MicroPython

---

#  Deutsche Dokumentation

## Projektübersicht

Dieses Projekt demonstriert die Steuerung einer externen LED über WiFi mit einem ESP32 und MicroPython.

Der ESP32 verbindet sich mit einem WLAN-Router und erstellt einen kleinen lokalen Webserver. Über einen Smartphone- oder Laptop-Browser kann die LED remote ein- und ausgeschaltet werden.

Das Projekt ist ein praktischer Einstieg in:

- IoT (Internet of Things)
- Smart Home Systeme
- WiFi Kommunikation
- Webserver mit ESP32
- MicroPython Programmierung

---

## Projektfunktionen

- ESP32 WiFi Verbindung
- Webserver mit MicroPython
- Remote LED-Steuerung
- Browserbasierte Steuerung
- HTTP Kommunikation
- Smart Home Grundlagen

---

## Verwendete Komponenten

| Komponente | Beschreibung |
|---|---|
| ESP32 DevKit V1 | Mikrocontroller-Board |
| LED | Visuelle Ausgabe |
| Widerstand | Schutz der LED |
| Breadboard | Schaltungsaufbau |
| Jumper Kabel | Elektrische Verbindungen |
| MicroPython | Programmiersprache |

---

## Schaltungsaufbau

GPIO5 → LED → Widerstand → GND

---

## Verwendete Technologien

- ESP32
- MicroPython
- WiFi Networking
- Socket Programming
- HTML
- IoT Basics

---

## Projektbilder

### ESP32 WiFi LED Steuerung

![ESP32 WiFi LED Control](images/esp32_wifi_led_1.jpg)

### Steuerung über Smartphone Browser

![ESP32 Smartphone Control](images/esp32_wifi_led_2.jpg)

---

## Python Code

```python
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

while True:

    client, addr = server.accept()

    print('Client connected from', addr)

    request = client.recv(1024)
    request = str(request)

    print(request)

    if '/on' in request:
        led.on()

    if '/off' in request:
        led.off()

    html = """
    <html>
    <head>
        <title>ESP32 Smart Home</title>
    </head>
    <body>
        <h1>ESP32 WiFi LED Control</h1>
        <a href="/on"><button>LED ON</button></a>
        <a href="/off"><button>LED OFF</button></a>
    </body>
    </html>
    """

    client.send(html)
    client.close()
```

---

## Projekt starten

1. ESP32 mit dem Computer verbinden.
2. Thonny IDE öffnen.
3. Den Code als `main.py` speichern.
4. WLAN-Name und Passwort eingeben.
5. Programm starten.
6. Die IP-Adresse aus der Shell kopieren.
7. Die IP-Adresse im Smartphone-Browser öffnen.
8. LED über die Webseite steuern.

---

## Zukünftige Erweiterungen

- Mehrere LEDs steuern
- Temperatursensor Integration
- Luftfeuchtigkeitssensor
- Relaissteuerung
- Smart Energy Monitoring
- IoT Dashboard
- Internetsteuerung
- KI-basierte Automatisierung

---

# 🇬🇧 English Documentation

## Smart Home IoT Project using ESP32 and MicroPython

---

## Project Overview

This project demonstrates controlling an external LED over WiFi using ESP32 and MicroPython.

The ESP32 connects to a WiFi router and creates a small local web server. Using a smartphone or laptop browser, the LED can be turned ON and OFF remotely.

This project is a practical introduction to:

- IoT (Internet of Things)
- Smart Home systems
- WiFi communication
- ESP32 web servers
- MicroPython programming

---

## Project Features

- ESP32 WiFi connection
- Web server using MicroPython
- Remote LED control
- Browser-based control interface
- HTTP communication
- Smart Home basics

---

## Components Used

| Component | Description |
|---|---|
| ESP32 DevKit V1 | Microcontroller board |
| LED | Visual output |
| Resistor | LED protection |
| Breadboard | Circuit prototyping |
| Jumper Wires | Electrical connections |
| MicroPython | Programming language |

---

## Circuit Wiring

GPIO5 → LED → Resistor → GND

---

## Technologies Used

- ESP32
- MicroPython
- WiFi Networking
- Socket Programming
- HTML
- IoT Basics

---

## Project Images

### ESP32 WiFi LED Control

![ESP32 WiFi LED Control](images/esp32_wifi_led_1.jpg)

### Smartphone Browser Control

![ESP32 Smartphone Control](images/esp32_wifi_led_2.jpg)

---

## Python Code

```python
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

while True:

    client, addr = server.accept()

    print('Client connected from', addr)

    request = client.recv(1024)
    request = str(request)

    print(request)

    if '/on' in request:
        led.on()

    if '/off' in request:
        led.off()

    html = """
    <html>
    <head>
        <title>ESP32 Smart Home</title>
    </head>
    <body>
        <h1>ESP32 WiFi LED Control</h1>
        <a href="/on"><button>LED ON</button></a>
        <a href="/off"><button>LED OFF</button></a>
    </body>
    </html>
    """

    client.send(html)
    client.close()
```

---

## How to Run the Project

1. Connect ESP32 to the computer.
2. Open Thonny IDE.
3. Save the code as `main.py`.
4. Enter your WiFi name and password.
5. Run the program.
6. Copy the ESP32 IP address from the shell.
7. Open the IP address in your smartphone browser.
8. Control the LED remotely.

---

## Future Improvements

- Multiple LED control
- Temperature sensor integration
- Humidity monitoring
- Relay module control
- Smart energy monitoring
- IoT dashboard
- Remote internet control
- AI-based automation

---

## Author

**Ahmad Azroun**  
Renewable Energy Manager | IoT & AI Specialist | Smart Energy Systems Developer
