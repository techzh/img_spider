import difflib
import os
import shutil


def getFileList(path):
    list_dir = os.listdir(path)
    list_dir.sort()
    print(list_dir)
    return list_dir


def check(base_path, dst_path, list_dir):
    curr_list = []
    last_name = ''
    for name in list_dir:
        ratio = difflib.SequenceMatcher(None, last_name, name).quick_ratio()
        if ratio > 0.7:
            curr_list.append(name)
        else:
            if len(curr_list) > 1:
                move(base_path, dst_path, curr_list)
            curr_list.clear()
            curr_list.append(name)
        last_name = name
    if len(curr_list) > 1:
        move(base_path, dst_path, curr_list)

def move(srcBasePath, dstBasePath, list_name):
    path = dstBasePath+"/"+list_name[0]
    if not os.path.exists(path):
        os.makedirs(path)
    for name in list_name:
        shutil.copyfile(srcBasePath+"/"+name, path+"/"+name)
        os.remove(srcBasePath+"/"+name)


def merge(base_path):
    list_dir = os.listdir(path)
    list_dir.sort()
    k = open(path + "/result.txt", 'a+')
    # list_dir.reverse()
    for name in list_dir:
        pathh = path + "/" + name
        f = open(pathh)
        k.write(f.read() + "\n")
    k.close()



if __name__ == "__main__":
    path = "/Users/zhangyafeng1/Desktop/testfile/txt"
    file_list = getFileList(path)
    check("/Users/zhangyafeng1/Desktop/testfile/txt","/Users/zhangyafeng1/Desktop/testfile/合并", file_list)
