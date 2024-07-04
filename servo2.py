import time
from machine import Pin, PWM

# Nilai duty cycle untuk posisi servo
MIN_DUTY = 2000  # Nilai untuk 0 derajat
MAX_DUTY = 8000  # Nilai untuk 180 derajat

# Fungsi untuk mengonversi derajat ke duty cycle
def degree_to_duty(degree):
    return MIN_DUTY + (degree * (MAX_DUTY - MIN_DUTY) // 180)

# Inisialisasi PWM pada pin 0
pwm = PWM(Pin(0))
pwm.freq(50)  # Atur frekuensi PWM ke 50 Hz

# Fungsi untuk menggerakkan servo ke derajat tertentu
def move_servo(degree):
    duty = degree_to_duty(degree)
    pwm.duty_u16(duty)
    print(f"Moving to {degree} degrees with duty {duty}")
    time.sleep(1)

# Tes gerakan servo ke beberapa posisi
while True:
    move_servo(0)    # Gerakkan servo ke 0 derajat
    time.sleep(2)    # Tunggu 2 detik
    move_servo(90)   # Gerakkan servo ke 90 derajat
    time.sleep(2)    # Tunggu 2 detik
    move_servo(180)  # Gerakkan servo ke 180 derajat
    time.sleep(2)    # Tunggu 2 detik
