import os 
import sys 

def copy_files(src_dir, dest_dir):
    try:
        with open(src_dir, "rb") as source_file:
            content = sorce_file.read()

            with open(dest_dir, "wb") as dest_file:
                dest_file.write(content)

        print(f"Copy file: {src_dir} -> {dest_dir}")
    except Exception as e:
        print(f"Error Copy file {src_dir}: {e}")
        raise



def copy_static(src_dir, dest_dir):

    if not os.path.exists(dest_dir):
        print(f"Create directory: {dest_dir}")
        os.mkdir(dest_dir)


    try:
        items = os.listdir(src_dir)
    except PermissionError:
        print(f"Error: Not Permission to read {src_dir}")
        return


    for item in items:
        source_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isfile(source_path):
            copy_file(source_path, dest_path)
        elif os.path.isdir(source_path):
            os.mkdir(dest_path)
            copy_static(source_path, dest_path)
        else:
            print(f"WARNING: Ignore item especial: {source_path}")


def delete_directory_contents(dir_path):
    if not os.path.exits(dir_path):
        return

    try:
        items = os.listdir(dest_dir)
    except PermissionError:
        print(f"ERROR: Permssion not read {dest_dir}")
        return

    for item in items:
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            try:
                os.remove(item_path)
            except Exception as e:
                print(e)

        elif os.path.isdir(item_path):
            try:
                delete_directory_contents(item_path)
                os.rmdir(item_path)
            except Exception as e:
                print(e)


        else:
            try:
                os.remove(item_path)
            except:
                print(f" WARNING: It was not possible to remove")



def clear_public_directory(public_dir):
    if os.path.exists(public_dir):
        delete_directory_contents(public_dir)
        try:
            os.rmdir(public_dir)
        except Exception as e:
            print(e)
        try:
            os.mkdir(public_dir)
            
        except Exception as e:
            print(e)
            sys.exit(1)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(base_dir, "static")
    public_dir = os.path.join(base_dir, "public")

    if not os.path.exists(static_dir):
        sys.exit(1)

    print("\n[1/2] Limpando diretório public...")
    clear_public_directory(public_dir)

    print("\n[2/2] Copiando arquivos statics...")
    copy_static(static_dir, public_dir)

    show_directory_structure(public_dir, 0)

def show_directory_structure(dir, ind_level):
    try:
        items = sorted(os.listdir(dir))
        indent = " " * ind_level

        for item in items:
            item_path = os.path.join(dir, item)
            if os.path.isdir(item_path):
                show_directory_structure(item_path, ind_level + 1)
            else:
                size = os.path.getsize(item_path)
                if size < 1024:
                    size_str = f"{size} bytes"
                elif size < 1024*1024:
                    size_str = f"{size/1024:.1f} KB"
                else:
                    size_str = f"{size/(1024*1024):.1f} MB"
                print(f"{indent} {item} ({size_str})")
    except PermissionError:
        print(f"[Sem permissão para ler {dir}]")

if  __name__ == "__main__":
    main()
