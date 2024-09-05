from flask import Flask, render_template
from kubernetes import client, config

app = Flask(__name__)

# Kubeconfig dosyasını yükle
config.load_kube_config(config_file='C:/Users/DELL/.kube/config')
v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

@app.route('/')
def index():
    namespaces = v1.list_namespace().items
    pods = v1.list_pod_for_all_namespaces(watch=False).items
    deployments = apps_v1.list_deployment_for_all_namespaces().items
    replica_sets = apps_v1.list_replica_set_for_all_namespaces().items
    services = v1.list_service_for_all_namespaces().items

    return render_template('index.html',
                           namespaces=namespaces,
                           pods=pods,
                           deployments=deployments,
                           replica_sets=replica_sets,
                           services=services)

if __name__ == "__main__":
    app.run(debug=True)
