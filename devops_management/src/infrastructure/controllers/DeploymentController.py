class DeploymentController:
    def __init__(self, manage_deployment):
        self.manage_deployment = manage_deployment

    def add_deployment(self, id, application, environment, version, status, timestamp):
        self.manage_deployment.create_deployment(id, application, environment, version, status, timestamp)

    def get_deployment(self, id):
        return self.manage_deployment.view_deployment(id)

    def get_all_deployments(self):
        return self.manage_deployment.view_all_deployments()

    def delete_deployment(self, id):
        self.manage_deployment.remove_deployment(id)
