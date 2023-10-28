from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from .models import CategoriaCurso
from .models import Curso
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password



