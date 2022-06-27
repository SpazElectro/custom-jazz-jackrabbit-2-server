import tcpserver, udpserver
import threading

threading.Thread(target=udpserver.start).start()
threading.Thread(target=tcpserver.start).start()
