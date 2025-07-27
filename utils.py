import os
import shutil

def clear_saves(directory="."):
    removed = 0
    for filename in os.listdir(directory):        #searching for .pkl file
        if filename.endswith(".pkl"):
            try:
                os.remove(os.path.join(directory, filename))     #.join creates the path with directory and filename
                removed += 1
            except Exception as e:
                print(f"Failed to delete {filename}: {e}")
    

    pycache_path  = os.path.join(directory, "__pycache__")     #deleting the pycache folder
    
    if os.path.isdir(pycache_path):     #verifying the folder is there
        try:
            shutil.rmtree(pycache_path)     #remove the folder and contents using tree recursion
        except Exception as e:
            print(f"Failed to remove __pycache__: {e}")
        
    print(f"Removed {removed} save file(s).")

            
        


 