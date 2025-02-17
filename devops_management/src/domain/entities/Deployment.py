class Deployment:
    def __init__(self, id, application, environment, version, status, timestamp):
        self.id = id
        self.application = application
        self.environment = environment
        self.version = version
        self.status = status
        self.timestamp = timestamp

    # Getters and Setters
