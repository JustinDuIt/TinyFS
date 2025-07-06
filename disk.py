
class Disk:
    
    def __init__(self):
        self.block_list = []
        self.free_blocks_list = []
        for i in range(128):
            obj = Block()                          #Creating a list of 128 empty Block objects   Constructor
            self.block_list.append(obj)
            self.free_blocks_list.append(True)      #Creating a list of 128 True/False for empty/nonempty
    
    def allocate(self, n_blocks):
        allocated = []
        for index, space in enumerate(self.free_blocks_list):
            if space and len(allocated) < n_blocks:                      #Creates an allocation list with indexes allocated
                allocated.append(index)                                  #Changes those indexes in free_blocks_list to false
                self.free_blocks_list[index] = False
        return allocated
    def write_block(self, index):
        
    def read_block(self):

     

class Block:
    def __init__(self, data_input=""):                          #Block Constructor
        self.data = data_input                    