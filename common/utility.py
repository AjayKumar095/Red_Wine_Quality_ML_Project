import sys
import pickle



class modelpreprocessing:
    
    def __init__(self):
        pass
    
    def save_obj(self, obj,file_path:str):
        
        try:
            
            with open(file_path, 'wb') as file_obj:
                pickle.dump(obj, file=file_obj)
                
            return 'obj save'    
                
        except Exception as e:
            return e    
    
