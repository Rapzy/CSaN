import socket
import struct, time

PORT = 8037
TIME1970 = 2208988800

service = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
service.bind(("", PORT))
service.listen(1)
print("listening on port", PORT)
while 1:
    # serve forever
    channel, info = service.accept()
    print("connection from", info)
    t = int(time.time()) + TIME1970
    t = struct.pack("!I", t)
    channel.send(t)
    channel.close()
