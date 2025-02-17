class DeploymentService:
    def __init__(self, deployment_repository):
        self.deployment_repository = deployment_repository

    def add_deployment(self, deployment):
        self.deployment_repository.save(deployment)

    def get_deployment(self, id):
        return self.deployment_repository.find_by_id(id)

    def get_all_deployments(self):
        return self.deployment_repository.find_all()

    def delete_deployment(self, id):
        self.deployment_repository.delete(id)
