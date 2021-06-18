from functools import wraps
from django.shortcuts import redirect

def register_signin_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if 'register_id' in request.session and kwargs['pk'] == request.session['register_id']:
            return function(request, *args, **kwargs)
        else:
            return redirect('amapp:login')
    
    return wrap
