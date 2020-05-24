# Terminal Recording

## Description
The purpose of this lab is to configure terminal session recording.

## Setup
Execute
```console
# all-open-lab setup terminal-recording
```

## Task list
* Ensure that software that enables terminal recording is installed
* Ensure that `cockpit` can be used to configure and play recorded terminal sessions
* In `/etc/sssd/conf.d/sssd-session-recording.conf`, enable session recording for all users and groups
* At the start of a terminal session, a user should be notified that their session is being recorded with `Your session is recorded and ALL OPEN!` banner
* All sessions are recorded to `journal`

## Grading
Execute
```console
# all-open-lab grade terminal-recording
```
