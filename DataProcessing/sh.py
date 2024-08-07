import os

# 计数器，用于文件重命名
counter = 1

# 获取当前目录下的所有文件和文件夹
entries = os.listdir('.')

# 遍历当前目录下的所有文件
for entry in entries:
    # 检查文件扩展名是否为.md
    if entry.endswith('.md'):
        # 获取不带扩展名的文件名
        file_name_without_extension = os.path.splitext(entry)[0]
        
        # 构造新的文件名，添加序号
        new_file_name = f"{counter}.md"
        new_file_path = os.path.join('.', new_file_name)
        
        # 构造文件的完整路径
        file_path = os.path.join('.', entry)
        
        # 打开文件，并读取内容
        with open(file_path, 'r+', encoding='utf-8') as file:
            content = file.read()
            pos = content.find('备案号')
            if pos != -1:
                content = content[:pos]
            pos = content.find('本文搬运来自')
            if pos != -1:
                content = content[:pos]
            # 构造要添加的标题行
            title_line = f'+++\ntitle="{file_name_without_extension}"\n+++\n'
            
            # 将文件指针移动到开头
            file.seek(0, 0)
            
            # 在文件开头添加标题行
            file.write(title_line + content)
            
            # 刷新文件缓冲区，确保内容被写入磁盘
            file.flush()
        
        # 重命名文件
        os.rename(file_path, new_file_path)
        
        # 更新计数器
        counter += 1