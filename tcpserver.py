import socket

from jj2.protocols import gameplay

players = []

def start():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 10052))
    s.listen(5)

    gamemode = gameplay.GameMode.SINGLEPLAYER
    
    print("[TCP] Started")

    while True:
        conn, addr = s.accept()
        
        serverDetails = gameplay.ServerDetails(
            client_id=len(players),
            player_id=len(players),
            level_file_name="battle1.j2l",
            level_crc=1,
            tileset_crc=1,
            game_mode=gamemode,
            max_score=10,
        )

        conn.send(serverDetails.serialize(None))
        
        print("[TCP] " + conn, addr)
        
        conn.close()
