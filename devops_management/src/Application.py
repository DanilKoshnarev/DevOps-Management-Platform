from src.domain.entities.Deployment import Deployment
from src.domain.repositories.DeploymentRepository import DeploymentRepository
from src.domain.services.DeploymentService import DeploymentService
from src.domain.usecases.ManageDeployment import ManageDeployment
from src.infrastructure.models.DeploymentModel import DeploymentModel
from src.infrastructure.controllers.DeploymentController import DeploymentController

def main():
    deployment_repository = DeploymentModel()
    deployment_service = DeploymentService(deployment_repository)
    manage_deployment = ManageDeployment(deployment_service)
    deployment_controller = DeploymentController(manage_deployment)

    
    deployment_controller.add_deployment("1", "App1", "Production", "1.0.0", "Success", "2025-02-17T10:00:00")
    deployment_controller.add_deployment("2", "App2", "Staging", "2.0.0", "InProgress", "2025-02-17T10:30:00")

    
    for deployment in deployment_controller.get_all_deployments():
        print(f"ID: {deployment.id}, Application: {deployment.application}, Environment: {deployment.environment}, Version: {deployment.version}, Status: {deployment.status}, Timestamp: {deployment.timestamp}")

  
    deployment_controller.delete_deployment("1")

    
    for deployment in deployment_controller.get_all_deployments():
        print(f"ID: {deployment.id}, Application: {deployment.application}, Environment: {deployment.environment}, Version: {deployment.version}, Status: {deployment.status}, Timestamp: {deployment.timestamp}")

if __name__ == "__main__":
    main()
