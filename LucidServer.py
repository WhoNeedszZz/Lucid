__author__ = 'Michael J. Cusack'

import asyncio

class LucidServer(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        if data == b'SYN':
            self.transport.write(b'ACK')

    def connection_lost(self, exc):
        serv.close()


if __name__== "__main__":
    loop = asyncio.get_event_loop()
    serv = loop.run_until_complete(loop.create_server(LucidServer, "localhost", 1357))
    loop.run_until_complete(serv.wait_closed())