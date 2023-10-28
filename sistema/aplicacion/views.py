from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from api.models import Usuario
from api.models import CategoriaCurso
from api.models import Curso
from api.models import Estudiante
from api.models import Inscripcion
from api.models import Notificacion
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('task:inicio')  # Redirige al index.html después de la autenticación exitosa
    return render(request, 'login.html')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def inicio(request):
    cursos = Curso.objects.all()
    notificaciones=Notificacion.objects.all()
    return render(request, 'index.html', {'cursos': cursos},{'notificaciones':notificaciones}    )

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def inicio(request):
    notificaciones = Notificacion.objects.all()
    return render(request, 'index.html',{'notificaciones':notificaciones})

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def curso_view(request):
    cursos = Curso.objects.all()
    notificaciones=Notificacion.objects.all()
    datos={
        'cursos':cursos,
        'notificaciones':notificaciones,
    }
    return render(request, 'Cursos/cursos.html', datos)

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def create_curso_view(request):
    notificaciones = Notificacion.objects.all()    
    return render(request, 'Cursos/create_curso.html',{'notificaciones':notificaciones})

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def create_curso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre_curso']
        descripcion = request.POST['descripcion_curso']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        duracion = request.POST['duracion']
        horarios = request.POST['horarios']
        establecimiento = request.POST['establecimiento']
        costo = request.POST['costo']
        cupos_disponibles = request.POST['cupos_disponibles']
        estado = True  # Valor predeterminado False si el campo no está presente
        id_categoria = request.POST['id_categoria']
        curso = Curso(nombre_curso=nombre, descripcion_curso=descripcion,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,duracion=duracion,horarios=horarios,establecimiento=establecimiento,costo=costo,cupos_disponibles=cupos_disponibles,estado=estado,id_categoria_id=id_categoria)
        curso.save()
        return redirect('task:curso_view')
    return render(request, 'Cursos/create_curso.html')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def editar_curso_view(request,idcurso):
    curso = Curso.objects.get(id_curso=idcurso)
    notificaciones=Notificacion.objects.all()
    datos={
        'curso':curso,
        'notificaciones':notificaciones,
    }
    return render(request, 'Cursos/editar_curso.html',datos)

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def editar_curso(request,idcurso):
    notificaciones = Notificacion.objects.all()
    if request.method == 'POST':
        curso = Curso.objects.get(id_curso=idcurso)
        nombre = request.POST['nombre_curso']
        descripcion = request.POST['descripcion_curso']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        duracion = request.POST['duracion']
        horarios = request.POST['horarios']
        establecimiento = request.POST['establecimiento']
        costo = request.POST['costo']
        cupos_disponibles = request.POST['cupos_disponibles']
        estado = True  # Valor predeterminado False si el campo no está presente    
        id_categoria = request.POST['id_categoria']
        curso = Curso(id_curso=idcurso,nombre_curso=nombre, descripcion_curso=descripcion,fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,duracion=duracion,horarios=horarios,establecimiento=establecimiento,costo=costo,cupos_disponibles=cupos_disponibles,estado=estado,id_categoria_id=id_categoria)
        curso.save()
        
        return redirect('task:curso_view')
    return render(request, 'Cursos/editar_curso.html',{'notificaciones':notificaciones})

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def eliminar_curso(request,idcurso):
    curso = Curso.objects.get(id_curso=idcurso)
    curso.delete()
    return redirect('task:curso_view')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def search_categoria(request):
    search_term = request.GET.get('search')
    categorias = CategoriaCurso.objects.filter(Q(nombre_categoria__icontains=search_term))
    user_list = [{'id': categoria.id_categoria, 'text': categoria.nombre_categoria} for categoria in categorias]
    return JsonResponse(user_list, safe=False)


def formulario_view(request,idcurso):
    curso = Curso.objects.get(id_curso=idcurso)
    return render(request, 'Formulario/formulario.html',{'curso':curso})



def enviar_formulario(request,idcurso):
    if request.method == 'POST':
        dpi = request.POST['dpi']
        nombre = request.POST['nombre']
        genero = request.POST['genero']
        escolaridad = request.POST['escolaridad']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        etnia = request.POST['etnia']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        edad = request.POST['edad']
        estudiante = Estudiante(
            dpi=dpi,
            nombre=nombre,
            genero=genero,
            escolaridad=escolaridad,
            telefono=telefono,
            direccion=direccion,
            etnia=etnia,
            fecha_nacimiento=fecha_nacimiento,
            edad=edad,
            id_curso_id=idcurso,
        )
        estudiante.save()
        estudiante2=Estudiante.objects.get(dpi=dpi)
        fecha_inscripcion = timezone.now()
        id_estudiante=estudiante2.id_estudiante
        inscripcion = Inscripcion(
            fecha_inscripcion=fecha_inscripcion,
            id_curso_id=idcurso,
            id_estudiante_id=id_estudiante,
        )
        inscripcion.save()
        curso=Curso.objects.get(id_curso=idcurso)
        notifacion=Notificacion(
            mensaje=" a "+nombre+" le interesa el curso de "+curso.nombre_curso,
            fecha_creacion=fecha_inscripcion,
            id_inscripcion_id=inscripcion.id_inscripcion,
        )
        notifacion.save()
        
        return render(request, 'Formulario/registro_enviado.html')
    #return redirect('task:formulario_view',idcurso=idcurso)

  

def logout_view(request):
    logout(request)
    return redirect('task:login')

@login_required(login_url='task:login')
@user_passes_test(lambda u: u.is_superuser)
def search_Curso(request):
    notificaciones = Notificacion.objects.all()
    if request.method == 'POST':
        search = request.POST['search']
        curso = Curso.objects.filter(Q(nombre_curso__icontains=search) | Q(cupos_disponibles__icontains=search))
        datos={
            'cursos':curso,
            'notificaciones':notificaciones,
        }
        return render(request, 'Cursos/cursos.html',datos)

def estudiantes_view(request):
    estudiantes = Estudiante.objects.all()
    cursos=Curso.objects.all()
    notificaciones = Notificacion.objects.all()
    datos={
        'estudiantes':estudiantes,
        'cursos':cursos,
        'notificaciones':notificaciones,
    }
    return render(request, 'Estudiante/estudiantes.html', datos)

def usuarios_view(request):
    usuarios_view = Usuario.objects.all()
    notificaciones = Notificacion.objects.all()
    datos={
        'usuarios':usuarios_view,
        'notificaciones':notificaciones,
    }
    return render(request, 'Usuarios/usuarios.html', datos)

def editar_estudiante_view(request,idestudiante):
    estudiante = Estudiante.objects.get(id_estudiante=idestudiante)
    return render(request, 'Estudiante/editar.html',{'estudiante':estudiante}) 

def estudiantes_curso_filtro(request,idcurso):
    estudiantes = Estudiante.objects.filter(id_curso_id=idcurso)
    cursos=Curso.objects.all()
    notificaciones=Notificacion.objects.all()
    datos={
        'estudiantes':estudiantes,
        'cursos':cursos,
        'notificaciones':notificaciones,
    }
    return render(request, 'Estudiante/estudiantes.html', datos)

def editar_estudiante(request,idestudiante,idcurso):
    notificaciones=Notificacion.objects.all()
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(id_estudiante=idestudiante)
        dpi = request.POST['dpi']
        nombre = request.POST['nombre']
        genero = request.POST['genero']
        escolaridad = request.POST['escolaridad']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        etnia = request.POST['etnia']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        edad = request.POST['edad']
        estudiante = Estudiante(id_estudiante=idestudiante,dpi=dpi,nombre=nombre,genero=genero,escolaridad=escolaridad,telefono=telefono,direccion=direccion,etnia=etnia,fecha_nacimiento=fecha_nacimiento,edad=edad,id_curso_id=idcurso)
        estudiante.save()
        return redirect('task:estudiantes_view')
    return render(request, 'Estudiante/editar.html',{'notificaciones':notificaciones})

def usuarios_view(request):
    usuarios_view = Usuario.objects.all()
    notificaciones=Notificacion.objects.all()
    datos={
        'usuarios':usuarios_view,
        'notificaciones':notificaciones,
    }
    return render(request, 'Usuarios/usuarios.html', datos)

def crear_usuario_view(request):
    notificaciones=Notificacion.objects.all()
    return render(request, 'Usuarios/crear_usuario.html',{'notificaciones':notificaciones})
    
def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        dpi=request.POST['dpi']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        genero = request.POST['genero']
        escolaridad=request.POST['escolaridad']
        telefono=request.POST['telefono']
        direccion=request.POST['direccion']
        etnia=request.POST['etnia']
        fecha_nacimiento=request.POST['fecha_nacimiento']
        edad=request.POST['edad']
        if password == password2:
            password=make_password(password)
            usuario = Usuario(nombre=nombre, apellido=apellido,dpi=dpi, email=email, password=password,genero=genero,escolaridad=escolaridad,telefono=telefono,direccion=direccion,etnia=etnia,fecha_nacimiento=fecha_nacimiento,edad=edad)
            usuario.is_staff = True
            usuario.is_superuser = True
            usuario.save()
            return redirect('task:usuarios_view')
        else:
            return redirect('task:crear_usuario_view')
    return render(request, 'Usuarios/crear_usuario.html')

def editar_usuario_view(request,idusuario):
    usuario = Usuario.objects.get(id_usuario=idusuario)
    notificaciones=Notificacion.objects.all()
    datos={
        'usuario':usuario,
        'notificaciones':notificaciones,
    }
    return render(request, 'Usuarios/editar_usuario.html',datos)

from django.contrib.auth.hashers import make_password

def editar_usuario(request, idusuario):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        dpi = request.POST['dpi']
        email = request.POST['email']
        password = request.POST.get('password')  # Usamos get para manejar la ausencia de password
        password2 = request.POST.get('password2')  # Usamos get para manejar la ausencia de password2
        genero = request.POST['genero']
        escolaridad=request.POST['escolaridad']
        telefono=request.POST['telefono']
        direccion=request.POST['direccion']
        etnia=request.POST['etnia']
        edad=request.POST['edad']
        fecha_nacimiento=request.POST['fecha_nacimiento']
        try:
            usuario = Usuario.objects.get(id_usuario=idusuario)
        except Usuario.DoesNotExist:
            # Manejar el caso en que el usuario no existe
            return redirect('task:usuarios_view')
        
        # Actualiza los campos del usuario
        usuario.nombre = nombre
        usuario.apellido = apellido
        usuario.dpi = dpi
        usuario.email = email
        usuario.genero = genero
        usuario.escolaridad = escolaridad
        usuario.telefono = telefono
        usuario.direccion = direccion
        usuario.etnia = etnia
        usuario.fecha_nacimiento = fecha_nacimiento
        usuario.edad = edad
        
        # Verifica si el campo de contraseña ha cambiado
        if password:
            if password == password2:
                usuario.password = make_password(password)
            else:
                return redirect('task:editar_usuario_view', idusuario=idusuario)
        
        # Guarda los cambios en la base de datos
        usuario.save()
        
        return redirect('task:usuarios_view')

    # Recuerda pasar el objeto `usuario` a la plantilla para mostrar los datos existentes.
    return render(request, 'Usuarios/editar_usuario.html', {'usuario': usuario})

def eliminar_usuario(request, idusuario):
    usuario = Usuario.objects.get(id_usuario=idusuario)
    usuario.delete()
    return redirect('task:usuarios_view')

from api.models import CategoriaCurso



def categoriaCursos(request):
    if request.method == 'POST':
        nombre_categoria = request.POST['nombre_categoria']
        descripcion_categoria = request.POST['descripcion_categoria']
        
        # Crea una nueva instancia de CategoriaCurso y guárdala en la base de datos
        nueva_categoria = CategoriaCurso(nombre_categoria=nombre_categoria, descripcion_categoria=descripcion_categoria)
        nueva_categoria.save()
        return redirect('task:categoria_curso_view')
    
    

def categoria_curso_view(request):
    categorias = CategoriaCurso.objects.all() 
    
    return render(request, 'Categorias/CategoriasCursos.html', {'categorias': categorias})


  
def editar_categoria_view(request,categoria_id):
    categorias = CategoriaCurso.objects.get(id_categoria=categoria_id)
    return render(request, 'Categorias/editar_categoria.html',{'categorias':categorias})

def editar_categoria(request, categoria_id):
    if request.method == 'POST':
        categoria=CategoriaCurso.objects.get(id_categoria=categoria_id)
        nombre=request.POST['nombre_categoria']
        descripcion=request.POST['descripcion_categoria']
        categoria=CategoriaCurso(id_categoria=categoria_id, nombre_categoria=nombre, descripcion_categoria=descripcion)
        categoria.save()
        return redirect('task:categoria_curso_view')
    return render(request, 'Categorias/editar_categoria.html')

def eliminar_categoria(request,categoria_id):
    categoria=CategoriaCurso.objects.get(id_categoria=categoria_id)
    categoria.delete()
    return redirect('task:categoria_curso_view')
           
    