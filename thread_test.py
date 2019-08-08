#!/usr/local/bin/python3
import threading
import time

class DiagnosticSession(threading.Thread):
    def __init__(self):
        super(DiagnosticSession, self).__init__()
        self._done = threading.Event()

    def run(self):
        while not self._done.is_set():
            # Send the heartbeat keepalive message
            print('beat ...')
            time.sleep(1)

    def stop(self):
        self._done.set()



if __name__ == "__main__":
    # Define and startup a thread to send a heartbeat command
    session = DiagnosticSession()
    session.start()
    
    # Body of the main function
    data = input()
    session.stop()
    print(data)