import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes import config

def initiate_api():
    """Function to Initiate Kubernetes API"""
    configuration = config.load_kube_config()
    api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))
    return api_instance

def list_limits():
    """Function to list Limits of Namespaces"""
    try:
        api_instance = initiate_api()
        namespaces = api_instance.list_namespace().items
        for namespace in namespaces:
            limit = api_instance.list_namespaced_limit_range(namespace.metadata.name).items
            if not limit:
                print(namespace.metadata.name + " named namespace don't have any limits")
            else:
                print(limit)
    except ApiException as e:
        print("Exception when calling list_namespaced_limit_range: %s\n" % e)

def main_function():
    list_limits()

main_function()
