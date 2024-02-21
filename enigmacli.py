# TODO: room_gen structure needs the host to remain in a listening state for connections instead of just
# creating the room and leaving it   
# TODO: fix "ran out of input" on client and similiar error on server, likely issue with incorrect stack on data transfer TRY: db commenting the if deleterequest
# TODO: remove all db lines, including the fake hostlist in the server 

import socket
import pickle 
import os

HOST = "18.225.117.43"
PORT = 9236
username = "anon"

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

def point_check(max): # return user input if within a range
    while True:
        try: usinp = int(input("$: "))
        except KeyboardInterrupt: quit() # ^C break
        except: continue
        if 0 <= usinp <= max: return usinp

def roomlist_load(): # List room names 
    # Request list of rooms from server
    cls()
    roomrequest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    roomrequest_socket.connect((HOST, PORT))
    roomrequest_socket.sendall(b'roomrequest')
    open_hosts = pickle.loads(roomrequest_socket.recv(1024))
    roomrequest_socket.close()

    # Print room names w/ formatting 
    print('|     room name     |\n')
    for x, roomname in enumerate(open_hosts[1:]):
        print(f'{x+1}) {roomname[2]}')
    print('____________________')
    print('\nenter room to join (0 to exit) -')
    usinp = point_check(len(open_hosts)-1) # db change -1 if last room cant be selected

    # Exit if usinp == 0
    if usinp == 0: 
        main()

    # Send request to server to delete room information 
    else:
        deleterequest = str.encode(f'deleterequest{usinp}')
        roomjoin_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        roomjoin_socket.connect((HOST, PORT))
        roomjoin_socket.sendall(deleterequest) # Send room list index to server with deleterequest
        roomjoin_socket.close()
        roomjoin_load()

def room_gen(): 
    cls()
    print("           _                \n ___ ___  (_)__ ___ _  ___ _\n/ -_) _ \/ / _ `/  ' \/ _ `/\n\__/_//_/_/\_, /_/_/_/\_,_/ \n          /___/             \n\n")
    while True:
        roomname = input("enter room name: ")
        password = input("enter room password: ")  
        if 0 < len(roomname) < 16 and 0 < len(password) < 16:
            host_info = pickle.dumps([roomname, password])
            hostgen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hostgen_socket.connect((HOST, PORT))
            hostgen_socket.sendall(host_info)
            hostgen_socket.close()
            break
        print("room name and/or password must not be longer than 16 characters\n")
    print(f"\nverify room information: \nroom name: {roomname}\nroom password: {password}")

    print("room configured, type 0 to exit")
    if point_check(1) == 1: main() 

def settings():
    cls()
    global username

    print("           _                \n ___ ___  (_)__ ___ _  ___ _\n/ -_) _ \/ / _ `/  ' \/ _ `/\n\__/_//_/_/\_, /_/_/_/\_,_/ \n          /___/             \n\n")
    print(f'1) change username ("{username}")\n2) back')
    usinp = point_check(2)
    if usinp == 1: 
        username = input("enter username: ")
        settings()

def roomjoin_load():
    pass 
    # loading screen / wait screen for host conection
    # could do a wait screen -> load screen, or have waiting integrated into the loading screen progress bar, like:
    #          [################-----------------] 43%
    #              awaiting peer establishment

def main():
    cls()

    print("           _                \n ___ ___  (_)__ ___ _  ___ _\n/ -_) _ \/ / _ `/  ' \/ _ `/\n\__/_//_/_/\_, /_/_/_/\_,_/ \n          /___/             \n\n")
    print('1) join a room\n2) create a room\n3) settings\n')

    point = point_check(3)

    if point == 1: roomlist_load()
    if point == 2: room_gen()
    if point == 3: settings()

if __name__ == "__main__":
    main()