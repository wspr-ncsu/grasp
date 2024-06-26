import re
from typing import Dict, List, Any, Pattern

from checkov.common.models.enums import CheckResult, CheckCategories
from checkov.terraform.checks.provider.base_check import BaseProviderCheck
from checkov.common.models.consts import linode_token_pattern


class LinodeCredentials(BaseProviderCheck):
    def __init__(self) -> None:
        name = "Ensure no hard coded Linode tokens exist in provider"
        id = "CKV_LIN_1"
        supported_provider = ("linode",)
        categories = (CheckCategories.SECRETS,)
        super().__init__(name=name, id=id, categories=categories, supported_provider=supported_provider)

    def scan_provider_conf(self, conf: Dict[str, List[Any]]) -> CheckResult:
        if self.secret_found(conf, "token", linode_token_pattern):
            return CheckResult.FAILED
        return CheckResult.PASSED

    @staticmethod
    def secret_found(conf: Dict[str, List[Any]], field: str, pattern: Pattern[str]) -> bool:
        if field in conf.keys():
            value = conf[field][0]
            if re.match(pattern, value) is not None:
                return True
        return False


check = LinodeCredentials()
