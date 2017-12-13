from gpiozero import MotionSensor
from datetime import datetime

pir = MotionSensor(4)

while True:
  pir.wait_for_motion()
  time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print (" Motion detected @ %s !" % time_now)
  pir.wait_for_no_motion()
  time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print (" Motion stopped @ %s !" % time_now)
  
  
