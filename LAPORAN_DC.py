import pyautogui
import time
import pyscreenshot as ImageGrab
import  subprocess
from datetime import  datetime


create_dc="mkdir DC"
create_drc="mkdir DRC"
route = "/home/fakhril/Documents/PEMOGRAMAN/PYTHON/cursor_move/"

subprocess.run(["mkdir", datetime.today().strftime("%d %h %y")])
subprocess.Popen(create_dc.split(), stdout=subprocess.PIPE,cwd= route + datetime.today().strftime("%d %h %y"))
subprocess.Popen(create_drc.split(), stdout=subprocess.PIPE,cwd= route + datetime.today().strftime("%d %h %y"))

array_Host = [169,156,191,227,260,296,331,368,399,434,470,502,540,572,608,643,677,710,747,779,815]
# array_get1 = [498,590,450,438,490,383,378,376,391,382,553,529,552,556,553,570,588,628,637,650]
# array_get2 = [327,403,473,480,423,460,479,481,440,444,460,459,454,459,484,449,464,478,464,444]


delay = 5
time.sleep(5)
n = 0
for i in range(len(array_Host)):
    # klik host
    pyautogui.click(454, array_Host[i]) 
    time.sleep(delay)

    ##tambahkan kordinat tiap host
        #scrol ambil helth
    # pyautogui.click(1596,670)
    # time.sleep(delay)

    #helth
    n+=1
    pyautogui.click(1059,345)
    time.sleep(delay)
    im = ImageGrab.grab(bbox=(90, 270, 1500, 700))
    im.save(datetime.today().strftime("%d %h %y")+"/DC"+"/"+ str(n) +".png")
    time.sleep(delay)
    # pyautogui.click(109,228)
    # time.sleep(delay)
    pyautogui.click(1480,240)
    time.sleep(delay)


    # pyautogui.click(1596,130)
    # time.sleep(delay)
    #memory usage
    # pyautogui.click(727,515) #crome
    n+=1
    pyautogui.click(1338,662) #2
    time.sleep(delay)
    im = ImageGrab.grab(bbox=(90, 270, 1500, 700))
    im.save(datetime.today().strftime("%d %h %y")+"/DC"+"/"+ str(n) +".png")
    time.sleep(delay)
    # pyautogui.click(109,228)
    # time.sleep(delay)
    pyautogui.click(1480,240)
    time.sleep(delay)

    #cpu usage
    n+=1
    pyautogui.click(1338,822) #2
    time.sleep(delay)
    im = ImageGrab.grab(bbox=(90, 270, 1500, 700))
    im.save(datetime.today().strftime("%d %h %y")+"/DC"+"/"+ str(n) +".png")
    time.sleep(delay)
    # pyautogui.click(109,228)
    # time.sleep(delay)
    pyautogui.click(1480,240)
    time.sleep(delay)

    #network
    n+=1
    pyautogui.click(1341,503)
    time.sleep(delay)
    im = ImageGrab.grab(bbox=(90, 270, 1500, 700))
    im.save(datetime.today().strftime("%d %h %y")+"/DC"+"/"+ str(n) +".png")
    time.sleep(delay)
    # pyautogui.click(109,228)
    # time.sleep(delay)
    pyautogui.click(1480,240)
    time.sleep(delay)

    #disklatecy
    n+=1
    pyautogui.click(1060,501)
    time.sleep(delay)
    im = ImageGrab.grab(bbox=(90, 270, 1500, 700))
    im.save(datetime.today().strftime("%d %h %y")+"/DC"+"/"+ str(n) +".png")
    time.sleep(delay)
    # pyautogui.click(109,228)
    # time.sleep(delay)
    pyautogui.click(1478,242)
    time.sleep(delay)

    # klik back
    pyautogui.click(19, 83)
    time.sleep(delay)
    # klik scroll
    pyautogui.click(1593, 877)
    time.sleep(delay)
import  DC