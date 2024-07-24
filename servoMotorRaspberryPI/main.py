from src.mirror_controller import MirrorController
from time import sleep
import RPi.GPIO as GPIO

servo_pin = 11

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servo_pin, GPIO.OUT)

if __name__ == "__main__":
    print("starting")
    setup_gpio()

    mirror = MirrorController(servo_pin)
    mirror.setup()
    mirror.init_mirror_pos()

    try:    
        while True:
            print("Moving up")
            mirror.move_up()  # Moves the mirror up
            sleep(5)  # Wait for 5 seconds

            print("Nudging")
            mirror.nudge()  # Nudges the mirror
            sleep(2)  # Wait for 2 seconds after nudging

            print("Moving down")
            mirror.move_down()  # Moves the mirror down
            sleep(5)  # Wait for another 5 seconds
    except KeyboardInterrupt:
        pass
    finally:
        mirror.cleanup()
        GPIO.cleanup()
        print("finished")
