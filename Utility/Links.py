class Links():
    def __init__(self):
        self.list = []
        self.nb_fig = 0
        self.refs = []
        self.commands = "\n"
    def get_nb_fig(self, namefig):
        self.nb_fig = self.nb_fig + 1
        self.refs.append(["Figure " + str(self.nb_fig), namefig])
        return "Figure " + str(self.nb_fig)
    def add(self, ref, chapter):
        self.list.append(Link(ref, chapter))
    def look_for(self, n):
        for l in self.list:
            if l.ref == n:
                return l
        return None
    def add_command(self, c):
        self.commands += "\n" + c
class Link():
    def __init__(self, ref, chapter):
        self.ref = ref
        self.chapter = chapter + 1
        
        