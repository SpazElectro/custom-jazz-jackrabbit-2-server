import socket

from jj2.lib.protocol import ALL_PAYLOADS
import jj2.protocols.gameplay as gameplay
import jj2.lib.protocol

players = []

@gameplay.GameplayProtocol.relation(ALL_PAYLOADS, jj2.lib.protocol.If.configured(capture_packets=True))
def something(proto, payload):
    print(payload)

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 10052))

    gamemode = gameplay.GameMode.SINGLEPLAYER

    while True:
        data, addr = s.recvfrom(1024)

        serverDetails = gameplay.ServerDetails()
        serverDetails.struct.client_id = players.__len__()
        serverDetails.struct.player_id = players.__len__() + 1
        serverDetails.struct.level_filename = "battle1"
        serverDetails.struct.level_crc = 1
        serverDetails.struct.tileset_crc = 1
        serverDetails.struct.gameMode = gamemode
        serverDetails.struct.maxScore = 10
        
        protocol = gameplay.GameplayProtocol()
        protocol.data_received(data)

        players.append(addr)

        bytes_serverDetails = bytes(serverDetails.data().__str__(), "utf-8")
        s.sendto(bytes_serverDetails, addr)

        print(str(data) + " | " + str(addr))