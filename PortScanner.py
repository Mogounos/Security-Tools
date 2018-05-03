''' ScannerJS.py - 2018/4/7 - This file implements a
    simple port scanner using the built-in Python socker library'''

import socket

# =====================================================================

if (__name__)==('__main__') :

    MyDoubleLine = "="*50

    # Get host ID from user (ex. 127.0.0.1)

    MyRemoteServer = input("Enter a host to scan > ")
    MyRemoteServerIP = socket.gethostbyname(MyRemoteServer)

        # echo HOSTID back to user

    print(MyDoubleLine)
    print("Scanning Host : ", MyRemoteServerIP)
    print(MyDoubleLine)

    try:
        for MyPort in range (1, 1025) :
            print("Scanning : ", MyPort)
            MySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            MyConnectionResult = MySock.connect_ex((MyRemoteServerIP, MyPort))
            if(MyConnectionResult == 0) :
                print(MyRemoteServerIP+":"+str(MyPort)+"\t Open.")
                MySock.close()
                
    except socket.gaierror:
        print("Error: Unresolved Hostname"+MyRemoteServerIP)
    except socket.error:
        print("Error: Unable to Connect to "+MyRemoteServerIP)
    except KeyboardInterrupt :
        print("User Pressed Ctrl+C")

        # print end of report message

    print(MyDoubleLine)
    print("Scan Completed.")
    print(MyDoubleLine)
            
