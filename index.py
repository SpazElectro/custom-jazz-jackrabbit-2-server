import tcpserver, udpserver
import threading

threading.Thread(target=udpserver.start).run()
threading.Thread(target=tcpserver.start).run()
