README
------
April 1-3, 2016
This project was done for HackCU 2016.
Project Members: Manohar Karthikeyan, Pravin Venkatesh, Swapnil Paratey

Objective: The project involves using Photon boards [https://www.particle.io/]
to create a wi-fi based GET/PUSH system that transfers sensor information when
requested through these RESTful APIs. The Photons were interfaced with Grove 
sensors [http://www.seeedstudio.com/wiki/Grove_System] with each module 
consisting of temperature, light, sound and touch sensors transmitting data
when requested through GET/POST calls from Python scripts or any other means.

An Amazon Echo device was used as a user interface to access sensor data and 
control LEDs connected to the Photon thereby demonstrating remote control of 
electronic circuits. Please refer to circuit diagram/schematic for details 
about implementation of circuit.

Overall, the following development scheme was used
1) Got Photons working with Wi-Fi [Photon documentation at particle.io]
2) Tried examples on the Photon through online IDE [build.particle.io]
3) Interfaced sensors to the Photon
4) Requested sensor data through a Python script [GetSensitivity.py]
5) Wrote Photon code on online IDE [allsensors.ino] This is Arduino based.
Note: Although this is Arduino based, at this moment of time in human history
Photon boards and products didn't have proper I2C communication 2-wire libraries
and the decision to use a 3-Axis Rate Gyro was abandanoed due to this.
6) node.js is required to be installed in the system to have a working debug 
terminal that can be used to debug the Photon boards incase the Wi-Fi method fails.
7) Particle online IDE was used to flash code into the Photons remotely without
any physical serial connection with the user laptop (although a USB was still 
connected though, it was addressed as a power port).
8) Programming the Echo was the most important part. Lambda functions were
created for specifying separate skills which would be updated based on user's
request [lambda_function_AWS]. Intents were described on the developers page. 
The following two pages were primarily used
- https://console.aws.amazon.com/lambda
- https://developer.amazon.com/ask [And then navigate to Apps -> Alexa] and
define your intents for the new skill that you want the Echo device to have.
For example, the project consisted of interfacing the Echo through Wifi to the
Photons using GET/POST RESTful APIs and retrieving sensor information when 
required.
9) A local Python script was also querying the senors all the time irrelevant of
the Amazon Echo (which would query only real-time). The Python script would 
store all sensor information along with sensor device ID and timestamps in a 
comma separated values (CSV file). Please refer to getSensitivity.py for more 
details about this Python script. 
10) Finally the repo also consists of Particle Photon sensor device drivers for Windows. 
11) As a final exercise, Keysight's new diagnostic software BenchVue was used to 
probe sensor data and create workflows for acquiring and managing sensor data 
whenever required.

Hardware
- Amazon Echo Device
- Breadboards and jumper wires
- Grove sensors x2 (light, sound, temperature and touch)
- LEDs connected to Photons
- Photon devices for GET/POST receivals which were heavily distributed.
- USB Serial Cables (not FTDI, but everyone had Type-C connectors).

Software Used
- Online Particle.io IDE [build.particle.io]
- Online Particle.io documentation
- Amazon EC2 cluster setup for Pythons script to store datas in CSV
- Arduino based