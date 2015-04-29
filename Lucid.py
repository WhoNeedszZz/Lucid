__author__ = 'Michael J. Cusack'

import asyncio

class Lucid(asyncio.Protocol):

    def __init__(self):
        self.host = "localhost"
        self.port = 1357

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        print(data)

    #def connection_lost(self, exc):

    def start(self):
        reader, writer = yield from asyncio.open_connection(self.host, self.port)
        writer.write(b'SYN')

        line = reader.readline()
        print(line)

        writer.close()


if __name__ == "__main__":
    app = Lucid()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.start())