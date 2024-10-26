from django.shortcuts import redirect
from django.contrib.auth.models import User
from functools import wraps
import requests
from django.conf import settings
from django.core.cache import cache

def token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        token = request.session.get('auth_token')
        if not token:
            return redirect('Ecommerce:login_view')
        
        user_data = cache.get(f'user_data_{token}')
        
        if user_data is None:  # Si no está en caché, realiza la solicitud a la API

            response_user = requests.get(
                f"{settings.ECOMMERCEAPI_URL}/auth/users/me/",
                headers={'Authorization': f'Token {token}'}
            )
            
            if response_user.status_code == 200:
                user_data = response_user.json()
                cache.set(f'user_data_{token}', user_data, timeout=3600)
            else:
                return redirect('Ecommerce:login_view')
            
        # Asigna el usuario al request
        user = User.objects.get(id=user_data['id'])
        request.user = user 

        return view_func(request, *args, **kwargs)
    return _wrapped_view