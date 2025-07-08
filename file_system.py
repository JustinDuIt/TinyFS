from  fs_objects import Directory, File

class Filesystem:
        def __init__(self, root):
            self.root = Directory("root")
            