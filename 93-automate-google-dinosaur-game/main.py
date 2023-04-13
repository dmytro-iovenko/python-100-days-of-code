import pyautogui as gui
import keyboard
import time


def get_pixel(image, x, y):
     
    px = image.load()
    return px[x, y]


def start():
  
    # set size of the image to be taken
    x, y, width, height = 0, 102, 1920, 872
  
    # calculating time
    jumping_time = 0
    last_jumping_time = 0
    current_jumping_time = 0
    last_interval_time = 0
  
    # interval for bot to find obstacles
    y_search1, y_search2, x_start, x_end = 557, 486, 400, 415
    y_search_for_bird = 460
  
    # allowing 3s to switch the interface to Google Chrome 
    # after the program is executed
    time.sleep(3)
    while True:
        t1 = time.time()
       # press q to exit the robot
        if keyboard.is_pressed('q'):
            break
  
        sct_img = gui.screenshot(region=(x, y, width, height))
        sct_img.save("dino.jpg")
  
        # get the background color of the screenshot image
        bg_color = get_pixel(sct_img, 100, 100)


start()
