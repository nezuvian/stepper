from time import sleep
import pigpio

class Stepper(object):
  pi = pigpio.pi()

  DIR_PIN = 20     # Direction GPIO Pin
  STEP_PIN = 21    # Step GPIO Pin

  MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
  RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
  DIRECTION = pigpio.HIGH

  SPEED = 0 # currently between 0-5999

  def __init__(self):
    self.pi.set_mode(self.DIR_PIN, pigpio.OUTPUT)
    self.pi.set_mode(self.STEP_PIN, pigpio.OUTPUT)
    self.setResolution('Full')

  def __del__(self):
    self.pi.stop()

  def flipDirection(self):
    if self.DIRECTION == pigpio.HIGH:
      self.DIRECTION = pigpio.LOW
    else:
      self.DIRECTION = pigpio.HIGH

  def setDirection(self, dir):
    self.DIRECTION = dir

  def start(self, startSpeed=500):
    self.pi.set_PWM_dutycycle(self.STEP_PIN, 128)  # PWM 1/2 On 1/2 Off
    self.pi.set_PWM_frequency(self.STEP_PIN, startSpeed)  # 0-5999 pulses per second
    self.pi.write(self.DIR_PIN, self.DIRECTION)

  def stop(self):
    self.pi.set_PWM_dutycycle(self.STEP_PIN, 0)  # PWM off

  def setResolution(self, resolutionName):
    if (resolutionName in self.RESOLUTION.keys()):
      for i in range(3):
        self.pi.write(self.MODE[i], self.RESOLUTION[resolutionName][i])
    else:
      print "wrong resolution name"

  def setSpeed(self, speed):
    if (speed < 0 or speed > 6000):
      print "wrong speed"
    else:
      self.SPEED = speed
      self.pi.set_PWM_frequency(self.STEP_PIN, self.SPEED)

