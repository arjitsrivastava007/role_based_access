"""
Testing assignment and deletion of a Role to User
"""

from role_based_access import Role, User


default_role = Role('default')
admin_role = Role('admin')

default_user = User(name='default_user', roles=[default_role])
admin_user = User(name='admin_user', roles=[admin_role, default_role])


class TestRoleAssignmentDeletion:

    def test_role_assignment(self):
        """
        Creates the roles which need to be assigned to users
        """
        assert [role.get_name() for role in default_user.get_roles()] == ['default']
        assert [role.get_name() for role in admin_user.get_roles()].sort() == ['admin', 'default'].sort()

    def test_delete_role_from_user(self):
        """
        Tests the function to delete a role from a user
        Since 'admin' role has be removed from 'anonymous_user' so condition for checking admin role in anonymous_user will evaluate to false
        """
        anonymous_user = User(roles=[default_role, admin_role])
        anonymous_user.remove_role('admin')
        assert 'admin' not in [role.get_name() for role in anonymous_user.get_roles()]

    def test_delete_user(self):
        """
        Tests successful deletion of user
        """
        anonymous_user = User(roles=[default_role])
        del anonymous_user
        assert 'anonymous_user' not in dir()