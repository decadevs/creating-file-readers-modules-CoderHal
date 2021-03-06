class OpenFile:
    def __init__(self, filename):
        self.filename = filename
        # self.mode = mode

    def __enter__(self):
        self.file = open(self.filename)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
