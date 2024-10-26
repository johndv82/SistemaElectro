from django.shortcuts import redirect
from django.contrib.auth.models import User
from functools import wraps
import requests
from django.conf import settings

def token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        token = request.session.get('auth_token')
        if not token:
            return redirect('Ecommerce:login_view')
        
        response_user = requests.get(
            f"{settings.ECOMMERCEAPI_URL}/auth/users/me/",
            headers={'Authorization': f'Token {token}'}
        )
        
        if response_user.status_code == 200:
            user_data = response_user.json()
            print(user_data)
            user = User.objects.get(id=user_data['id'])
            request.user = user  # Asigna el usuario autenticado al request

        return view_func(request, *args, **kwargs)
    return _wrapped_view