# @Author: Arjit Srivastava
# @https://github.com/arjitsrivastava007


"""
    Role Based Access Control:
    Implementing a role based auth system. System should be able to assign a role to user and remove a user from the role.

    Entities are USER, ACTION TYPE, RESOURCE, ROLE

    ACTION TYPE defines the access level(Ex: _read, _write, _delete)

    Access to resources for users are controlled strictly by the role.One user can have multiple roles. 
    Given a user, action type and resource system should be able to tell whether user has access or not.
"""


class AccessControl(object):
    """
    Defines the detailed access control rules
    If a role is not given an explicit resource authorisation, it's rejected by default. Rule of Least privileges.
    """

    def __init__(self):
        self._read = []
        self._write = []
        self._delete = []

    def resource_read_rule(self, role, access, resource):
        """
        Add rules to allow read access
        :param role:
        :param access:
        :param resource:
        """
        permission = (role.get_name(), access, resource)
        if permission not in self._read:
            self._read.append(permission)

    def resource_write_rule(self, role, access, resource):
        """
        Add rules to allow write access
        :param role:
        :param access: 
        :param resource:
        """
        permission = (role.get_name(), access, resource)
        if permission not in self._write:
            self._write.append(permission)

    def resource_delete_rule(self, role, access, resource):
        """
        Add rules to allow full access.
        :param role:
        :param access:
        :param resource:
        """
        permission = (role.get_name(), access, resource)
        if permission not in self._delete:
            self._delete.append(permission)

    def is_read_allowed(self, role, access, resource):
        """
        returns whether the role is allowed READ access resource
        :return: Boolean
        """
        return (role, access, resource) in self._read

    def is_write_allowed(self, role, access, resource):
        """
        returns whether the role is allowed WRITE access resource
        :return: Boolean
        """
        return (role, access, resource) in self._write

    def is_delete_allowed(self, role, access, resource):
        """
        returns whether the role is allowed DELETE access resource
        :return: Boolean
        """
        return (role, access, resource) in self._delete
