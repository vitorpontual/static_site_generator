import os 

from copystatic import clear_public_directory, copy_static
from generatepage import generate_page
dir_path_static = "./static"
dir_path_public = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        clear_public_directory(dir_path_public)

    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)

    generate_page(
        "./content/index.md",
        "public/index.html",
        "template.html"
    )



if __name__ == "__main__":
    main()
