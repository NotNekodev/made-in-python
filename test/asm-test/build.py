import mip
from mip import project

proj = project.Project(name="ASM Test", language=project.Languages.ASM)

proj.add_src_file("src/main.asm")

proj.set_compiler("/usr/bin/clang")
proj.set_assember("/usr/bin/nasm")
proj.set_linker("/usr/bin/ld")

proj.info()

proj.set_executable_name("test-asm")

mip.build_proj(proj=proj)
# Very cool syntax imo