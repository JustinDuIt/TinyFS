from fs_objects import Directory, File
from disk import Disk, Block

class Filesystem:
    
    def __init__(self, disk):
        self.root = Directory("root")
        self.cwd = self.root
        self.disk = disk
    
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
    def pwd(self):
        temp = self.cwd
        pwd_list = []
        while temp:
            pwd_list.append(temp.name)
            temp = temp.parent
        pwd_list.reverse()
        for item in pwd_list:
            print(item + "/", end="")
        print()
    
    def create(self, name):
        if name in self.cwd.children:
            print("File already exists")       #if file already exists
        else:
            added_file = File(name)           #create new file
            self.cwd.add_child(name, added_file)      #update cwd.children

    def write(self, name, data):
        if not (name in self.cwd.children):
            print("File doesn't exist")          #checking if file exists
        else:
            for i in range ((len(data)//64) + 1):
                allocated = self.disk.allocate(1)               #allocate 1 block for each 64 bytes of the data
                chunk  = data[i*64:(i+1)*64]
                if not chunk:
                    break                                       #Detects empty strings, happens when len(data) is exactly a multiple of 64
                self.disk.write_block(allocated[0], chunk)             #write takes in indices allocated and the data itself
                self.cwd.children[name].block_indices.append(allocated[0])   #add allocated indices to the block indices the file takes up
                self.cwd.children[name].size += len(chunk)             #update size

    def read(self, name):
        if not (name in self.cwd.children):
            print("File doesn't exist")
        else:
            blocks_to_read = self.cwd.children[name].block_indices
            for index in blocks_to_read:
                print(self.disk.read_block(index), end="")
            print()

    def rm(self, name):
        if not (name in self.cwd.children):
            print("File doesn't exist")
        else:
            for index in self.cwd.children[name].block_indices:
                self.disk.free_blocks_list[index] = True
                self.disk.block_list[index].data = ""
  
            self.cwd.remove_child(name)


            
            
                

            

