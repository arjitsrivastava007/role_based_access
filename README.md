# role_based_access
Implement a role based auth system. System should be able to assign a role to a user and remove a role from a user.

## Installation Instructions

1. Move to directory where you want to clone project

2. Download python 2.7,
https://www.python.org/downloads/release/python-276/

```bash
$ git clone https://github.com/arjitsrivastava007/role_based_access.git
$ cd role_based_access
$ python -m install pip
$ python -m pip install virtualenv
$ python -m virtualenv venv
$ source venv/bin/activate
(venv)$ pip install pytest==3.1.0
(venv)$ python run.py
```

## Demo

### Role creation and assignment of role to a User

```python
from role_based_access import Role, User


default_role = Role('default')
admin_role = Role('admin')

default_user = User(roles=[default_role])
admin_user = User(roles=[admin_role, default_role])
```

### User resource access permissions allocation

```python
from role_based_access import AccessControl, Role, User


everyone_role = Role('everyone')
admin_role = Role('admin')

everyone_user = User(roles=[everyone_role])
admin_user = User(roles=[admin_role, everyone_role])

acl = AccessControl()

# assign permission to everyone role
acl.resource_read_rule(everyone_role, 'read', 'my_folder')

# assign permission to admin role
acl.resource_read_rule(admin_role, 'read', 'my_folder')
acl.resource_write_rule(admin_role, 'write', 'my_folder')
acl.resource_delete_rule(admin_role, 'delete', 'my_folder')

# checking READ operation on resource for user `everyone_user`
for user_role in [role.get_name() for role in everyone_user.get_roles()]:
    assert acl.is_read_allowed(user_role, 'read', 'my_folder') == True

# checking WRITE operation on resource for user `everyone_user`
# Since you have not defined the rule for the particular, it will disallow any such operation by default.
for user_role in [role.get_name() for role in everyone_user.get_roles()]:
    assert acl.is_write_allowed(user_role, 'write', 'my_folder') == False
```


## Tests

`role_based_access` uses `py.test` for running the tests, running which is as simple as doing a

```bash
$ py.test
```

## RBAC in simple terms

<p align="center">
  <img src="http://tasdikrahman.me/content/images/2017/06/rbac_model.jpg" alt="rbac"/>
</p>
