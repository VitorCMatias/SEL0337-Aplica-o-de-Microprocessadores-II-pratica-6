from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024,768)

camera.start_preview()
camera.annotate_text = "11803034  &  11892153"
sleep(2)
camera.capture('pratica682.jpg')
camera.stop_preview()

