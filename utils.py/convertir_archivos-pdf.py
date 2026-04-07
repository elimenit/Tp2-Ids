from PIL import Image
import os

def convertir_a_pdf(ruta_entrada, nombre_salida):
    """Convierte un archivo a pdf

    Args:
        ruta_entrada: ruta del archivo fuente
        nombre_salida (_type_): ruta del archivo de salida
    Example:
    convertir_a_pdf("mi_imagen.png", "resultado.pdf")
    """
    # Abrir la imagen y convertirla a modo RGB 
    # (importante porque PNG puede estar en RGBA y PDF no siempre lo maneja bien)
    imagen = Image.open(ruta_entrada)
    rgb_imagen = imagen.convert('RGB')
    
    rgb_imagen.save(nombre_salida)
    print(f"¡Éxito! Archivo guardado como: {nombre_salida}")

def imagenes_a_un_solo_pdf(lista_imagenes, nombre_final):
    """Convierte una lista de imagenes a archivos pdf

    Args:
        lista_imagenes (_type_): Una lista de todos los archivos pdf
        nombre_final (_type_): nombre final que se les dara al conjunto de archivos pdf
    Example:
        fotos = ["foto1.png", "foto2.jpg", "foto3.png"]
        imagenes_a_un_solo_pdf(fotos, "album_completo.pdf")
    """
    imagenes_listas = []
    
    for ruta in lista_imagenes:
        img = Image.open(ruta).convert('RGB')
        imagenes_listas.append(img)
    
    # Tomamos la primera y le pasamos el resto en el parámetro 'append_images'
    if imagenes_listas:
        imagenes_listas[0].save(
            nombre_final, 
            save_all=True, 
            append_images=imagenes_listas[1:]
        )
        print(f"PDF multipágina creado: {nombre_final}")
    
convertir_a_pdf("/home/elimenit/Desktop/java_basico/comprobante.png", "/home/elimenit/Desktop/conprobante.pdf")