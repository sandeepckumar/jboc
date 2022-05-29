# jboc
A jboss CLI utility based on management API for quick adhoc operations.

```text
Usage: jboc [OPTIONS] COMMAND [ARGS]...

  An adhoc Jboss Command Line Utility, to make your life easy.

Options:
  -h, --url TEXT        jboss management url
  -u, --username TEXT   username for connecting to jboss management api
  -p, --password TEXT   password for connecting to jboss management api
  -v, --verify BOOLEAN  verify SSL connection/certs  [default: False]
  -c, --certs TEXT      ca cert path, valid only if verify is TRUE
  --version             shows version package_name prog_name
  --help                Show this message and exit.

Commands:
  add-user                   Provision RBAC user with a specific role
  get-standalone-deployment  Lists all deployments for standalone profile
  get-user                   Lists all RBAC users
```
## Examples
### 1. Get current users
```shell
$ jboc -u admin --url "https://10.10.10.10:9993" get-users
Password []:

+---------------------+-----------+
|        Name         |   Role    |
+---------------------+-----------+
|     User2           | Deployer  |
|     User1           |  Monitor  |
|     $local          | SuperUser |
|  sandeep.chenna     | SuperUser |
+---------------------+-----------+
```
### 2. Add new user

```shell
$ jboc -u admin --url "https://10.10.10.10:9993" add-user --help
Usage: jboc add-user [OPTIONS]

  Provision RBAC user with a specific role

Options:
  -u, --username TEXT             username to be added  [required]
  -r, --role [Monitor|Operator|Maintainer|Deployer|Auditor|Administrator|SuperUser]
                                  available roles [Monitor, Operator,
                                  Maintainer, Deployer, Auditor,
                                  Administrator, SuperUser] (case-sensitive)
                                  [required]
  --help                          Show this message and exit.

$ jboc -u admin --url "https://10.10.10.10:9993" add-user -u new-user -r Monitor
[SUCCESS] -- URL: https://10.10.10.10:9993 -- USER: new-user -- ROLE: Monitor -- Provisioned
```
### 3. List standalone deployments
```shell
$  jboc.exe -u admin -p 'cleartextpassword'--url "https://10.10.10.10:9993" get-standalone-deployment
deployement1.war
deployment2.war
```