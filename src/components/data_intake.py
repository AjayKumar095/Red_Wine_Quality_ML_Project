from common.utility import modelpreprocessing

model=modelpreprocessing    ()

text='try to save text file'

file='text.pkl'


res=model.save_obj(file, text)
print(res)