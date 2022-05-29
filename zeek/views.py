from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import yaml
from jinja2 import Environment, FileSystemLoader
import os
import subprocess
from pathlib import Path
import json


def index(request):

    return render(request, "index.html")


def validate(request):

    if request.method == 'POST':

        BASE_DIR = Path(__file__).resolve().parent.parent
        es_data = []
        env = Environment(loader = FileSystemLoader(os.path.join(BASE_DIR, 'zeek/templates/')), trim_blocks=True, lstrip_blocks=True)

        template_docker = env.get_template('docker.j2')
        template_env = env.get_template('env.j2')

        username = request.POST['username']
        password = request.POST['password']
        nodes = int(request.POST['nodes'])

        for number in range(1, nodes+1):
           es_data.append("es0" + str(number))
        

        es_data = ','.join(es_data)
      
        dict = {
        
            'username': username,
            'password': password,
            'nodes': nodes,
            'es_data': es_data
        }

        file_docker = open("docker-compose"+".yml", "w")
        file_docker.write(template_docker.render(dict))
        file_docker.close()

        file_env = open(".env", "w")
        file_env.write(template_env.render(dict))
        file_env.close()
        

        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))

        subprocess.call(["docker compose up -d"], shell=True)

    return render(request, "validate.html")


def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + 'net.pcap', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    os.system('cp upload/net.pcap filebeat/')

# Create your views here.
