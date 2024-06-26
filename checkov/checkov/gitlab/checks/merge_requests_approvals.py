from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.gitlab.base_gitlab_configuration_check import BaseGitlabCheck
from checkov.gitlab.schemas.project_approvals import schema as project_aprovals_schema
from checkov.json_doc.enums import BlockType


class MergeRequestRequiresApproval(BaseGitlabCheck):
    def __init__(self):
        name = "Merge requests should require at least 2 approvals"
        id = "CKV_GITLAB_1"
        categories = [CheckCategories.SUPPLY_CHAIN]
        super().__init__(
            name=name,
            id=id,
            categories=categories,
            supported_entities=["*"],
            block_type=BlockType.DOCUMENT
        )

    def scan_entity_conf(self, conf):
        if project_aprovals_schema.validate(conf):
            if conf.get("approvals_before_merge", 0) < 2:
                return CheckResult.FAILED, conf
            return CheckResult.PASSED, conf


check = MergeRequestRequiresApproval()
