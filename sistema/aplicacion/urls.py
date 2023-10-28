from django import views
from .import views
from django.urls import path

app_name = 'task'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('create_curso_view/', views.create_curso_view, name='create_curso_view'),
    path('create_curso/', views.create_curso, name='create_curso'),
    path('curso_view/', views.curso_view, name='curso_view'),
    path('editar_curso_view/<int:idcurso>/', views.editar_curso_view, name='editar_curso_view'),
    path('editar_curso/<int:idcurso>/', views.editar_curso, name='editar_curso'),
    path('eliminar_curso/<int:idcurso>/', views.eliminar_curso, name='eliminar_curso'),
    path('search_categoria/', views.search_categoria, name='search_categoria'),
    path('formulario_view/<int:idcurso>/', views.formulario_view, name='formulario_view'),
    path('enviar_formulario/<int:idcurso>/', views.enviar_formulario, name='enviar_formulario'),
    path('estudiantes_view/', views.estudiantes_view, name='estudiantes_view'),
    path('logout/', views.logout_view, name='logout'),
    path('search_curso/', views.search_Curso, name='search_curso'),
    path('estudiante_view/', views.estudiantes_view, name='estudiante_view'),
    path('estudiantes_curso_filtro/<int:idcurso>/', views.estudiantes_curso_filtro, name='estudiantes_curso_filtro'),
    path('editar_estudiante_view/<int:idestudiante>/', views.editar_estudiante_view, name='editar_estudiante_view'),
    path('editar_estudiante/<int:idestudiante>/<int:idcurso>/', views.editar_estudiante, name='editar_estudiante'),
    path('usuarios_view/', views.usuarios_view, name='usuarios_view'),
    path('crear_usuario_view/', views.crear_usuario_view, name='crear_usuario_view'),
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('editar_usuario_view/<int:idusuario>/', views.editar_usuario_view, name='editar_usuario_view'),
    path('editar_usuario/<int:idusuario>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:idusuario>/', views.eliminar_usuario, name='eliminar_usuario'),

    path('categoria_cursos/', views.categoriaCursos, name='categoria_cursos'),
    path('agregar_categoria_curso', views.categoriaCursos, name='agregar_categoria_curso'),

    path('mostrar_categorias', views.categoriaCursos, name='mostrar_categorias'),
    path('editar_categoria_view/<int:categoria_id>/', views.editar_categoria_view, name='editar_categoria_view'),
    path('agregar_categoria_curso', views.editar_categoria, name='agregar_categoria_curso'),
    path('editar_categoria/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categoria_curso_view/', views.categoria_curso_view, name='categoria_curso_view'),
    path('eliminar_categoria/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),    

    
]