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
# GPIOの設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(green_led_pin, GPIO.OUT)

# 関数
def led_lighting(gpio: int, sleep_time: int):
    GPIO.output(gpio, True)
    time.sleep(sleep_time)
    GPIO.output(gpio, False)
    time.sleep(sleep_time)

# メイン処理
while(num < 10):
    led_lighting(green_led_pin, sleep_time)
    num += 1

GPIO.cleanup()

