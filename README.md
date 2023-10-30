# clear-registry
Script para limpar imagens do Docker Registry.

Para utilizar esse script primeiramente instale a biblioteca docker_registry_client
através do comando "pip install docker-registry-client"

Para um correto funcionamento será necessária uma alteração no codigo fonte, para identificar 
onde está o codigo fonte utilize o seguinte comando pip show --files docker-registry-client

Agora podemos realizar a alteração na linha 176 do arquivo _BaseClient.py  
altere de  return self._http_call('/v2/_catalog', get) para  return self._http_call('/v2/_catalog?n=10000', get)

Fazendo isso todos os Namespaces serão carregados corretamente!