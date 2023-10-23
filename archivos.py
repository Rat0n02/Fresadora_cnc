from gerber import load

# Ruta al archivo Gerber que deseas cargar
gerber_file_path = 'ruta/al/archivo.gbr'

# Cargar el archivo Gerber
gerber = load(gerber_file_path)

# Ahora puedes trabajar con el objeto Gerber
# Por ejemplo, puedes imprimir información sobre la capa:
print("Nombre de la capa:", gerber.name)
print("Unidades:", gerber.units)
print("Formato:", gerber.format)
print("Número de aperturas:", len(gerber.apertures))
print("Número de comandos:", len(gerber.commands))

# Puedes recorrer los comandos del archivo Gerber
for command in gerber:
    print(command)

# A continuación, puedes realizar las operaciones necesarias en el archivo Gerber.
# Por ejemplo, puedes generar una imagen de la capa:
if gerber.name.endswith(".gto"):
    from gerber.render import GerberCairoContext
    from gerber.render import render

    # Crear un contexto de renderizado
    ctx = GerberCairoContext()

    # Renderizar la capa en una imagen
    render(gerber, ctx)

    # Guardar la imagen en un archivo
    ctx.dump('nombre_de_la_imagen.png')

# Recuerda importar las bibliotecas necesarias según tus necesidades.
