import re
import csv

txt_url = "input.md"

with open(txt_url, 'r', encoding='utf-8') as f:
    content = f.read()  # 读取txt文件内容 保存到content中
start = "## [" 
end = "]"   
pattern = re.escape(start) + r'(.*?)' + re.escape(end) #re.escape()函数用于转义start和end字符串中的特殊字符
title = re.findall(pattern, content, re.DOTALL) #re.DOTALL标志来让.匹配包括换行符在内的任意字符
    
start = "&emsp;&emsp;" 
end = "\n" 
pattern = re.escape(start) + r'(.*?)' + re.escape(end) #re.escape()函数用于转义start和end字符串中的特殊字符
discription = re.findall(pattern, content, re.DOTALL) #re.DOTALL标志来让.匹配包括换行符在内的任意字符

headers = ['title', 'discription']

# 打开一个新的CSV文件用于写入
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    # 写入每一行数据
    for title, discription in zip(title, discription):
        writer.writerow([title, discription])