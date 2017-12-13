from gpiozero import MotionSensor
from datetime import datetime

pir = MotionSensor(4)

while True
  pir.wait_for_motion()
  time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print (" Motion detected @ %s !" % time_now)
