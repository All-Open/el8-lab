# System-wide Cryptographic Policies

## Description
The purpose of this lab is to ensure the operating system is compliant with the ever growing security requirements.

## Task list
* Using System-wide crypto policies, set policy level that:
    * does not allow SHA-1 in signature algorithms
    * enforces RH and RSA keys of at least 3072-bit key length
* Due to compatibility restrictions, SSH daemon should be excluded from system-wide crypto policy settings
* Configure Apache web server:
    * to serve any content at `https://localhost`
    * leave system-default `localhost.crt` and `localhost.key` location

## Setup
Execute
```console
# all-open-lab setup crypto-policies
```

## Grading
Execute
```console
# all-open-lab grade crypto-policies
```
