from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from django.http import HttpResponseRedirect
# Create your views here.

access_token = "APP_USR-7436991723557344-020311-e49490b817d09b0b99decac7a82f611d-1144777955"


def get_acess_token(request):
    url = 'https://api.mercadolibre.com/oauth/token'
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'client_id': '7436991723557344',
        'client_secret': 'GxJZ0vEm1ZWWxgbU3uHWbq75IU9bPbq1',
        'refresh_token': 'TG-65be59bdaddec100016ccca9-1144777955'
    }

    response = requests.post(url, headers=headers, data=data)
    data = response.json()
    access_token = data['access_token']
    print(data)
    return HttpResponse(access_token)


def get_user_data_by_id(access_token):
    url = f'https://api.mercadolibre.com/users/1144777955'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)




def page_redirect(request):
    return HttpResponseRedirect('page-redirect')


def mercado_livre_user(request):
    api_url = "https://api.mercadolibre.com/users/1144777955"

    response = requests.get(api_url)

    if response.status_code == 200:

        user_data = response.json()

        return render(request, 'consultas/user.html', {'user_data': user_data})
    else:
        return HttpResponse("erro")
