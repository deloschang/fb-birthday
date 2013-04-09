from django.shortcuts import render_to_response
from facepy import GraphAPI

def home(request):
    # test for successful login
    try: 
        access_token = request.user.social_auth.all().get(user=request.user, provider='facebook').extra_data['access_token']

        # pull the birthday data from facebook
        data = pull_facebook(access_token)


        return render_to_response('loggedin.html', {'data':data} )
    except AttributeError:
        return render_to_response('main.html')

# pull the birthday information
def pull_facebook(access_token):
    graph = GraphAPI(access_token)

    full_data = graph.get('me/friends?fields=id,name,birthday')

    import pdb;
    pdb.set_trace()

    # remove the paging portions
    data = full_data['data']


