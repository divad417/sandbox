import time
import math
import busio
import adafruit_trellism4
import adafruit_adxl34x

PIXEL_ON = (255, 255, 255)
PIXEL_OFF = (0, 0, 0)
RAD2DEG = 180/math.pi

board_scale = 0.015

board = adafruit_trellism4.TrellisM4Express(rotation=0)
i2c = busio.I2C(adafruit_trellism4.board.ACCELEROMETER_SCL, adafruit_trellism4.board.ACCELEROMETER_SDA)

board_width = board.pixels.width
board_height = board.pixels.height

accelerometer = adafruit_adxl34x.ADXL345(i2c)
# Coordinate frame: +X near side, +Y left side, +Z down

t = time.monotonic()
x, y = 0, 0
vx, vy = 0, 0
x_lit, y_lit = int(board_height*0.5), int(board_width*0.5)
board.pixels.fill(PIXEL_OFF)
board.pixels[y_lit, x_lit] = PIXEL_ON
# pressed = set(trellis.pressed_keys)


while True:
    #time.sleep(0.01)

    # Read time since last loop
    dt = time.monotonic() - t
    t = time.monotonic()

    # Read acceleration
    ax, ay, az = accelerometer.acceleration

    # Acceleration mapping to bowl

    # Integrate to get velocity
    vx, vy = vx + ax*dt, vy + ay*dt

    # Integrate to get position
    x, y = x + vx*dt, y + vy*dt

    # Limit position to size of board
    if x < -0.5 * board_height * board_scale:
        vx = 0
        x = -0.5 * board_height * board_scale
    elif x >= 0.5 * board_height * board_scale:
        vx = 0
        x = 0.499 * board_height * board_scale
    if y < -0.499 * board_width* board_scale:
        vy = 0
        y = -0.499 * board_width * board_scale
    elif y > 0.5 * board_width * board_scale:
        vy = 0
        y = 0.5 * board_width * board_scale

    # Find correct light from position
    if math.floor(x / board_scale + 0.5 * board_height) != x_lit or math.floor(-y / board_scale + 0.5 * board_width) != y_lit:
        board.pixels[y_lit, x_lit] = PIXEL_OFF
        x_lit = math.floor(x / board_scale + 0.5 * board_height) 
        y_lit = math.floor(-y / board_scale + 0.5 * board_width)
        board.pixels[y_lit, x_lit] = PIXEL_ON
