from django.contrib.auth.models import User          # Importa el modelo User de Django para trabajar con los usuarios.

from django.http import HttpResponseForbidden        # Permite devolver un error 403 cuando un usuario no tiene permisos.

from django.shortcuts import render, redirect, get_object_or_404
# render: muestra una plantilla HTML.
# redirect: redirige al usuario a otra página.
# get_object_or_404: busca un objeto y devuelve un error 404 si no existe.

from django.contrib.auth.decorators import login_required
# Decorador que obliga a que el usuario haya iniciado sesión.

from .models import Receta, Perfil                  # Importa los modelos Receta y Perfil.

from django.contrib.auth import authenticate, login
# authenticate: verifica si el usuario y contraseña son correctos.
# login: inicia la sesión del usuario.

from django.contrib import messages                 # Permite mostrar mensajes en la aplicación (éxito, error, aviso, etc.).

from .forms import RegistroForm                     # Importa el formulario de registro de usuarios.



# =========================================================
# LISTAR RECETAS
# =========================================================

def lista_recetas(request):                         # Vista que muestra todas las recetas.

    categoria = request.GET.get('categoria')        # Obtiene el valor del parámetro "categoria" enviado por la URL.

    if categoria:                                   # Si el usuario seleccionó una categoría...

        recetas = Receta.objects.filter(categoria=categoria)
        # Busca únicamente las recetas que pertenecen a esa categoría.

    else:                                           # Si no seleccionó ninguna categoría...

        recetas = Receta.objects.all()              # Obtiene todas las recetas de la base de datos.

    return render(
        request,                                    # Envía la petición actual.
        'lista.html',                               # Plantilla HTML que se mostrará.
        {'recetas': recetas}                        # Envía la lista de recetas a la plantilla.
    )
# =========================================================
# CREAR RECETA
# =========================================================

@login_required                              # Obliga a que el usuario haya iniciado sesión.
def crear_receta(request):                   # Vista encargada de crear una nueva receta.

    # SOLO LOS EDITORES PUEDEN CREAR
    if request.user.perfil.rol != "editor":  # Verifica si el usuario NO es editor.

        return redirect("lista")             # Si no es editor, lo envía nuevamente a la lista de recetas.

    if request.method == 'POST':             # Comprueba si el formulario fue enviado.

        Receta.objects.create(               # Crea un nuevo registro en la tabla Receta.

            titulo=request.POST['titulo'],           # Guarda el título ingresado.

            categoria=request.POST['categoria'],     # Guarda la categoría seleccionada.

            ingredientes=request.POST['ingredientes'], # Guarda los ingredientes.

            preparacion=request.POST['preparacion'],   # Guarda la preparación.

            imagen=request.FILES.get('imagen'),      # Guarda la imagen subida (si existe).

            video=request.FILES.get('video')         # Guarda el video subido (si existe).

        )

        return redirect('lista')            # Una vez creada la receta vuelve a la lista.

    return render(                          # Si el usuario aún no envió el formulario...
        request,                            # Envía la petición.
        'crear.html'                        # Muestra la plantilla crear.html.
    )
# =========================================================
# EDITAR RECETA
# =========================================================

@login_required                              # Solo usuarios autenticados pueden editar.
def editar_receta(request, id):              # Vista que edita una receta.

    # SOLO LOS EDITORES PUEDEN EDITAR
    if request.user.perfil.rol != "editor":  # Comprueba que el usuario sea editor.

        return redirect("lista")             # Si no lo es, vuelve a la lista.

    receta = get_object_or_404(              # Busca la receta...
        Receta,
        id=id                                # ...por su ID.
    )

    if request.method == 'POST':             # Si el formulario fue enviado...

        receta.titulo = request.POST['titulo']               # Actualiza el título.

        receta.categoria = request.POST['categoria']         # Actualiza la categoría.

        receta.ingredientes = request.POST['ingredientes']   # Actualiza los ingredientes.

        receta.preparacion = request.POST['preparacion']     # Actualiza la preparación.

        if request.FILES.get('imagen'):      # Si el usuario subió una nueva imagen...

            receta.imagen = request.FILES.get('imagen')  # Reemplaza la imagen anterior.

        if request.FILES.get('video'):       # Si subió un nuevo video...

            receta.video = request.FILES.get('video')    # Reemplaza el video anterior.

        receta.save()                        # Guarda todos los cambios en la base de datos.

        return redirect('lista')             # Regresa a la lista de recetas.

    return render(                           # Si todavía no envió el formulario...
        request,
        'editar.html',                       # Muestra la plantilla editar.html.
        {'receta': receta}                   # Envía la receta para completar el formulario.
    )
# =========================================================
# ELIMINAR RECETA
# =========================================================

@login_required                              # Solo los usuarios que iniciaron sesión pueden acceder.
def eliminar_receta(request, id):            # Vista que elimina una receta.

    # SOLO LOS EDITORES PUEDEN ELIMINAR
    if request.user.perfil.rol != "editor":  # Verifica si el usuario NO es editor.

        return redirect("lista")             # Si no es editor, vuelve a la lista.

    receta = get_object_or_404(              # Busca la receta por su ID.
        Receta,
        id=id
    )

    receta.delete()                          # Elimina la receta de la base de datos.

    return redirect('lista')                 # Regresa a la lista de recetas.
# =========================================================
# LOGIN PERSONALIZADO
# =========================================================

def login_usuario(request):                  # Vista que permite iniciar sesión.

    if request.user.is_authenticated:        # Comprueba si el usuario ya inició sesión.

        return redirect("lista")             # Si ya inició sesión, lo envía a la página principal.

    if request.method == "POST":             # Si el formulario fue enviado...

        username = request.POST.get("username")   # Obtiene el nombre de usuario.

        password = request.POST.get("password")   # Obtiene la contraseña.

        user = authenticate(                 # Verifica si los datos son correctos.
            request,
            username=username,
            password=password
        )

        if user is not None:                 # Si el usuario existe...

            login(request, user)             # Inicia la sesión.

            return redirect("lista")         # Lo redirige a la lista de recetas.

        else:                                # Si el usuario o contraseña son incorrectos...

            messages.error(                  # Muestra un mensaje de error.

                request,

                "Usuario o contraseña incorrectos."

            )

    return render(                           # Muestra la plantilla de login.
        request,

        "registration/login.html"

    )
# =========================================================
# REGISTRO DE USUARIOS
# =========================================================

def registro_usuario(request):               # Vista que registra nuevos usuarios.

    if request.user.is_authenticated:        # Comprueba si el usuario ya inició sesión.

        return redirect('lista')             # Si ya inició sesión, vuelve a la lista.

    if request.method == 'POST':             # Si el formulario fue enviado...

        form = RegistroForm(request.POST)    # Crea el formulario con los datos recibidos.

        if form.is_valid():                  # Verifica que los datos sean válidos.

            form.save()                      # Guarda el nuevo usuario en la base de datos.

            messages.success(                # Muestra un mensaje de éxito.

                request,

                "Usuario creado correctamente. Ya podés iniciar sesión."

            )

            return redirect('login')         # Redirige al login.

    else:                                    # Si todavía no envió el formulario...

        form = RegistroForm()                # Crea un formulario vacío.

    return render(                           # Muestra la plantilla de registro.

        request,

        'registration/registro.html',

        {

            'form': form                     # Envía el formulario a la plantilla.

        }

    )
# =========================================================
# LISTA DE USUARIOS
# =========================================================

@login_required                                  # Solo los usuarios que iniciaron sesión pueden acceder.
def lista_usuarios(request):                     # Vista que muestra todos los usuarios registrados.

    if request.user.perfil.rol != "editor":      # Comprueba si el usuario NO tiene el rol Editor.

        return HttpResponseForbidden(            # Devuelve un error 403 (Acceso prohibido).
            "No tenés permiso para acceder."
        )

    usuarios = User.objects.all()                # Obtiene todos los usuarios de la base de datos.

    return render(                               # Muestra la plantilla HTML.
        request,

        "usuarios.html",                         # Plantilla que muestra la lista de usuarios.

        {

            "usuarios": usuarios                 # Envía la lista de usuarios a la plantilla.

        }

    )
# =========================================================
# CAMBIAR ROL
# =========================================================

@login_required                                  # Solo usuarios autenticados pueden acceder.
def cambiar_rol(request, id):                    # Vista que cambia el rol de un usuario.

    if request.user.perfil.rol != "editor":      # Verifica que quien realiza la acción sea Editor.

        return HttpResponseForbidden(            # Si no tiene permisos devuelve un error 403.

            "No tenés permiso."

        )

    usuario = get_object_or_404(                 # Busca el usuario por su ID.
        User,
        id=id
    )

    # Evita que el editor cambie su propio rol
    if usuario == request.user:                  # Comprueba si intenta modificar su propio usuario.

        return redirect("usuarios")              # Si es así, vuelve a la lista de usuarios.

    if usuario.perfil.rol == "lector":           # Si el usuario es Lector...

        usuario.perfil.rol = "editor"            # Lo convierte en Editor.

    else:                                        # Si ya era Editor...

        usuario.perfil.rol = "lector"            # Lo convierte en Lector.

    usuario.perfil.save()                        # Guarda el nuevo rol en la base de datos.

    return redirect("usuarios")                  # Regresa a la lista de usuarios.
