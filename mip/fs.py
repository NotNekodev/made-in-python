################################################
# FS.PY                                        #
# Contains functions for example copying files #
################################################

from . import shell


def copy(src: str, dest: str) -> None:
    """
    Copies the object src to dest

    Args:
        src (str): The path to the input object
        dest (str): The path to the output object
    """
    tshell = shell.Shell(f"bash - copy {src}")
    tshell.execute(f"cp -r {src} {dest}")
    del tshell

def move(src: str, dest: str) -> None:
    """
    Moves the object src to dest

    Args:
        src (str): The path to the input object
        dest (str): The path to the output object
    """
    tshell = shell.Shell(f"bash - move {src}")
    tshell.execute(f"mv {src} {dest}")
    del tshell

def remove(obj: str) -> None:
    """
    Deltetes the object "obj"

    Args:
        obj (str): The object to delete
    """ 
    tshell = shell.Shell(f"bash - del {obj}")
    tshell.execute(f"rm -rf {obj}")
    del tshell
