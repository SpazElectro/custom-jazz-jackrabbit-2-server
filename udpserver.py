import socket

from jj2.lib.protocol import ALL_PAYLOADS
import jj2.protocols.gameplay as gameplay
import jj2.lib.protocol


@gameplay.GameplayProtocol.relation(ALL_PAYLOADS, jj2.lib.protocol.If.configured(capture_packets=True))
def something(proto, payload):
    print(payload)

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', 10052))

    print("[UDP] Started")

    while True:
        data, addr = s.recvfrom(1024)

        protocol = gameplay.GameplayProtocol()
        protocol.data_received(data)

        # serverDetails = gameplay.ServerDetails(
        #     client_id=0,
        #     player_id=0,
        #     level_file_name="battle1.j2l",
        #     level_crc=1,
        #     tileset_crc=1,
        #     game_mode=gameplay.GameMode.SINGLEPLAYER,
        #     max_score=10,
        # )

        # s.sendto(serverDetails.serialize(None), addr)

        # idk wtf to send please someone help me its 11:33pm

        print("[UDP] " + str(data) + " | " + str(addr))