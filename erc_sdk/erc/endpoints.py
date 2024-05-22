class ERCEndpoints:
    def __init__(self, client):
        self.client = client

    def get_resource(self, resource_id):
        return self.client.get(f'resources/{resource_id}')

    def create_resource(self, data):
        return self.client.post('resources', data)
