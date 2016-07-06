import pygame
import pygame.camera
import time
from threading import Timer
import os
from time import sleep

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def getNewImageName():
	directory = '/home/rajesh/Pictures/allpics/'
	if not os.path.exists(directory):
		os.makedirs(directory)
	return directory+time.strftime("%Y_%m_%d-%H_%M_%S")+'.jpg'

def getPicture():
    pygame.camera.init()
    pygame.camera.list_cameras() #Camera detected or not
    cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam.start()
    img = cam.get_image()
    imageName = getNewImageName()
    pygame.image.save(img,imageName)
    cam.stop()

def main():
    getPicture()
    rt = RepeatedTimer(300, getPicture)

if __name__ == '__main__':
    main()