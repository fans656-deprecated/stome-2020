"""
Stome use directories and files to store its data, the directory structure looks like:
    /data/stome-root/                               The root directory.
        meta/                                       Meta directory, utilized the filesystem to store structure info.
            img/                                    Example directory "/img".
                girl.jpg                            Example file "/img/girl.jpg", this only store meta info (has a pointer to the actual content file).
        inode-data/                                 Inode data directory, used to store the actual file content, the file name is MD5 hash of the content.
            bda80cf1c0192a9091de592c5cc04b8f        Example content file for "girl.jpg".
        inode-meta/                                 Inode meta directory, used to store inode meta.
            bda80cf1c0192a9091de592c5cc04b8f        Example inode meta file for "girl.jpg", store MIME type of the content and other info.
        temp/                                       Temporary directory, used to store file content during uploading.
            9f7c0089-718d-4f44-9e56-c5ae69df4127    Example temporary file to store file content during uploading.
"""
import os


CHUNK_SIZE = 4096


ROOT_DIR = '/data/stome-root'
META_DIR = os.path.join(ROOT_DIR, 'meta')
INODE_DATA_DIR = os.path.join(ROOT_DIR, 'inode-data')
INODE_META_DIR = os.path.join(ROOT_DIR, 'inode-meta')
TEMP_DIR = os.path.join(ROOT_DIR, 'temp')

META_DIR_PREFIX_LENGTH = len(META_DIR)

for path in (META_DIR, INODE_DATA_DIR, INODE_META_DIR, TEMP_DIR):
    if not os.path.exists(path):
        os.makedirs(path)


PUBKEY = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDP6Sm7IYP9/1SwvgAnIK8+omG5WeK4ZmEeSrAbjtPsqw8JtfbXAI8/IlaOv9EK+jjZ6A0KOH3LvnmpbAZVgK0PaDbNXiNE6ZXs5Z26Yt9peTWD4tKEZoBNc0M0TvLv5RK2MQCYOEHrdJODGh4MLqhC58QT3SbL3TE0jCgo7rqf2aQkrX+gwDynnjBkzh8/GUmWT6XK2SYn/d4bWJ7Xrf37Rj+hIEvnO1NEETlrIljGg0XuFjLXLxdXoKv69XZ0G0avypcq+6BYzgy9bghySviwwGCA2k9eaOSt2iKf6J8H4laSyR2SC7AJMfe3zNeNTlwTrp4frkRr6Mzc2+zI0erP'
