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
