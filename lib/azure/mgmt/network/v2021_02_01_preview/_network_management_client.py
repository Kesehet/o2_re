# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import NetworkManagementClientConfiguration
from .operations import (
    ActiveConnectivityConfigurationsOperations,
    ActiveSecurityAdminRulesOperations,
    ActiveSecurityUserRulesOperations,
    AdminRuleCollectionsOperations,
    AdminRulesOperations,
    ConnectivityConfigurationsOperations,
    EffectiveConnectivityConfigurationsOperations,
    EffectiveVirtualNetworksOperations,
    NetworkGroupsOperations,
    NetworkManagerCommitsOperations,
    NetworkManagerDeploymentStatusOperations,
    NetworkManagerEffectiveSecurityAdminRulesOperations,
    NetworkManagersOperations,
    NetworkSecurityPerimetersOperations,
    NspAccessRulesOperations,
    NspAccessRulesReconcileOperations,
    NspAssociationReconcileOperations,
    NspAssociationsOperations,
    NspLinkReconcileOperations,
    NspLinkReferenceReconcileOperations,
    NspLinkReferencesOperations,
    NspLinksOperations,
    NspProfilesOperations,
    PerimeterAssociableResourceTypesOperations,
    SecurityAdminConfigurationsOperations,
    SecurityUserConfigurationsOperations,
    UserRuleCollectionsOperations,
    UserRulesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class NetworkManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Network Client.

    :ivar network_managers: NetworkManagersOperations operations
    :vartype network_managers:
     azure.mgmt.network.v2021_02_01_preview.operations.NetworkManagersOperations
    :ivar network_manager_commits: NetworkManagerCommitsOperations operations
    :vartype network_manager_commits:
     azure.mgmt.network.v2021_02_01_preview.operations.NetworkManagerCommitsOperations
    :ivar network_manager_deployment_status: NetworkManagerDeploymentStatusOperations operations
    :vartype network_manager_deployment_status:
     azure.mgmt.network.v2021_02_01_preview.operations.NetworkManagerDeploymentStatusOperations
    :ivar effective_virtual_networks: EffectiveVirtualNetworksOperations operations
    :vartype effective_virtual_networks:
     azure.mgmt.network.v2021_02_01_preview.operations.EffectiveVirtualNetworksOperations
    :ivar active_connectivity_configurations: ActiveConnectivityConfigurationsOperations operations
    :vartype active_connectivity_configurations:
     azure.mgmt.network.v2021_02_01_preview.operations.ActiveConnectivityConfigurationsOperations
    :ivar active_security_admin_rules: ActiveSecurityAdminRulesOperations operations
    :vartype active_security_admin_rules:
     azure.mgmt.network.v2021_02_01_preview.operations.ActiveSecurityAdminRulesOperations
    :ivar active_security_user_rules: ActiveSecurityUserRulesOperations operations
    :vartype active_security_user_rules:
     azure.mgmt.network.v2021_02_01_preview.operations.ActiveSecurityUserRulesOperations
    :ivar connectivity_configurations: ConnectivityConfigurationsOperations operations
    :vartype connectivity_configurations:
     azure.mgmt.network.v2021_02_01_preview.operations.ConnectivityConfigurationsOperations
    :ivar effective_connectivity_configurations: EffectiveConnectivityConfigurationsOperations
     operations
    :vartype effective_connectivity_configurations:
     azure.mgmt.network.v2021_02_01_preview.operations.EffectiveConnectivityConfigurationsOperations
    :ivar network_manager_effective_security_admin_rules:
     NetworkManagerEffectiveSecurityAdminRulesOperations operations
    :vartype network_manager_effective_security_admin_rules:
     azure.mgmt.network.v2021_02_01_preview.operations.NetworkManagerEffectiveSecurityAdminRulesOperations
    :ivar network_groups: NetworkGroupsOperations operations
    :vartype network_groups:
     azure.mgmt.network.v2021_02_01_preview.operations.NetworkGroupsOperations
    :ivar security_user_configurations: SecurityUserConfigurationsOperations operations
    :vartype security_user_configurations:
     azure.mgmt.network.v2021_02_01_preview.operations.SecurityUserConfigurationsOperations
    :ivar user_rule_collections: UserRuleCollectionsOperations operations
    :vartype user_rule_collections:
     azure.mgmt.network.v2021_02_01_preview.operations.UserRuleCollectionsOperations
    :ivar user_rules: UserRulesOperations operations
    :vartype user_rules: azure.mgmt.network.v2021_02_01_preview.operations.UserRulesOperations
    :ivar security_admin_configurations: SecurityAdminConfigurationsOperations operations
    :vartype security_admin_configurations:
     azure.mgmt.network.v2021_02_01_preview.operations.SecurityAdminConfigurationsOperations
    :ivar admin_rule_collections: AdminRuleCollectionsOperations operations
    :vartype admin_rule_collections:
     azure.mgmt.network.v2021_02_01_preview.operations.AdminRuleCollectionsOperations
    :ivar admin_rules: AdminRulesOperations operations
    :vartype admin_rules: azure.mgmt.network.v2021_02_01_preview.operations.AdminRulesOperations
    :ivar network_security_perimeters: NetworkSecurityPerimetersOperations operations
    :vartype network_security_perimeters:
     azure.mgmt.network.v2021_02_01_preview.operations.NetworkSecurityPerimetersOperations
    :ivar nsp_profiles: NspProfilesOperations operations
    :vartype nsp_profiles: azure.mgmt.network.v2021_02_01_preview.operations.NspProfilesOperations
    :ivar nsp_access_rules: NspAccessRulesOperations operations
    :vartype nsp_access_rules:
     azure.mgmt.network.v2021_02_01_preview.operations.NspAccessRulesOperations
    :ivar nsp_associations: NspAssociationsOperations operations
    :vartype nsp_associations:
     azure.mgmt.network.v2021_02_01_preview.operations.NspAssociationsOperations
    :ivar nsp_association_reconcile: NspAssociationReconcileOperations operations
    :vartype nsp_association_reconcile:
     azure.mgmt.network.v2021_02_01_preview.operations.NspAssociationReconcileOperations
    :ivar perimeter_associable_resource_types: PerimeterAssociableResourceTypesOperations
     operations
    :vartype perimeter_associable_resource_types:
     azure.mgmt.network.v2021_02_01_preview.operations.PerimeterAssociableResourceTypesOperations
    :ivar nsp_access_rules_reconcile: NspAccessRulesReconcileOperations operations
    :vartype nsp_access_rules_reconcile:
     azure.mgmt.network.v2021_02_01_preview.operations.NspAccessRulesReconcileOperations
    :ivar nsp_links: NspLinksOperations operations
    :vartype nsp_links: azure.mgmt.network.v2021_02_01_preview.operations.NspLinksOperations
    :ivar nsp_link_reconcile: NspLinkReconcileOperations operations
    :vartype nsp_link_reconcile:
     azure.mgmt.network.v2021_02_01_preview.operations.NspLinkReconcileOperations
    :ivar nsp_link_references: NspLinkReferencesOperations operations
    :vartype nsp_link_references:
     azure.mgmt.network.v2021_02_01_preview.operations.NspLinkReferencesOperations
    :ivar nsp_link_reference_reconcile: NspLinkReferenceReconcileOperations operations
    :vartype nsp_link_reference_reconcile:
     azure.mgmt.network.v2021_02_01_preview.operations.NspLinkReferenceReconcileOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft
     Azure subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2021-02-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = NetworkManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.network_managers = NetworkManagersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_manager_commits = NetworkManagerCommitsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_manager_deployment_status = NetworkManagerDeploymentStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.effective_virtual_networks = EffectiveVirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.active_connectivity_configurations = ActiveConnectivityConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.active_security_admin_rules = ActiveSecurityAdminRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.active_security_user_rules = ActiveSecurityUserRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.connectivity_configurations = ConnectivityConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.effective_connectivity_configurations = EffectiveConnectivityConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_manager_effective_security_admin_rules = NetworkManagerEffectiveSecurityAdminRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_groups = NetworkGroupsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.security_user_configurations = SecurityUserConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.user_rule_collections = UserRuleCollectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.user_rules = UserRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.security_admin_configurations = SecurityAdminConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.admin_rule_collections = AdminRuleCollectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.admin_rules = AdminRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.network_security_perimeters = NetworkSecurityPerimetersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.nsp_profiles = NspProfilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.nsp_access_rules = NspAccessRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.nsp_associations = NspAssociationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.nsp_association_reconcile = NspAssociationReconcileOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.perimeter_associable_resource_types = PerimeterAssociableResourceTypesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.nsp_access_rules_reconcile = NspAccessRulesReconcileOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.nsp_links = NspLinksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.nsp_link_reconcile = NspLinkReconcileOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.nsp_link_references = NspLinkReferencesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.nsp_link_reference_reconcile = NspLinkReferenceReconcileOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "NetworkManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details) -> None:
        self._client.__exit__(*exc_details)
