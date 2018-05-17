class Chapter():
    def __init__(self, name):
        self.list = []
        self.info = ChapterInfo(name)
    def add(self, name, file_link):
        self.list.append(ChapterInfo(name, file_link))
class ChapterInfo():
    def __init__(self, name, file_link = ""):
        self.name = name
        self.file_link = file_link