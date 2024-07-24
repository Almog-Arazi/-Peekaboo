import RPi.GPIO as GPIO
from time import sleep

duty_cycle_min = 2.5  # Minimum duty cycle for 0 degrees
duty_cycle_max = 12.5  # Maximum duty cycle for 180 degrees

class MirrorController:
    def __init__(self, servo_pin):
        self.pwm = None
        self.servo_pin = servo_pin
        self.duty_cycle_min = 2.5  # Minimum duty cycle for 0 degrees
        self.duty_cycle_max = 12.5  # Maximum duty cycle for 180 degrees
        self.up_angle = 145
        self.down_angle = 90
        self.nudge_angle = 132

    def init_mirror_pos(self):
        self.move_down()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.servo_pin, 50)  # 50 Hz (20 ms period)
        self.pwm.start(2.5)
        
    def move_up(self):
        print("Move up - set to 160 degrees")
        self.set_angle(self.up_angle)

    def move_down(self):
        print("Move down - set to 90 degrees")
        self.set_angle(self.down_angle)
    
    def nudge(self):
        print("Nudge")
        self.set_angle(self.nudge_angle)
        self.set_angle(self.up_angle)

    def set_angle(self, angle):
        duty_cycle = (angle / 180) * (self.duty_cycle_max - self.duty_cycle_min) + self.duty_cycle_min
        self.pwm.ChangeDutyCycle(duty_cycle)
        sleep(0.2)  # Adjust this delay as needed
        self.pwm.ChangeDutyCycle(0)
        sleep(0.3)  # Adjust this delay as needed

    def cleanup(self):
        if self.pwm is not None:
            self.pwm.stop()
        GPIO.cleanup()
