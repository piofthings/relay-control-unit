import time
import os
import ntplib

class TimeSync:
    client = None
    def __init__(self):
        try:
            self.client = ntplib.NTPClient()

        except:
            print('Could not sync with time server.')

    def sync(self):
        try:
            response = self.client.request('pool.ntp.org')
            print('Setting time to: ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)));
            os.system('date ' + time.strftime('%m%d%H%M%Y.%S',time.localtime(response.tx_time)))
        except:
            print('Could not sync with time server.')
        print('Done.')
