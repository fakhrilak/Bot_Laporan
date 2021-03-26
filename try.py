import pyautogui
import time
import pyscreenshot as ImageGrab
from datetime import  datetime
import  subprocess
import paramiko

# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('127.0.0.1', port=22, username='fakhril', password='fakhrilak')


# stdin, stdout, stderr = ssh.exec_command('df -kh')
# time.sleep(0.1) # some enviroment maybe need this.

# print (stdout.readlines())
# ssh.close()


# create_dc="mkdir DC"
# create_drc="mkdir DRC"
# route = "/home/fakhril/Documents/PEMOGRAMAN/PYTHON/cursor_move/"
# subprocess.run(["mkdir", datetime.today().strftime("%d %h %y")])
# time.sle
# subprocess.Popen(create_dc.split(), stdout=subprocess.PIPE,cwd= route + datetime.today().strftime("%d %h %y"))
# subprocess.Popen(create_drc.split(), stdout=subprocess.PIPE,cwd= route + datetime.today().strftime("%d %h %y"))

#array_Host = [172,149,186,223,261,297,331,368,404,442,472,515,553,589,626,661,698,736,772,808]
#array_get1 = [498,533,450,512,490,383,378,376,391,382,553,529,552,556,553,570,586,648,648,623]
#array_get2 = [299,510,473,277,423,460,479,481,440,444,460,459,454,459,484,449,449,421,420,462]
# time.sleep(3)
# im = ImageGrab.grab(bbox=(90, 270, 1500, 75))
# im.show()

##bccdhcmdr01.customs.go.id Point(x=454, y=157) print(pyautogui.position())
##bccdhcmdr02.customs.go.id Point(x=442, y=194) print(pyautogui.position())
while True:
    print("start")
    time.sleep(3)
    print(pyautogui.position())
    time.sleep(3)
##Point(x=21, y=83)
# pyautogui.click(100, 100)
#pyautogui.moveTo(1163, 900)
# pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
# pyautogui.dragTo(100, 150)
# pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down
# cursor_y = 157
#cursor_x = 454
# # cursor_y = 157
#Point(x=527, y=256) ///


# Point(x=109, y=228) close ss
# Point(x=1596, y=486) scroll bar ambil helth
# Point(x=1049, y=177) helth
# Point(x=1593, y=157) scroll bar ambil selain helth
# Point(x=734, y=515) memory usage
# Point(x=730, y=337) cpu usage
# Point(x=733, y=696) hostnetwork
# Point(x=1048, y=696) disk latency


# array_Host = [157,194,228,262,299,333,369,401,439,473,508,544,578,612,647,683,718,754,787,823]
# delay = 4

# for i in range(len(array_Host)):
#     pyautogui.click(454, array_Host[i]-14)
#     time.sleep(delay)
#     pyautogui.click(21, 83)
#     time.sleep(delay)
#     pyautogui.click(1593, 877)
#     time.sleep(delay)

##posisi_mozila = helth = x=1043, y=368 , host_memory_usage = x=1355, y=725