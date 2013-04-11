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

    # offset used for paginating Facebook users
    offset = 0
    full_data = graph.get('me/friends?fields=id,name,birthday&offset='+str(offset))

    # remove the paging portions
    data = full_data['data']

    # keep scraping until no more material
    while not not full_data['data']:
        data = full_data['data']

        counter = 0 
        if 'birthday' in data[counter]:
            return data[counter]['birthday']

        counter+=1

        offset += 1000 # inc offset each time to search for more facebook users and paginate

        print "Finished one loop, starting another"

        # Make the pagination request
        full_data = graph.get('me/friends?fields=id,name,birthday&offset='+str(offset))

    

    return data


