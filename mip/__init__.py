from . import project

def build_proj(proj: project.Project):
    proj.info()
    print(proj.get_src_files())