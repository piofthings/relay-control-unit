import json

class Payload(object):
    def __init__(self, json_def):
        s = json.loads(json_def)
        self.id = None if 'id' not in s else s['id']
        self.state = None if 'state' not in s else s['state']
