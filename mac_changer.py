#!/usr/bin/env python
# importing
import subprocess
import random

# when this programm starts it shows us what devices we can edit
subprocess.call(["ifconfig"])

# the programm requires us to type the name of device
interface = input("What interface do you need? Please enter the name in the SAME WAY! \n")
# if this device is incorrect it shows message about error
if (interface == ""):
	print("Execute the programm again. This interface isn't reachable.")

# current mac adress shuts down
subprocess.call(["ifconfig", interface, "down"])


# the programm asks us to write down a new mac adress
new_mac = input("Write down please a new mac adress like this 10:20:30:40:50:60 \nor you can get a new random one, write please /random. \n")

# if user wrote phrase: /random the programm will give you a new random mac adress
if (new_mac == "/random"):
	subprocess.call(["ifconfig", interface, "hw", "ether", f"{random.randrange(10, 90)}:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}:{random.randint(10, 99)}"])
else:
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# the new mac adress turns on
subprocess.call(["ifconfig", interface, "up"])
# printing the result and showing change of mac adress
subprocess.call(["ifconfig"])