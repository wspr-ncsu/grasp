import serverless.parsers.ManagedPolicyDict as ManagedPolicyDict

def managed_policy(policy):
    policy_name = policy.split('/')[-1]

    if policy_name not in ManagedPolicyDict.policies:
        raise NotImplementedError('{} not defined.'.format(policy))

    return ManagedPolicyDict.policies[policy_name]['Document']['Statement']