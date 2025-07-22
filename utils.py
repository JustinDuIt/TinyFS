import os
import shutil

def clear_saves(directory="."):
    removed = 0
    for filename in os.listdir(directory):
        if filename.endswith(".pkl"):
            try:
                os.remove(os.path.join(directory, filename))
                removed += 1
            except Exception as e:
                print(f"Failed to delete {filename}: {e}")
    

    pycache_path  = os.path.join(directory, "__pycache__")
    
    if os.path.isdir(pycache_path):
        try:
            shutil.rmtree(pycache_path)
        except Exception as e:
            print(f"Failed to remove __pycache__: {e}")
        
    print(f"Removed {removed} save file(s).")

            
        


 