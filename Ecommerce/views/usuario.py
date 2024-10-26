from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings

def login_view(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()

        if not user:
            messages.error(request, 'Credenciales incorrectas')
        else:
            # Realizar solicitud POST al endpoint de Djoser para obtener el token
            response_token = requests.post(
                f"{settings.ECOMMERCEAPI_URL}/auth/token/login/",
                json={'username': user.username, 'password': password}
            )

            if response_token.status_code == 200:
                token = response_token.json().get('auth_token')
                # Guardar el token en la sesión de Django
                request.session['auth_token'] = token
                return redirect('Ecommerce:productos')
            else:
                messages.error(request, 'Credenciales incorrectas')

    return redirect('Ecommerce:login_view')


def logout(request):
    auth.logout(request)  # Desconecta al usuario
    return redirect('Ecommerce:login_view')