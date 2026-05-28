# Importa funciones útiles de Django.
# render = muestra páginas HTML
# redirect = redirige a otra URL
# get_object_or_404 = busca un objeto o muestra error 404 si no existe
from django.shortcuts import render, redirect, get_object_or_404


# Importa el modelo Receta desde models.py
from .models import Receta


# =========================================================
# LISTAR RECETAS
# =========================================================

# Define la función lista_recetas.
# request contiene toda la información de la petición del usuario.
def lista_recetas(request):

    # Obtiene todas las recetas de la base de datos.
    recetas = Receta.objects.all()

    # Renderiza el template lista.html
    # y le envía las recetas en un diccionario.
    return render(request, 'lista.html', {'recetas': recetas})


# =========================================================
# CREAR RECETA
# =========================================================

# Define la función crear_receta.
def crear_receta(request):

    # Verifica si el formulario fue enviado usando POST.
    if request.method == 'POST':

        # Crea una nueva receta en la base de datos.
        Receta.objects.create(

            # Guarda el título enviado desde el formulario.
            titulo=request.POST['titulo'],

            # Guarda la categoría.
            categoria=request.POST['categoria'],

            # Guarda los ingredientes.
            ingredientes=request.POST['ingredientes'],

            # Guarda la preparación.
            preparacion=request.POST['preparacion'],

            # Guarda la imagen subida.
            # request.FILES contiene archivos.
            # .get('imagen') obtiene la imagen si existe.
            imagen=request.FILES.get('imagen')
        )

        # Redirige a la URL llamada 'lista'
        # después de guardar la receta.
        return redirect('lista')

    # Si la petición es GET,
    # muestra el formulario crear.html
    return render(request, 'crear.html')


# =========================================================
# EDITAR RECETA
# =========================================================

# Define la función editar_receta.
# id representa el ID de la receta a editar.
def editar_receta(request, id):

    # Busca la receta por ID.
    # Si no existe, muestra error 404.
    receta = get_object_or_404(Receta, id=id)

    # Verifica si el formulario fue enviado.
    if request.method == 'POST':

        # Actualiza el título.
        receta.titulo = request.POST['titulo']

        # Actualiza la categoría.
        receta.categoria = request.POST['categoria']

        # Actualiza los ingredientes.
        receta.ingredientes = request.POST['ingredientes']

        # Actualiza la preparación.
        receta.preparacion = request.POST['preparacion']

    # Verifica si el usuario subió una nueva imagen.
    if request.FILES.get('imagen'):
        
        # Reemplaza la imagen anterior.
        receta.imagen = request.FILES.get('imagen')

        # Guarda los cambios en la base de datos.
        receta.save()

        # Redirige a la lista de recetas.
        return redirect('lista')

    # Muestra el formulario editar.html
    # enviando la receta actual.
    return render(request, 'editar.html', {'receta': receta})


# =========================================================
# ELIMINAR RECETA
# =========================================================

# Define la función eliminar_receta.
def eliminar_receta(request, id):

    # Busca la receta por ID.
    # Si no existe, muestra error 404.
    receta = get_object_or_404(Receta, id=id)

    # Elimina la receta de la base de datos.
    receta.delete()

    # Redirige nuevamente a la lista.
    return redirect('lista')