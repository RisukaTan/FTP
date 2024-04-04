import socket

Filezilla_user = "alice"
password = "35477"
Filezilla_user2 = "bob"
password2 = "999"
state = False
ok = False
connect = False

def Ascii():
    print("200 Type set to A")

def Binary():
    print("200 Type set to I")

def PW_directory():
    print ("257 '/' is current directory.")

def list_files():
    print ("200 PORT command successful.")
    print("150 Starting data transfer.")
    print("226 Operation successful")
    print("ftp: 21 bytes received in 0.00Seconds 21000.00Kbytes/sec.")
    
while True:
    line = input('ftp> ').strip()
    args = line.split()

    command = args[0]

    if command == 'quit':
        break

    elif command == 'bye':
        break

    elif command == 'open' and state == False:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect((args[1],int(args[2])))
        respon = clientSocket.recv(1024)
        result = str(respon)
        state = True
        print(result[2:28])
        print("220",end=' ')
        print(result[36:79])
        print("202 UTF8 mode is always enabled. No need to send this command")
        Name = input("User (127.0.0.1:(none)): ")
        print("331 Please, specify the password.")
        key = input("Password: ")
        if key == password or key == password2:
                print("")
                print("230 Login successful.")
                ok = True
        else:
                print("")
                print("530 Login incorrect.")
                print("Login failed.")
                ok = False
    
    elif command == 'open' and state == True:
        print("Already connected to 127.0.0.1, use disconnect first.")            
        
    elif command == 'ascii':
        Ascii()

    elif command == 'binary':
        Binary()

    elif command == 'cd':
        print("change directory to c/:")

    elif command == 'get':
        print("get file")

    elif command == 'ls':
        list_files()

    elif command == 'put':
        print("put file")

    elif command == 'pwd':
        PW_directory()

    elif command == 'rename':
        current_name = input("Frome name ")
        if current_name == Filezilla_user:
          new_name = input("To name ")
          Filezilla_user = new_name
        else:
            print("not found.")

    elif command == 'user' and ok == False and state == True:
        name = input("Username ")
        print("331 Please, specify the password.")
        key = input("Password: ")
        if key == password or key == password2:
            print("")
            print("230 Login successful.")
        else:
            print("")
            print("530 Login incorrect.")
            print("Login failed.")
    
    elif command == 'user' and ok == True and state == True:
        print("503 Already logged in. QUIT first.")
        print("Login failed.")
    
    elif command == 'user' and ok == False and state == False:
        print("Not connected.")
    

    elif command == 'close':
        clientSocket.close()
        print("221 Goodbye.")

    elif command == 'disconnect':
        clientSocket.close()
        print("221 Goodbye.")
    else:
        print("Invalid command.")