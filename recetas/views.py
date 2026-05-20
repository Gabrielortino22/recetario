from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta

# LISTAR
def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista.html', {'recetas': recetas})

# CREAR
def crear_receta(request):
    if request.method == 'POST':
        Receta.objects.create(
            titulo=request.POST['titulo'],
            ingredientes=request.POST['ingredientes'],
            preparacion=request.POST['preparacion']
        )
        return redirect('lista')

    return render(request, 'crear.html')

# EDITAR
def editar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)

    if request.method == 'POST':
        receta.titulo = request.POST['titulo']
        receta.ingredientes = request.POST['ingredientes']
        receta.preparacion = request.POST['preparacion']
        receta.save()

        return redirect('lista')

    return render(request, 'editar.html', {'receta': receta})

# ELIMINAR
def eliminar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    receta.delete()
    return redirect('lista')