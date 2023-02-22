from random import choice
from string import ascii_lowercase
from os import (
    walk,
    remove,
    makedirs,
)
from os.path import (
    isfile,
    exists,
    basename,
)
from shutil import rmtree
import tarfile


def _temp_id(length):
    return "".join(choice(ascii_lowercase) for _ in range(length))


def _maybe_remove(name):
    try:
        if isfile(name):
            remove(name)
        else:
            rmtree(name, ignore_errors=True)
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
    temp_id = _temp_id(8)
    temporary_file_name = f"/tmp/{temp_id}.tar.gz"
    temporary_folder_name = f"/tmp/{temp_id}.d"
    raw_binary = None

    try:
        if not exists(temporary_folder_name):
            makedirs(temporary_folder_name)

        for fn, contents in files.items():
            with open(f"{temporary_folder_name}/{fn}", "wb") as fp:
                if type(contents) is str:
                    fp.write(bytes(contents, "utf-8"))
                else:
                    fp.write(contents)

        with tarfile.open(name=temporary_file_name, mode="w:gz") as tf:
            tf.add(temporary_folder_name, arcname="./")

        with open(temporary_file_name, "rb") as fp:
            raw_binary = fp.read()
    finally:
        _maybe_remove(temporary_file_name)
        _maybe_remove(temporary_folder_name)

    return raw_binary

