from src.domain.repositories.DeploymentRepository import DeploymentRepository

class DeploymentModel(DeploymentRepository):
    def __init__(self):
        self.deployments = []

    def save(self, deployment):
        self.deployments.append(deployment)

    def find_by_id(self, id):
        return next((deployment for deployment in self.deployments if deployment.id == id), None)

    def find_all(self):
        return self.deployments

    def delete(self, id):
        self.deployments = [deployment for deployment in self.deployments if deployment.id != id]
