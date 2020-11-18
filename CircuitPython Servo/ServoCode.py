import board
import servo
import pulseio
import time

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

while True:
    my_servo.angle = 0
    time.sleep(1)
    my_servo.angle = 180
    time.sleep(1)
