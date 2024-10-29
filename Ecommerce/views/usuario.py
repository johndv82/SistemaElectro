from django.shortcuts import render, redirect
import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from ..decorators import token_required

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
            # Realizar solicitud POST para obtener el token
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

@token_required
def micuenta(request):
    usuario = request.user
    context = {
        'usuario': usuario
    }
    return render(request, 'micuenta.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Verifica que las contraseñas coincidan
        if password != password2:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect('Ecommerce:register') 

        # Verifica que el usuario no exista ya
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso")
            return redirect('Ecommerce:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "El email ya está en uso")
            return redirect('Ecommerce:register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.') 
        return redirect('Ecommerce:login_view') 

    return render(request, 'register.html')  # Renderiza el formulario si no es un POST