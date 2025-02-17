from src.domain.entities.Deployment import Deployment

class ManageDeployment:
    def __init__(self, deployment_service):
        self.deployment_service = deployment_service

    def create_deployment(self, id, application, environment, version, status, timestamp):
        deployment = Deployment(id, application, environment, version, status, timestamp)
        self.deployment_service.add_deployment(deployment)

    def view_deployment(self, id):
        return self.deployment_service.get_deployment(id)

    def view_all_deployments(self):
        return self.deployment_service.get_all_deployments()

    def remove_deployment(self, id):
        self.deployment_service.delete_deployment(id)
