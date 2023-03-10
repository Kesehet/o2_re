# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._availability_sets_operations import AvailabilitySetsOperations
from ._virtual_machine_extension_images_operations import VirtualMachineExtensionImagesOperations
from ._virtual_machine_extensions_operations import VirtualMachineExtensionsOperations
from ._virtual_machines_operations import VirtualMachinesOperations
from ._virtual_machine_images_operations import VirtualMachineImagesOperations
from ._usage_operations import UsageOperations
from ._virtual_machine_sizes_operations import VirtualMachineSizesOperations
from ._virtual_machine_scale_sets_operations import VirtualMachineScaleSetsOperations
from ._virtual_machine_scale_set_vms_operations import VirtualMachineScaleSetVMsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AvailabilitySetsOperations",
    "VirtualMachineExtensionImagesOperations",
    "VirtualMachineExtensionsOperations",
    "VirtualMachinesOperations",
    "VirtualMachineImagesOperations",
    "UsageOperations",
    "VirtualMachineSizesOperations",
    "VirtualMachineScaleSetsOperations",
    "VirtualMachineScaleSetVMsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
