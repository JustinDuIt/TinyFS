from  fs_objects import Directory, File

class Filesystem:
    
    def __init__(self, root):
        self.root = Directory("root")
        self.cwd = self.root
    
    def mkdir(self, name):
        if name in self.cwd.children:
            print("Duplicate name")
        else:
            new_direc = Directory(name, self.cwd)
            self.cwd.add_child(name, new_direc)
    
    def cd(self, name):
        if name == "..":
            if self.cwd == self.root:
                print("Already at root")
            else:
                self.cwd = self.cwd.parent
        else:
            if not (name in self.cwd.children):
                print("File not found")
            else:
                if isinstance(self.cwd.children[name], File):
                    print("Can't cd into file")
                else:
                    self.cwd = self.cwd.children[name]
    
    def ls(self):
        for name in self.cwd.children:
            if isinstance(self.cwd.children[name], Directory):
                print(name + "/")
            else:
                print (name, " ")