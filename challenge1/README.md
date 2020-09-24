# Time Taken: 45 min
# Introduction 
   TODO: Code Pipeline to deploy AKS, kubectl, helm and 3-Tier Environment
# Getting Started
    Installation process
   	Create Azure Service Account with Client ID & Client Secret
    	Please refer the variable name in the config.tf
    	Create a storage blob container to host the state files
    	Create and call the new pipeline and Execute run
    	Give environment variable of your choice during execution
# Yet to do
    Naming Standards
    parameterize Network and the number of nodes etc
    parameterize passwords
    store kubeconfig in secret management vault and use IAM to get kubeconfig at runtime
    separate infrastructure pipeline and application pipeline
    Use application pipeline to query vault and use kubeconfig 
# Variable_groups & Variables
        TF_STATE    
        Description                     Variables   
        VAR_STATE_ACCESS_KEY            ********
        VAR_STATE_CONTAINER_NAME        <stg_container_name>
        VAR_STATE_STORAGE_ACCOUNT_NAME  <stg_account_name>

        AKS_SUBSCRIPTION
        Description                     Variables
        VAR_CLIENT_ID                   ********
        VAR_CLIENT_SECRET               ********
        VAR_SUBSCRIPTION_ID             ********
        VAR_TENANT_ID                   ********
