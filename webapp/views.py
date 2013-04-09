from django.shortcuts import render_to_response
from facepy import GraphAPI

def home(request):
    # test for successful login
    try: 
        access_token = request.user.social_auth.all().get(user=request.user, provider='facebook').extra_data['access_token']

        # pull the birthday data from facebook
        data_amount = pull_facebook(access_token)


        return render_to_response('loggedin.html')
    except AttributeError:
        return render_to_response('main.html')

def pull_facebook(access_token):
    graph = GraphAPI(access_token)


