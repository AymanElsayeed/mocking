

class RedisClient:

    def __init__(self, data="this is my data"):
        self.data = data

    def send_data(self):
        return self.data

    def get_data(self):
        return self.data
