import time
from machine import Pin, PWM

# Nilai duty cycle untuk posisi servo
MIN_DUTY = 2000  # Nilai untuk 0 derajat
MID_DUTY = 6000  # Nilai untuk 90 derajat
MAX_DUTY = 9000  # Nilai untuk 180 derajat

# Fungsi untuk mengonversi derajat ke duty cycle
def degree_to_duty(degree):
    return MIN_DUTY + (degree * (MAX_DUTY - MIN_DUTY) // 180)

# Inisialisasi PWM pada pin 0
servo = PWM(Pin(0))
servo.freq(50)  # Atur frekuensi PWM ke 50 Hz

# Inisialisasi push button dengan pull-up internal
button_red = Pin(16, Pin.IN, Pin.PULL_UP)
button_yellow = Pin(17, Pin.IN, Pin.PULL_UP)
button_green = Pin(13, Pin.IN, Pin.PULL_UP)

# Fungsi untuk menggerakkan servo ke derajat tertentu
def move_servo(degree):
    duty = degree_to_duty(degree)
    servo.duty_u16(duty)
    print(f"Moving to {degree} degrees with duty {duty}")
    time.sleep(1)  # Jeda untuk memberi waktu servo bergerak

while True:
    if not button_red.value():  # Tombol merah ditekan
        move_servo(0)  # Gerakkan servo ke 0 derajat
    elif not button_yellow.value():  # Tombol kuning ditekan
        move_servo(90)  # Gerakkan servo ke 90 derajat
    elif not button_green.value():  # Tombol hijau ditekan
        move_servo(180)  # Gerakkan servo ke 180 derajat
    
    time.sleep(0.1)  # Jeda kecil untuk debounce tombol
