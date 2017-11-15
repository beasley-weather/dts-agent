# Need a logging service to have a record of events
import zmq

import weewx_orm


SOCK_ADDR = 'tcp://127.0.0.1:34343'


class TransferAgent:
    ACK = bytes.fromhex('06')

    def __init__(self, sock_addr):
        self._context = zmq.Context()
        self._sock_addr = sock_addr
        self._sock = self._context.socket(zmq.REP)

    def __enter__(self):
        self._sock.bind(self._sock_addr)

    def __exit(self, *args):
        self._sock.disconnect(self._sock_addr)

    def start(self):
        while True:
            data = self._sock.recv()
            self._sock.send_string(self.ACK)
            self._insert_data(data)

    def _insert_data(self, data):
        weewx_orm.archive_insert(data)
        pass


if __name__ == '__main__':
    with TransferAgent(SOCK_ADDR) as agent:
        agent.start()
