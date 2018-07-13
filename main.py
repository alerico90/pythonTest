from flask import Flask
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.web.models.certificate import Certificate

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    #define credentials for authentication
auth = {
    'tenant_id': 'XXXXXXXXXXXXXXXXX',
    'client_id': 'XXXXXXXXXXXXXXXXX',
    'key': 'XXXXXXXXXXXXXXX',
}

#define which subscription ID we are doing the actions
subscription_id = 'XXXXXXXXXXXXXXXXXXXXXX';

#create a credentials object
credentials = ServicePrincipalCredentials(client_id=auth['client_id'], secret=auth['key'], tenant=auth['tenant_id']);

#instantiate the management client for WebApp
webSiteManagementClient = WebSiteManagementClient(credentials, subscription_id);

#creates a hostname in the given WebApp Slot
hostNameBinding = webSiteManagementClient.web_apps.create_or_update_host_name_binding_slot(resource_group_name='botdoc-api-front', name='botdoc-api-front', slot='sandbox', host_name='testingggg.botdoc.io', host_name_binding={});


  return 'Hello, World!'

if __name__ == '__main__':
  app.run()
