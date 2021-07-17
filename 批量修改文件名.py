# 批量修改文件名

import os

path = '\home\desktop' # filepath

# # name_list = []
# # player_list = []
# rename_list = []
# k = []
# for i, j, k in os.walk(filePath):
#     print(k)
#
#     for item in k:
#         if item!='rename.bat':
#             print(item)
#             k_list = item.split('-')
#             print(k_list)
#             # name_list.append(k_list[0])
#             k1_list = k_list[1].split('.')
#             # player_list.append(k1_list[0])
#             rename_list.append("ren " + item + ' ' + k1_list[0] + '-' +k_list[0] + '.' + k1_list[1])
#
# print(rename_list)
# f = open('C:/Users/18471/Desktop/test/files/rename.bat','w',encoding= 'utf-8')
# f.write('@echo off\n')
# for item in rename_list:
#     f.write(item)
#     f.write('\n')
# f.close()


fileList = os.listdir(path)
print(fileList)

for item in fileList:
    print(item)
    oldname = path + os.sep + item  # os.sep添加系统分隔符
    oldname_list = item.split(' - ')
    oldname_list1 = oldname_list[1].split('.')


    # 设置新文件名
    newname = path + os.sep + oldname_list1[0] + ' - ' + oldname_list[0] + '.' + oldname_list1[1]
    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

