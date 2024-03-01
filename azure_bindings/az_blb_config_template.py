class StorageAccountConfig:
    def __init__(self):
        self.config = {
            'account_name' : 'abc123',
            'account_key' : 'abc123',
            'container_name' : 'abc123',
            'blob_name' : 'abc123.json'
        }   
    
    def get_config(self):
        return self.config