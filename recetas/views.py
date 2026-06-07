from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Receta


# =========================================================
# LISTAR RECETAS
# =========================================================
def lista_recetas(request):

    categoria = request.GET.get('categoria')

    if categoria:
        recetas = Receta.objects.filter(categoria=categoria)
    else:
        recetas = Receta.objects.all()

    return render(request, 'lista.html', {'recetas': recetas})


# =========================================================
# CREAR RECETA
# =========================================================
@login_required
def crear_receta(request):

    if request.method == 'POST':

        Receta.objects.create(
            titulo=request.POST['titulo'],
            categoria=request.POST['categoria'],
            ingredientes=request.POST['ingredientes'],
            preparacion=request.POST['preparacion'],

            imagen=request.FILES.get('imagen'),
            video=request.FILES.get('video')  # ✔ video agregado
        )

        return redirect('lista')

    return render(request, 'crear.html')


# =========================================================
# EDITAR RECETA
# =========================================================
@login_required
def editar_receta(request, id):

    receta = get_object_or_404(Receta, id=id)

    if request.method == 'POST':

        receta.titulo = request.POST['titulo']
        receta.categoria = request.POST['categoria']
        receta.ingredientes = request.POST['ingredientes']
        receta.preparacion = request.POST['preparacion']

        # ✔ imagen opcional
        if request.FILES.get('imagen'):
            receta.imagen = request.FILES.get('imagen')

        # ✔ video opcional (ESTO ES LO QUE TE FALTABA)
        if request.FILES.get('video'):
            receta.video = request.FILES.get('video')

        receta.save()

        return redirect('lista')

    return render(request, 'editar.html', {'receta': receta})


# =========================================================
# ELIMINAR RECETA
# =========================================================
@login_required
def eliminar_receta(request, id):

    receta = get_object_or_404(Receta, id=id)
    receta.delete()

    return redirect('lista')