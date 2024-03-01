class StorageAccountConfig:
    def __init__(self):
        self.config = {
            'account_name' : '<overwrite>',
            'account_key' : '<overwrite>',
            'container_name' : '<overwrite>',
            'blob_name' : '<overwrite>.json'
        }   
    
    def get_config(self):
        return self.config