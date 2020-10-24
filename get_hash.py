import hashlib
import os
import json

path = "F:\\Python\\System assistant\\dist\\toodoAssistant"  # os.path.dirname(os.path.realpath(__file__))
os.chdir(path)


def get_file_md5(file_path):
    """
    获取文件md5值
    :param file_path: 文件路径名
    :return: 文件md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).upper()


local_files = {}
for dirpath, dirnames, filenames in os.walk('./'):
    for filename in filenames:
        if ('.git' and 'dist' and '.idea') not in dirpath:
            file = os.path.join(dirpath.split('./')[1], filename)
            fhash = get_file_md5(file)
            local_files[file] = fhash
with open("update_info.txt", "w") as f:
    f.write(json.dumps(local_files))
