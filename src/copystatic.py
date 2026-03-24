import os
import shutil
import sys

def copy_files_recursive(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for filename in os.listdir(src_dir):
        from_path = os.path.join(src_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        print(f"* {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)

def copy_file(src_path, dest_path):
    """Copia um único arquivo"""
    try:
        with open(src_path, "rb") as source_file:
            content = source_file.read()
            with open(dest_path, "wb") as dest_file:
                dest_file.write(content)
        print(f"Copiado: {src_path} -> {dest_path}")
    except Exception as e:
        print(f"Erro ao copiar {src_path}: {e}")
        raise

def copy_static(src_dir, dest_dir):
    """Copia recursivamente todo o conteúdo de src_dir para dest_dir"""
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    
    try:
        items = os.listdir(src_dir)
    except PermissionError:
        print(f"Erro: Sem permissão para ler {src_dir}")
        return
    
    for item in items:
        source_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        if os.path.isfile(source_path):
            copy_file(source_path, dest_path)
        elif os.path.isdir(source_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_static(source_path, dest_path)

def delete_directory_contents(dir_path):
    """Remove recursivamente todo o conteúdo de um diretório"""
    if not os.path.exists(dir_path):
        return
    
    try:
        items = os.listdir(dir_path)
    except PermissionError:
        print(f"Erro: Sem permissão para ler {dir_path}")
        return
    
    for item in items:
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            try:
                os.remove(item_path)
            except Exception as e:
                print(f"Erro ao remover {item_path}: {e}")
        elif os.path.isdir(item_path):
            try:
                delete_directory_contents(item_path)
                os.rmdir(item_path)
            except Exception as e:
                print(f"Erro ao remover {item_path}: {e}")

def clear_public_directory(public_dir):
    """Limpa e recria o diretório public"""
    if os.path.exists(public_dir):
        delete_directory_contents(public_dir)
        try:
            os.rmdir(public_dir)
        except Exception as e:
            print(f"Erro ao remover {public_dir}: {e}")
            sys.exit(1)
    
    try:
        os.mkdir(public_dir)
    except Exception as e:
        print(f"Erro ao criar {public_dir}: {e}")
        sys.exit(1)
