from random import choice
from string import ascii_lowercase
from os import walk, remove
import tarfile


def _temp_id(length):
    return "".join(choice(ascii_lowercase) for _ in range(length))


def _maybe_remove(name):
    try:
        remove(name)
    except:
        pass


def list_directory(name):
    files = []

    for _, _, filenames in walk(name):
        files.extend(filenames)

    return files


def extract(raw_binary):
    temp_id = _temp_id(7)
    temporary_file_name = f"/tmp/{temp_id}.tar.gz"
    temporary_folder_name = f"/tmp/{temp_id}.d"
    result = {}

    try:
        with open(temporary_file_name, "wb") as fp:
            fp.write(raw_binary)
    
        with tarfile.open(name=temporary_file_name, mode="r:gz") as tf:
            tf.extractall(path=temporary_folder_name)
            files = list_directory(temporary_folder_name)
            result = {}

            for fn in files:
                with open(f"{temporary_folder_name}/{fn}", "r") as fp:
                    result[fn] = fp.read()
    except:
        result = None
    finally:
        _maybe_remove(temporary_file_name)
        _maybe_remove(temporary_folder_name)

    return result


def compress(files):
    pass

