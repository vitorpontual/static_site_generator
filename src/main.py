import os 
import sys

from copystatic import clear_public_directory, copy_static
from gencontent import  generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():

    basepath = '/'
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        if not basepath.startswith("/"):
            basepath = "/" + basepath
        if not basepath.endswith("/"):
            basepath = basepath + "/"

    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        clear_public_directory(dir_path_public)

    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)

    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        basepath
    )


if __name__ == "__main__":
    main()
