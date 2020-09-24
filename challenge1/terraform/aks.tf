resource "azurerm_resource_group" "codechg-#{VAR_ENVIRONMENT_NAME}#" {
  name     = "codechg-#{VAR_ENVIRONMENT_NAME}#-resources"
  location = "West Europe"
}

resource "azurerm_kubernetes_cluster" "codechg-#{VAR_ENVIRONMENT_NAME}#" {
  name                = "codechg-#{VAR_ENVIRONMENT_NAME}#-aks1"
  location            = azurerm_resource_group.codechg-#{VAR_ENVIRONMENT_NAME}#.location
  resource_group_name = azurerm_resource_group.codechg-#{VAR_ENVIRONMENT_NAME}#.name
  dns_prefix          = "codechgaks1-#{VAR_ENVIRONMENT_NAME}#"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "#{VAR_ENVIRONMENT_NAME}#"
  }
}

output "client_certificate" {
  value = azurerm_kubernetes_cluster.codechg-#{VAR_ENVIRONMENT_NAME}#.kube_config.0.client_certificate
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.codechg-#{VAR_ENVIRONMENT_NAME}#.kube_config_raw
}
