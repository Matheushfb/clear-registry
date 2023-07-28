import docker_registry_client
import requests
import os
from dotenv import load_dotenv

load_dotenv()
page=os.environ['url']
tags_keep = int(os.environ['tags_to_keep'])
drc=docker_registry_client.DockerRegistryClient(page)
bc=docker_registry_client.BaseClient(page)


response = requests.request(url="https://registry.123milhas.com/v2/_catalog?n=100000",method="GET")

lista_parseada = []

def parseia(response):
    get_values = response.content.decode()
    get_repo_names = get_values.split("[")[1]
    lista_separate_by_comma = get_repo_names.split(',')
    for i in list(lista_separate_by_comma):
        retira_aspas = "".join(i).replace('"', "")
        retira_chaves_colchetes = "".join(retira_aspas).replace("]}","")
        lista_parseada.append(retira_chaves_colchetes)
    return lista_parseada

#print(len(parseia(response)))
repositorios = parseia(response)

print(lista[144])

print(page+"v2/"+lista[144]+"/manifests/"+"v1.5.2")

#for i in parseia(response):
#    print(i)


#separa_repositorios = list(separa_aspas.split(","))
#print(page+"v2/"+separa_repositorios+"/manifests/"+"1223")

#list(bc.get_repository_tags(repository="akatsuki/bf-emission-flow-frontend").values())


#print(namespaces)
#result = bc.get_repository_tags(namespaces).keys()
#print(result)

#i=0
#namespaces = drc.namespaces()
#print(namespaces)
#while i < len(namespaces):
#    repositorios = drc.repositories(namespaces[i])
#    lista_repositorios = list(repositorios)
#    for j in lista_repositorios:
#        get_infos=list(bc.get_repository_tags(j).values())
#        tags = get_infos[1]
#        repo_name = get_infos[0]
#        if len(tags) < tags_keep:
#            print("Nenhuma ação. O arepositório" ,repo_name, "possui menos que", tags_keep ,"tags registradas.")
#        else:
#            tags_elegibles_for_delete=(tags[:len(tags) - tags_keep])
#            for k in tags_elegibles_for_delete:
#                url_manifests = (page+"v2/"+repo_name+"/manifests/"+k)
#                payload = {'Accept': 'application/vnd.docker.distribution.manifest.v2+json'}
#                response=requests.get(url=url_manifests, headers=payload)
#                manifest = response.headers.get("Docker-Content-Digest")
#                url_to_delete = (page + "v2/" + repo_name + "/manifests/" + manifest)
#                print(url_to_delete)
#    i = i + 1
