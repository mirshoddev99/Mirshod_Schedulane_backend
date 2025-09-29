import os

# Deployment settings


# AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY')

# INSTALLED_APPS += ['storages']
# AZURE_ACCOUNT_NAME = 'schedulanestorage'
# AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY')
# AZURE_CONTAINER = 'media'
# MEDIA_URL = f'https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/{AZURE_CONTAINER}/'
# AZURE_SSL = True


# DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'



from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = "schedulanestorage"  # Must be replaced by your storage account name
    account_key = os.environ.get("AZURE_ACCOUNT_KEY")  # Securely set in environment
    azure_container = "media"
    expiration_secs = None


DEFAULT_FILE_STORAGE = 'backend.storage_backends.AzureMediaStorage'
MEDIA_URL = "https://schedulanestorage.blob.core.windows.net/media/"

