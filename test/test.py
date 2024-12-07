import mip
from mip import project

proj = project.Project(name="Test", language=project.Languages.C)

#proj.info()
proj.add_src_file("src/main.c")

mip.build_proj(proj=proj)