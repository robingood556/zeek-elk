from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import yaml
from jinja2 import Environment, FileSystemLoader
import os
from pathlib import Path



def index(request):
    return render(request, "index.html")

def validate(request):
    if request.method == 'POST':
        BASE_DIR = Path(__file__).resolve().parent.parent
        es_data = []
        env = Environment(loader = FileSystemLoader(os.path.join(BASE_DIR, 'zeek/templates/')), trim_blocks=True, lstrip_blocks=True)
        template = env.get_template('test.j2')
        username = request.POST['username']
        nodes = int(request.POST['nodes'])

        for i in range(nodes):
           es_data.append("es" + str(i))
        
        es_data = ','.join(es_data)      
        dict = {
        
            'username': username,
            'nodes': nodes,
            'es_data': es_data
        }
        file=open("docker-compose"+".yaml", "w")
        file.write(template.render(dict))
        file.close()
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")

    return render(request, "validate.html")

def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)








# Create your views here.
