# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import NetworkInterfacesOperations
from ._operations import ApplicationGatewaysOperations
from ._operations import NetworkManagementClientOperationsMixin
from ._operations import ExpressRouteCircuitAuthorizationsOperations
from ._operations import ExpressRouteCircuitPeeringsOperations
from ._operations import ExpressRouteCircuitsOperations
from ._operations import ExpressRouteServiceProvidersOperations
from ._operations import LoadBalancersOperations
from ._operations import NetworkSecurityGroupsOperations
from ._operations import SecurityRulesOperations
from ._operations import NetworkWatchersOperations
from ._operations import PacketCapturesOperations
from ._operations import PublicIPAddressesOperations
from ._operations import RouteTablesOperations
from ._operations import RoutesOperations
from ._operations import UsagesOperations
from ._operations import VirtualNetworksOperations
from ._operations import SubnetsOperations
from ._operations import VirtualNetworkPeeringsOperations
from ._operations import VirtualNetworkGatewaysOperations
from ._operations import VirtualNetworkGatewayConnectionsOperations
from ._operations import LocalNetworkGatewaysOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "NetworkInterfacesOperations",
    "ApplicationGatewaysOperations",
    "NetworkManagementClientOperationsMixin",
    "ExpressRouteCircuitAuthorizationsOperations",
    "ExpressRouteCircuitPeeringsOperations",
    "ExpressRouteCircuitsOperations",
    "ExpressRouteServiceProvidersOperations",
    "LoadBalancersOperations",
    "NetworkSecurityGroupsOperations",
    "SecurityRulesOperations",
    "NetworkWatchersOperations",
    "PacketCapturesOperations",
    "PublicIPAddressesOperations",
    "RouteTablesOperations",
    "RoutesOperations",
    "UsagesOperations",
    "VirtualNetworksOperations",
    "SubnetsOperations",
    "VirtualNetworkPeeringsOperations",
    "VirtualNetworkGatewaysOperations",
    "VirtualNetworkGatewayConnectionsOperations",
    "LocalNetworkGatewaysOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
