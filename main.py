from disk import Disk, Block
from file_system import Filesystem
from fs_objects import Directory, File

def main():
    
    disk = disk()
    fs = Filesystem(disk)

    while True:
        user_input = input()
        fs.user_input()
