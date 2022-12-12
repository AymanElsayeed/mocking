def get_one():
    return 1


class Connection:

    global_data = ""

    def __init__(self, data="this is my data"):
        self.data = data

    def send_data(self):
        return self.data

    def get_data(self):
        return self.data

    def get_global_data(self):
        return self.global_data
