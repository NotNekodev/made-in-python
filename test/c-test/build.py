import mip
from mip import project

proj = project.Project(name="C Test", language=project.Languages.C)

# proj.add_src_file("src/main.c")

proj.add_src_dir("src/", ".c") # first is the path to the folder, the second one is the extension to scan with

proj.set_compiler("/usr/bin/clang")
proj.set_assember("/usr/bin/nasm")
proj.set_linker("/usr/bin/ld")

proj.info()

proj.set_executable_name("test-c")

mip.build_proj(proj=proj)