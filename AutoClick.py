from PIL import ImageGrab, Image
from pynput.mouse import Button, Controller
import cv2
import numpy as np
import time
import decimal

mouse = Controller()
accept_btn = cv2.imread("Accept!.png", 0)
w, h = accept_btn.shape[::-1]
clicked = False

while True:
	screen_img = np.array(ImageGrab.grab().convert("RGB"))
	res = cv2.matchTemplate(screen_img[:,:,0], accept_btn, eval("cv2.TM_CCOEFF_NORMED"))
	loc = np.where(res >= 0.6)

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	top_left = min_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)

	if clicked == False and len(loc) > 0:
		for pt in zip(*loc[::-1]):
			cv2.rectangle(screen_img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
			mouse.position = (pt)
			mouse.click(Button.left, 1)
			clicked = True

	if clicked == True:
		break

	time.sleep(1)
