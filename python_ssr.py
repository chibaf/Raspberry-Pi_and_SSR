# switching SSR via GPIO by python on Raspberry Pi
#
import RPi.GPIO as GPIO
import datetime
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)   # GPIO PIN No.14
def main():
  for i in range(100):
    now = datetime.datetime.now()
    print(now)
    print(i)
    GPIO.output(14,GPIO.HIGH)
    sleep(1)
    GPIO.output(14,GPIO.LOW)
    sleep(1)
try:
  main()
except KeyboardInterrupt:
  print("Keyboard Interrupt")
  GPIO.cleanup()
  exit()