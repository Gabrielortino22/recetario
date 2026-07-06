from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Receta, Perfil

from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import RegistroForm

def prueba_receta(request):
    return render(request, 'prueba.html')


def prueba_2_receta(request):
    return render(request, 'prueba_2.html')


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

    # SOLO LOS EDITORES PUEDEN CREAR
    if request.user.perfil.rol != "editor":
        return redirect("lista")

    if request.method == 'POST':

        Receta.objects.create(

            titulo=request.POST['titulo'],

            categoria=request.POST['categoria'],

            ingredientes=request.POST['ingredientes'],

            preparacion=request.POST['preparacion'],

            imagen=request.FILES.get('imagen'),

            video=request.FILES.get('video')

        )

        return redirect('lista')

    return render(request, 'crear.html')


# =========================================================
# EDITAR RECETA
# =========================================================

@login_required
def editar_receta(request, id):

    # SOLO LOS EDITORES PUEDEN EDITAR
    if request.user.perfil.rol != "editor":
        return redirect("lista")

    receta = get_object_or_404(Receta, id=id)

    if request.method == 'POST':

        receta.titulo = request.POST['titulo']

        receta.categoria = request.POST['categoria']

        receta.ingredientes = request.POST['ingredientes']

        receta.preparacion = request.POST['preparacion']

        if request.FILES.get('imagen'):

            receta.imagen = request.FILES.get('imagen')

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

    # SOLO LOS EDITORES PUEDEN ELIMINAR
    if request.user.perfil.rol != "editor":
        return redirect("lista")

    receta = get_object_or_404(Receta, id=id)

    receta.delete()

    return redirect('lista')

# =========================================================
# LOGIN PERSONALIZADO
# =========================================================

def login_usuario(request):

    if request.user.is_authenticated:
        return redirect("lista")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("lista")

        else:

            messages.error(
                request,
                "Usuario o contraseña incorrectos."
            )

    return render(
        request,
        "registration/login.html"
    )

# =========================================================
# REGISTRO DE USUARIOS
# =========================================================

def registro_usuario(request):

    if request.user.is_authenticated:

        return redirect('lista')

    if request.method == 'POST':

        form = RegistroForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Usuario creado correctamente. Ya podés iniciar sesión."

            )

            return redirect('login')

    else:

        form = RegistroForm()

    return render(

        request,

        'registration/registro.html',

        {

            'form': form

        }

    )