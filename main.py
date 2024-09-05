from kubernetes import client, config

# Kubeconfig dosyasını yükle
config.load_kube_config(config_file='C:/Users/DELL/.kube/config')

# API istemcisi oluştur
v1 = client.CoreV1Api()

# Namespace'leri al
print("Namespaces:")
namespaces = v1.list_namespace()
for ns in namespaces.items:
    print(ns.metadata.name)

# Pod'ları al
print("\nPods:")
pods = v1.list_pod_for_all_namespaces(watch=False)
for pod in pods.items:
    print(f"{pod.metadata.namespace} - {pod.metadata.name}")

# Deployment'ları al
apps_v1 = client.AppsV1Api()
print("\nDeployments:")
deployments = apps_v1.list_deployment_for_all_namespaces()
for deploy in deployments.items:
    print(f"{deploy.metadata.namespace} - {deploy.metadata.name}")

# ReplicaSets'leri al
print("\nReplicaSets:")
replica_sets = apps_v1.list_replica_set_for_all_namespaces()
for rs in replica_sets.items:
    print(f"{rs.metadata.namespace} - {rs.metadata.name}")

# Services'leri al
print("\nServices:")
services = v1.list_service_for_all_namespaces()
for svc in services.items:
    print(f"{svc.metadata.namespace} - {svc.metadata.name}")