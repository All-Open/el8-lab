# System Registration

!!! warning "RHEL only step!"
    This step is only needed if you are using Red Hat (r) Enterprise Linux (r).
    If not, proceed to the next step.

!!! tip
    This step can be skipped if you are running RHEL in Public Cloud. <br/>
    Public Cloud instances have RHEL subscription included in instance costs.

## Why is Registration Needed?

All Open Labs require `yum` software repositories content very often.

Red Hat (r) Enterprise Linux (r) `yum` repositories are not publicly accessible. Therefore, you have to register to make then available.

## Registration process

If your system is not registered, use the following command:
```
# subscription-manager register --username <username> --password <password> --auto-attach
```

If it fails, follow [this guide](https://access.redhat.com/solutions/253273) to understand and troubleshoot registration process.
