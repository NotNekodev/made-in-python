import mip
from mip import project

proj = project.Project(name="Test", language=project.Languages.C)

proj.add_src_file("src/main.c")

proj.set_compiler("/usr/bin/clang")
proj.set_assember("/usr/bin/nasm")

mip.build_proj(proj=proj)