terraform {
  backend "azurerm" {
    storage_account_name = "#{VAR_STATE_STORAGE_ACCOUNT_NAME}#"
    container_name       = "#{VAR_STATE_CONTAINER_NAME}#"
    key                  = "#{VAR_ENVIRONMENT_NAME}#/AKS.tfstate"
    access_key           = "#{VAR_STATE_ACCESS_KEY}#"
  }
}

provider "azurerm" {
  client_id       = "#{VAR_CLIENT_ID}#"
  client_secret   = "#{VAR_CLIENT_SECRET}#"
  subscription_id = "#{VAR_SUBSCRIPTION_ID}#"
  tenant_id       = "#{VAR_TENANT_ID}#"
  features {}
}

