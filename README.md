ESP32 WiFi LED Control

Smart Home IoT Projekt mit ESP32 und MicroPython

Dieses Projekt demonstriert die Steuerung einer externen LED über WiFi mit ESP32 und MicroPython.

Der ESP32 verbindet sich mit einem WLAN-Router und erstellt einen kleinen Webserver.
Über den Smartphone- oder Laptop-Browser kann die LED remote ein- und ausgeschaltet werden.

---

Projektfunktionen

- ESP32 WiFi Verbindung
- Webserver mit MicroPython
- Remote LED-Steuerung
- Smart Home Grundprojekt
- HTTP-Kommunikation
- Browserbasierte Steuerung

---

Verwendete Komponenten

Komponente| Beschreibung
ESP32 DevKit V1| Mikrocontroller-Board
LED| Visuelle Ausgabe
Widerstand| Schutz der LED
Breadboard| Schaltungsaufbau
Jumper Kabel| Elektrische Verbindungen
MicroPython| Programmiersprache

---

Schaltungsaufbau

GPIO5 → LED → Widerstand → GND

---

Verwendete Technologien

- ESP32
- MicroPython
- WiFi-Netzwerke
- Socket Programmierung
- HTML
- IoT Grundlagen

---

Funktionsweise

1. ESP32 verbindet sich mit dem WLAN.
2. ESP32 erstellt einen lokalen Webserver.
3. Der Browser sendet ON/OFF Befehle.
4. ESP32 empfängt die Anfrage.
5. GPIO5 steuert die LED.

---

Weboberfläche

Die Webseite zeigt:

- LED ON
- LED OFF

Tasten zur Steuerung der LED über den Browser.

---

Python Code

import network
import socket
from machine import Pin

ssid = 'Your_WiFi_Name'
password = 'Your_WiFi_Password'

led = Pin(5, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

while True:
    client, addr = server.accept()

    request = client.recv(1024)
    request = str(request)

    if '/on' in request:
        led.on()

    if '/off' in request:
        led.off()

    html = '''
    <html>
    <body>
    <h1>ESP32 WiFi LED Control</h1>
    <a href="/on"><button>LED ON</button></a>
    <a href="/off"><button>LED OFF</button></a>
    </body>
    </html>
    '''

    client.send(html)
    client.close()

---

Projekt starten

1. ESP32 mit dem Computer verbinden.
2. Thonny IDE öffnen.
3. Den Code als "main.py" speichern.
4. WLAN-Name und Passwort eingeben.
5. Programm starten.
6. Die IP-Adresse aus der Shell kopieren.
7. Die IP-Adresse im Smartphone-Browser öffnen.
8. LED remote steuern.

---

Zukünftige Erweiterungen

- Mehrere LEDs steuern
- Temperatursensor Integration
- Luftfeuchtigkeitssensor
- Relaissteuerung
- Smart Energy Monitoring
- IoT Dashboard
- Internetsteuerung
- KI-basierte Automatisierung

---

English Documentation

Smart Home IoT Project using ESP32 and MicroPython

This project demonstrates controlling an external LED over WiFi using ESP32 and MicroPython.

The ESP32 connects to a WiFi router and creates a small web server.
Using a smartphone or laptop browser, the LED can be turned ON and OFF remotely.

---

Project Features

- ESP32 WiFi connection
- Web server using MicroPython
- Remote LED control
- Smart Home prototype
- HTTP communication
- Browser-based control interface

---

Components Used

Component| Description
ESP32 DevKit V1| Microcontroller board
LED| Visual output
Resistor| LED protection
Breadboard| Circuit prototyping
Jumper Wires| Electrical connections
MicroPython| Programming language

---

Circuit Wiring

GPIO5 → LED → Resistor → GND

---

Technologies Used

- ESP32
- MicroPython
- WiFi Networking
- Socket Programming
- HTML
- IoT Basics

---

How It Works

1. ESP32 connects to the WiFi router.
2. ESP32 creates a local web server.
3. The browser sends ON/OFF requests.
4. ESP32 receives the request.
5. GPIO5 controls the LED.

---

Web Interface

The webpage displays:

- LED ON
- LED OFF

Buttons for controlling the LED remotely.

---

Python Code

import network
import socket
from machine import Pin

ssid = 'Your_WiFi_Name'
password = 'Your_WiFi_Password'

led = Pin(5, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

while True:
    client, addr = server.accept()

    request = client.recv(1024)
    request = str(request)

    if '/on' in request:
        led.on()

    if '/off' in request:
        led.off()

    html = '''
    <html>
    <body>
    <h1>ESP32 WiFi LED Control</h1>
    <a href="/on"><button>LED ON</button></a>
    <a href="/off"><button>LED OFF</button></a>
    </body>
    </html>
    '''

    client.send(html)
    client.close()

---

How to Run the Project

1. Connect ESP32 to the computer.
2. Open Thonny IDE.
3. Save the code as "main.py".
4. Enter your WiFi name and password.
5. Run the program.
6. Copy the ESP32 IP address from the shell.
7. Open the IP address in your smartphone browser.
8. Control the LED remotely.

---

Future Improvements

- Multiple LED control
- Temperature sensor integration
- Humidity monitoring
- Relay module control
- Smart energy monitoring
- IoT dashboard
- Remote internet control
- AI-based automation

---

Author

Ahmad Azroun
Renewable Energy Manager | IoT & AI Specialist | Smart Energy Systems Developer
