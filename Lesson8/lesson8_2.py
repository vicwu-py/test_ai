with open ('assets/names.txt',encoding="utf-8") as file:
    content=file.read()
    
names = content.split(',')
names 