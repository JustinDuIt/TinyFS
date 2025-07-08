class Directory:
    def __init__(self, name="", parent=None):
        self.name = name
        self.parent = parent
        self.children = {}

    def add_child(self, name, obj):
        if name in self.children:
            print("File is already in directory")
        else:
            self.children[name] = obj
    def get_child(self, name):
        if not(name in self.children):
            print("Item not found")
        else:
            return self.children[name]
    
    def remove_child(self, name):
        if not(name in self.children):
            print("Item not found")
        else:
            del self.children[name]

class File:
    def __init__(self, name="", size=0, block_indices=None):
        self.name = name
        self.size = size
        self.block_indices = block_indices or []
