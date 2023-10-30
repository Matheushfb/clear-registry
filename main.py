import docker_registry_client
import requests
import os
from dotenv import load_dotenv

load_dotenv()
page=os.environ['url']
tags_keep = int(os.environ['tags_to_keep'])
drc=docker_registry_client.DockerRegistryClient(page)
bc=docker_registry_client.BaseClient(page)

i=0
namespaces = drc.namespaces()
while i < len(namespaces):
    repositorios = drc.repositories(namespaces[i])
    lista_repositorios = list(repositorios)
    for j in lista_repositorios:
        get_infos=list(bc.get_repository_tags(j).values())
        tags = get_infos[1]
        repo_name = get_infos[0]
        if len(tags) < tags_keep:
            print("Nenhuma ação. O repositório" ,repo_name, "possui menos que", tags_keep ,"tags registradas.")
        else:
            tags_elegibles_for_delete=(tags[:len(tags) - tags_keep])
            for k in tags_elegibles_for_delete:
                url_manifests = (page+"v2/"+repo_name+"/manifests/"+k)
                payload = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
                response=requests.get(url=url_manifests, headers=payload)
                manifest = response.headers.get("Docker-Content-Digest")
                url_to_delete = (page + "v2/" + repo_name + "/manifests/" + manifest)
                print(url_to_delete)
    i = i + 1
