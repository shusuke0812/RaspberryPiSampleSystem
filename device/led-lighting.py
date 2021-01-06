"""
2つのLEDを点滅させるプログラム
"""
import RPi.GPIO as GPIO
import time

# カウンタ
num = 0
# LEDのGPIO番号
green_led_pin = 2
yellow_led_pin = 3
# スリープ時間[s]
sleep_time = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(green_led_pin, GPIO.OUT)

while(num < 10):
    GPIO.output(green_led_pin, True)
    time.sleep(sleep_time)
    GPIO.output(green_led_pin, False)
    time.sleep(sleep_time)
    num += 1

GPIO.cleanup()
