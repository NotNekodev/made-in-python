##########################
# __INIT__.PY            #
# The librarys main file #
##########################

# Codes
MIP_SUCCESS = 0x0
MIP_FAILURE = 0x1

from . import project


def build_proj(proj: project.Project) -> int:
    """
    Buils the project specified in proj

    Args:
        proj (project.Project): The project that 
    """
    return MIP_SUCCESS