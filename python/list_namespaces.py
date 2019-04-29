import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes import config

def initiate_api():
    """Function to Initiate Kubernetes API"""
    configuration = config.load_kube_config()
    api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))
    return api_instance

def list_namespaces():
    """Function to list namespace using Kubernetes Rest API"""
    try:
        api_instance = initiate_api()
        namespaces = api_instance.list_namespace().items
        for namespace in namespaces:
            if namespace.metadata.name is not None:
                print(namespace.metadata)
    except ApiException as e:
        print("Exception when list_namespace: %s\n" % e)

def main_function():
    """Main Function for calling other functions"""
    list_namespaces()

main_function()
