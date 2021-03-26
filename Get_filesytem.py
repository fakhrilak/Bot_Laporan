import paramiko
import time

# DC
data = [
    {"host":"10.161.4.12","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.13","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.10","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.11","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.14","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.35","uname":"root","password":"stt123"},
    {"host":"10.161.4.36","uname":"root","password":"stt123"},
    {"host":"10.161.4.37","uname":"root","password":"stt123"},
    {"host":"10.161.4.38","uname":"root","password":"stt123"},
    {"host":"10.161.4.39","uname":"root","password":"stt123"},
    {"host":"10.161.4.26","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.27","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.28","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.8.45","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.8.46","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.8.47","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.8.48","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.23","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.24","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.25","uname":"root","password":"P@ssw0rd123"},
    {"host":"10.161.4.129","uname":"root","password":"P@ssw0rd123"},
]

# DRC
# data = [
#     {"host":"10.241.56.12","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.13","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.10","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.11","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.14","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.43","uname":"root","password":"stt123"},
#     {"host":"10.241.56.44","uname":"root","password":"stt123"},
#     {"host":"10.241.56.45","uname":"root","password":"stt123"},
#     {"host":"10.241.56.46","uname":"root","password":"stt123"},
#     {"host":"10.241.56.47","uname":"root","password":"stt123"},
#     {"host":"10.241.56.35","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.36","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.37","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.29.45","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.29.46","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.29.47","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.29.48","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.32","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.33","uname":"root","password":"P@ssw0rd123"},
#     {"host":"10.241.56.34","uname":"root","password":"P@ssw0rd123"},
# ]
for i in range(len(data)):
    a= data[i]
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(a["host"], port=22, username=a["uname"], password=a["password"])


    stdin, stdout, stderr = ssh.exec_command('df -kh')
    time.sleep(1)
    b = stdout.readlines()
    for j in b:
        print(j)
    ssh.close()

# from docx import Document
# from docx.shared import Inches
# import  subprocess
# import json
# import pandas as pd
# from openpyxl import Workbook,load_workbook
# import paramiko

# wb = Workbook()
# ws = wb.active

# comments = 'df -kh'

# proc = subprocess.Popen(comments.split(), stdout=subprocess.PIPE)
# out, err = proc.communicate()
# A = json.dumps(out.decode("utf-8"))
# print(A)
# df = pd.Series(" ".join(A.strip(' b\'').strip('\'').split('\' b\'')).split('\\n'))


# result=[]
# z = 0

# for i in df:
#     result.append({z:i})
#     z+=1

# obj = load_workbook('sample.xlsx')
# sheet= obj.active
# row = ['B','C','D','E','F','G']


# for i in range(len(df)-1):
#     x = df[i].split()
#     for z in range(len(row)):
#         ws[str(row[z])+str(i+1)]= x[z]
# wb.save("sample.xlsx")
