import os

def rename_images(folder_path, new_name_prefix):
    # Obtener la lista de archivos en el folder
    files = os.listdir(folder_path)

    # Filtrar solo los archivos con la extensión ".jpg"
    image_files = [file for file in files if file.lower().endswith('.jpg')]

    # Ordenar los archivos para asegurarnos de que se renombren en orden
    image_files.sort()

    # Iterar sobre cada archivo y renombrarlo
    for index, old_name in enumerate(image_files):
        # Construir el nuevo nombre
        new_name = f"{new_name_prefix}_{index:03}.jpg"
        # Obtener el path completo del archivo antiguo y nuevo
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        # Renombrar el archivo
        os.rename(old_path, new_path)
        print(f"Renombrado: {old_name} -> {new_name}")

if __name__ == "__main__":
    folder_path = "Project\Recolected_img\Images\Pilas"  # Cambia esto por la ruta a tu folder de imágenes
    new_name_prefix = "Pila"   # Cambia esto por el nuevo prefijo de nombre deseado
    rename_images(folder_path, new_name_prefix)
