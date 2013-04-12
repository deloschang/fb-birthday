# this is mysterious code territory----
from webapp.models import * 

from django.shortcuts import render_to_response
from facepy import GraphAPI

def home(request):
    # test for successful login
    try: 
        access_token = request.user.social_auth.all().get(user=request.user, provider='facebook').extra_data['access_token']

        # pull the birthday data from facebook
        #data = pull_facebook(access_token)
        data = access_token  # set later for manual link



        return render_to_response('loggedin.html', {'data':data} )
    except AttributeError:
        return render_to_response('main.html')

# pull the birthday information
def pull_facebook(access_token):
    # clean database first



    graph = GraphAPI(access_token)

    # offset used for paginating Facebook users
    offset = 0
    LIMIT = 5000
    full_data = graph.get('me/friends?fields=id,name,birthday&limit='+str(LIMIT)+'+offset='+str(offset))

    # remove the paging portions
    data = full_data['data']


    #### TESTING facebook post functionality #####
    friend_id='me'
    
    message='Check 1 2 3'
    #graph.post(path=friend_id+"/feed", retry=1, message=message)
    
    permissions = graph.get('me/permissions')
    print permissions


    counter = 0  # count how many loaded into DB

    # keep scraping until no more material
    while not not full_data['data']:
        data = full_data['data']

        # parse out
        for i in range(0,len(data)):
            if 'birthday' in data[i]:
                print data[i]['id'],
                print data[i]['name'],
                print data[i]['birthday']

                # add user to the db
                new_person = Person(name = data[i]['name'], uid = data[i]['id'], birthday = data[i]['birthday'])

                try:
                    new_person.save()
                    print new_person.name + " loaded to database."
                    counter += 1
                except:
                    print "Error on " + new_person.name
                    print str(i) + " loaded."
                    import pdb;
                    pdb.set_trace()


        offset += 5000 # inc offset each time to search for more facebook users and paginate

        print "Finished one loop, starting another"

        # Make the pagination request
        full_data = graph.get('me/friends?fields=id,name,birthday&offset='+str(offset))

    print str(counter) + " total people loaded into database."
    print + " ============================== "


    return data

# commence the search
def search(request):
    pass

