from gpiozero import OutputDevice
from time import sleep

from uuid import getnode as get_mac
mac = get_mac()

print(mac)

relay1 = OutputDevice(17, active_high=False)
relay2 = OutputDevice(27, active_high=False)

print("initialized")
action = input("Enter 1 to turn on, 0 to turn off: ")


while action !=9:
	if action == 1:
		relay1.on()
		relay2.on()
		print("on")
	elif action == 0:
		relay1.off()
		relay2.off()
		print("off")
	action = input("Enter 1 to turn on, 0 to turn off: ")

relay1.close()
relay2.close()
print("Bye")
