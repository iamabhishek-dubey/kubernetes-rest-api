import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes import config

def initiate_api():
    """Function to Initiate Kubernetes API"""
    configuration = config.load_kube_config()
    api_instance = kubernetes.client.CoreV1Api(kubernetes.client.ApiClient(configuration))
    return api_instance

def list_quota():
    """Function to list Quota of Namespaces"""
    try:
        api_instance = initiate_api()
        namespaces = api_instance.list_namespace().items
        for namespace in namespaces:
            quota = api_instance.list_namespaced_resource_quota(namespace.metadata.name).items
            if not quota:
                print(namespace.metadata.name + " named namespace don't have any quota")
            else:
                print(quota)
    except ApiException as e:
        print("Exception when calling list_namespace_resource_quota: %s\n" % e)

def main_function():
    list_quota()

main_function()
