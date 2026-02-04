import os

def get_names(file_name):
    #使用names.txt的絕對路徑
    current_dir=os.path.dirname(os.path.abspath("_file_"))
    file_path=os.path.join(current_dir,'assets',file_name)

    with open(file_path,encoding='utf-8')as file:
        content=file.read()

    return content.split(',')
    
names=get_names("names.txt")
print(names)