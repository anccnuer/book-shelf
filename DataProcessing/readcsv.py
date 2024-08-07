import csv
with open('output.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    my_dict = {rows[0]: rows[1] for rows in reader}
key_to_find = "本宫偏不"
if key_to_find in my_dict:
    value = my_dict[key_to_find]
    print(f"The value for key '{key_to_find}' is: {value}")
else:
    print(f"Key '{key_to_find}' not found in the dictionary.")
    # i = 0
    # for row in reader:
    #     print(row[0])
    #     i= i+1
    #     if i ==5: break  # 只打印第一行，然后退出循环
