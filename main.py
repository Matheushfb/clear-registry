import subprocess

import docker_registry_client
from io import BytesIO
import requests
import scrapy
from docker_registry_client.Repository import RepositoryV1
from docker_registry_client._BaseClient import BaseClientV1
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()
import pycurl
page=os.environ['url']
drc=docker_registry_client.DockerRegistryClient(page)
bc=docker_registry_client.BaseClient(page)


#print(bc.MANIFEST)
#namespaces = drc.namespaces()
#print(namespaces[0])
#get_info=list(bc.get_repository_tags(namespaces[0],'akatsuki/emissao').values())
#get_info=list(bc.get_repository_tags('akatsuki/emissao').values())
#print(get_info)
#tags = get_info[1]
#repo_name = get_info[0]
#print(tags)
#print(repo_name)
#bc.delete_repository_tag(repo_name,'1.15.0')
#bc.delete_repository_tag(namespaces[0],repo_name,'1.15.0')
#print(manifest)
#bc.delete_manifest(repo_name,'')
i=0
namespaces = drc.namespaces()
while i < len(namespaces):
    repositorios = drc.repositories(namespaces[i])
    lista_repositorios = list(repositorios)
    for j in lista_repositorios:
        get_infos=list(bc.get_repository_tags(j).values())
        tags = get_infos[1]
        repo_name = get_infos[0]
        if len(tags) < 5 :
            print("Nenhuma ação. O repositório" ,repo_name, "possui menos que 5 tags registradas.")
        else:
            tags_elegibles_for_delete=(tags[:len(tags) - 5])  #Pega a lista de tags exceto as 5 mais recentes
            for k in tags_elegibles_for_delete:
                #teste=bc.get_manifest_and_digest(repo_name,k)
                #print(repo_name,k,teste[1])
                url_manifests = ("https://registry.123milhas.com/v2/"+repo_name+"/"+"manifests/"+k)
                payload = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
                response=requests.get(url=url_manifests, headers=payload)
                manifest = response.headers.get("Docker-Content-Digest")
                url_to_delete = ("https://registry.123milhas.com/v2/" + repo_name + "/" + "manifests/" + manifest)
                print(url_to_delete)
    i = i + 1
