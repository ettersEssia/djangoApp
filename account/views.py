from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import redirect
from .models import project, parallelepiped, pipe
# il faut bien penser a ajouter le « @csrf_exempt » et importer la librairie associée sinon Django refusera tout simplement les données. C’est une sécurité qui est en place par défaut de façon à vérifier que le POST vient bien du client qui a demandé la page. Cette dernière n’est pas utilisable en Ajax il faut donc la désactiver.
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render_to_response
import json

@login_required()
def home(request):
    return render(request, 'account/home.html')

def new_project(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return render(request, 'account/new_project.html')

@csrf_exempt
def list_project(request):
    print("________________________________msg:")
    print(10/10*2)
    comp = {}
    projetList = {}

    projets = project.objects.all().filter(owner_id=request.user.id)
    pipes = pipe.objects.all()
    cubes = parallelepiped.objects.all()

    for projet in projets:
        for p in pipes:
            if (p.project_id == projet.id):
                comp[p.name] = p
        for cube in cubes:
            if (cube.project_id == projet.id):
                comp[cube.name] = cube
        projetList[projet.name] = comp
        comp = {}

    print("resultat: \n")
    print(projetList)

    context = {
        'projectDetails': projetList
    }
    return render(request, 'account/list_projects.html', context)

@csrf_exempt
def delete_project(request):
    post = request.POST['projet']
    projet = json.loads(post)
    print(projet['name'])
    reponse = project.objects.filter(name=projet['name']).delete()
    return HttpResponse(json.dumps({'msg': reponse}), content_type="application/json")

@csrf_exempt
def save_project(request):
    try:
        post = request.POST['projet']
        # le post est au format json. On le désérialize
        projet = json.loads(post)
        # newProject
        # on affiche chaque élément. Ici vous devez faire votre traitement, une insertion
        # en base de données par exemple
        for element in projet:
            name = element['name']
            print ("Un projet du nom de %s", name)
            # ajout du projet à la base
            newProject = project.objects.create(name=name, owner=request.user)
            cube = element['cube']
            for champs in cube:
                parallelepiped.objects.create(name=champs['name'], length=champs['length'], color=champs['color'], project=newProject)
            pipeTab = element['pipe']
            for champs in pipeTab:
                pipe.objects.create(name=champs['name'], length=champs['length'], inDiam=champs['inDiam'], outDiam=champs['outDiam'], color=champs['color'], project=newProject)
    except IntegrityError as e:
        return HttpResponse(json.dumps({'msg': e.args}), content_type="application/json")

    return HttpResponse(json.dumps({'msg': 'success'}), content_type="application/json")

    # supprimer le projet ayant comme valeur pr le chmps (name) 'projet 1'
    # project.objects.filter(name='p').delete()

    # on fait un retour au client
    # json data est maintenant au format JSON et pret à etre envoyé au client
    # return HttpResponse(json.dumps({'msg': newProject}), content_type="application/json")

def logoutnlogin(request):
    return logout_then_login(request,login_url=None)
