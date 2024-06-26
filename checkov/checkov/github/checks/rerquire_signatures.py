from checkov.github.base_github_branch_security import BranchSecurity


class GithubBranchCommitSignature(BranchSecurity):
    def __init__(self):
        name = "Ensure GitHub branch protection rules requires signed commits"
        id = "CKV_GITHUB_4"
        super().__init__(
            name=name,
            id=id
        )

    def get_evaluated_keys(self):
        return ['required_signatures/enabled']


check = GithubBranchCommitSignature()
