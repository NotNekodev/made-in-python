##########################
# __INIT__.PY            #
# The librarys main file #
##########################



from . import project
from . import shell
import os
import re

# Codes
MIP_SUCCESS = 0x0
MIP_FAILURE = 0x1

def build_proj(proj: project.Project, link: bool = True) -> int:
    """
    Buils the project specified in proj, including all subprojects.

    Args:
        proj (project.Project): The project that you want to build
        link (opt, bool): If you would like to link the project
    Returns:
        result: MIP_SUCCESS (0) on success and MIP_FAILURE (1) on error
    """


    obj_files = []

    if proj.subprojects.count is 0:
        print("No subprojects found, skipping to main project")
    elif proj.subprojects >= 1:
        print(f"Found {proj.subprojects.count}! Building them.")
        while proj.subprojects:
            sproj = proj.subprojects.pop()
            if sproj.name == proj.name:
                print(f"Recursion found in subproject {sproj.name}! Not buidling that one!")
                break
            build_proj(sproj)
            print(f"Built subproject {sproj.name}!")

    

    # Create a new shell
    bs = shell.Shell(name="build shell", shell="/bin/bash")

    if os.path.exists(proj.get_build_dir()) == True:
        bs.execute(f"rm -rf {proj.get_build_dir()}")

    # create the build dir
    bs.execute(f"mkdir -p {proj.get_build_dir()}")
    print("Successfully created the build directory")

    if proj.language is project.Languages.C or proj.language is project.Languages.CXX:
        for file in proj.get_src_files():
            bs.execute(f"{proj.get_compiler()} {' '.join(proj.compile_args)} -c {file} -o {proj.get_build_dir()}/{re.sub(r'^.*/', '', file)}.o")

            obj_files.append(f"{proj.get_build_dir()}/{re.sub(r'^.*/', '', file)}.o")
     
        if link is True:
            bs.execute(f"{proj.get_compiler()} {' '.join(obj_files)} -o {proj.get_build_dir()}/{proj.get_executable_name()}")

            if os.path.exists(f"{proj.get_build_dir()}/{proj.get_executable_name()}") == False:
                raise FileNotFoundError(f"The executable {proj.get_build_dir()}/{proj.get_executable_name()} wasnt found!")
    
            print(f"Linked final executable {proj.get_build_dir()}/{proj.get_executable_name()}!")
        else:
            print("Not linking. Link is false!")

    elif proj.language is project.Languages.ASM:
        for file in proj.get_src_files():
            bs.execute(f"{proj.get_assembler()} {' '.join(proj.compile_args)}  -felf64 {file} -o {proj.get_build_dir()}/{re.sub(r'^.*/', '', file)}.o")

            obj_files.append(f"{proj.get_build_dir()}/{re.sub(r'^.*/', '', file)}.o")

        if link is True:
            bs.execute(f"{proj.get_linker()} {' '.join(obj_files)} -o {proj.get_build_dir()}/{proj.get_executable_name()}")

            if os.path.exists(f"{proj.get_build_dir()}/{proj.get_executable_name()}") == False:
                raise FileNotFoundError(f"The executable {proj.get_build_dir()}/{proj.get_executable_name()} wasnt found!")
    
            print(f"Linked final executable {proj.get_build_dir()}/{proj.get_executable_name()}!")
        else:
            print("Not linking. Link is false!")


    return MIP_SUCCESS