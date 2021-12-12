# jboc
A jboss CLI based on management API for quick adhoc operations.

```text
Usage: jboc [OPTIONS] URL COMMAND [ARGS]...

  An adhoc Jboss Command Line Utility, to make your life easy.

Options:
  -u, --username TEXT   username for connecting to jboss management api
  -p, --password TEXT   password for connecting to jboss management api
  -v, --verify BOOLEAN  verify SSL connection/certs  [default: False]
  -c, --certs TEXT      ca cert path, valid only if verify is TRUE
  --help                Show this message and exit.

Commands:
  add-user  Provision RBAC user with a specific role
  get-user  Lists all RBAC users

```
