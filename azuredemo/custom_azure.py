from storages.backends.azure_storage import AzureStorage

# class AzureMediaStorage(AzureStorage):
#     account_name = 'storageblob123' # Must be replaced by your <storage_account_name>
#     account_key = 'gkynzn+CXD+yOLfJAIMin0PS/JzYh6/OW3IlGIywTPMvaXsz4rLgomMd4gisdMRMYvcXnhSpunTBbgsCOxN0aQ==' # Must be replaced by your <storage_account_key>
#     azure_container = 'media'
#     expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'azuredemoblob123' # Must be replaced by your storage_account_name
    account_key = 'kw9gMcBjYSyKZ/C4pSEhrytMAUHoMVaNxJw50xfPJqVDWl7QmogmrI0Akz9UYW6+KGRA3mvnzaHu+AStJ86Kgw==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None