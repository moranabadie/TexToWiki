class Links():
    def __init__(self):
        self.list = []
    def add(self, ref, chapter):
        self.list.append(Link(ref, chapter))
    def look_for(self, n):
        for l in self.list:
            if l.ref == n:
                return l
        return None
class Link():
    def __init__(self, ref, chapter):
        self.ref = ref
        self.chapter = chapter + 1
        
        