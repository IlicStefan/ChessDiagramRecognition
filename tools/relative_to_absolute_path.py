from os.path import exists, abspath, dirname, join


def get_absolute_path(relative_path: str, file_path: str) -> str:
    absolute_path: str = join(abspath(dirname(file_path)), relative_path)
    # assert exists(absolute_path), "'%s' must be a valid directory path" % absolute_path
    return absolute_path
