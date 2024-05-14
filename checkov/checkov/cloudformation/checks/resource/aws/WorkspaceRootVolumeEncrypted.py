from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.cloudformation.checks.resource.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.consts import ANY_VALUE


class WorkspaceRootVolumeEncrypted(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure that Workspace root volumes are encrypted"
        id = "CKV_AWS_156"
        supported_resources = ['AWS::WorkSpaces::Workspace']
        categories = [CheckCategories.ENCRYPTION]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'Properties/RootVolumeEncryptionEnabled'


check = WorkspaceRootVolumeEncrypted()
