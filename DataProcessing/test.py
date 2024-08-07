import re
import os
def a(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
            content = file.read()
    start = "&emsp;&emsp;" 
    end = "\n"   
    pattern = re.escape(start) + r'(.*?)' + re.escape(end) #re.escape()函数用于转义start和end字符串中的特殊字符
    des = re.findall(pattern, content, re.DOTALL) #re.DOTALL标志来让.匹配包括换行符在内的任意字符
    return "".join(des[0:2])
print(a("1.md"))