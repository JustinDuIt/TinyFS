from disk import Disk, Block
from file_system import Filesystem
from fs_objects import Directory, File

def main():
    disk = Disk()
    fs = Filesystem(disk)

    while True:
        user_input = input("> ").strip().split()

        if not user_input:
            continue

        command = user_input[0]          
        args = user_input[1:]

        if command == "mkdir" and args:
            fs.mkdir(args[0])
        elif command == "cd" and args:
            fs.cd(args[0])
        elif command == "ls":
            fs.ls()
        elif command == "pwd":
            fs.pwd()
        elif command == "create" and args:
            fs.create(args[0])
        elif command == "append" and len(args) >= 2:
            filename = args[0]
            data = " ".join(args[1:])
            fs.append(filename, data)
        elif command == "overwrite" and len(args) >= 2:
            filename = args[0]
            data = " ".join(args[1:])
            fs.overwrite(filename, data)
        elif command == "read" and args:
            fs.read(args[0])
        elif command == "rm" and args:
            fs.rm(args[0])
        elif command == "exit":
            from utils import clear_saves
            clear_saves()
            break
        elif command == "save" and args:
            fs.save(args[0])
        elif command == "load" and args:
            fs.load(args[0])
        elif command == "clear":
            from utils import clear_saves
            clear_saves()
        elif command == "rmdir":
            fs.rmdir(args[0])
        else:
            print("Unknown command or invalid arguments.")
                                                                                    
if __name__ == "__main__":
    main()
