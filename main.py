from stepper import Stepper
from time import sleep

stepper = Stepper()

try:
    print "start"
    stepper.start()  
    for i in range(1,5):
        stepper.setSpeed(i*200)
        print i*200
        sleep(1)
    print "stop"
    stepper.stop()
    sleep(.2)
    print "flip"
    stepper.flipDirection()        
    stepper.start()
    sleep(5)
    print "stop"
    stepper.stop()

except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
finally:
    stepper.stop()
