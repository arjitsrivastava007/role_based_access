from role_based_access import AccessControl, User, Role

everyone_role = Role('everyone')
admin_role = Role('admin')

everyone_user = User(roles=[everyone_role])
admin_user = User(roles=[admin_role, everyone_role])


acl = AccessControl()

acl.resource_read_rule(everyone_role, 'read', 'document')
acl.resource_delete_rule(admin_role, 'delete', 'admin_panel')


class TestPermissions():

    def test_read_rule_everyone(self):
        """
        checking resource access with the employee himself in context
        """
        for user_role in [role.get_name() for role in everyone_user.get_roles()]:
            assert acl.is_read_allowed(user_role, 'read', 'document') == True

    def test_write_rule_everyone(self):
        """
        write operation by the role 'everyone' should fail
        """
        for user_role in [role.get_name() for role in everyone_user.get_roles()]:
            assert acl.is_write_allowed(user_role, 'WRITE', 'document') == False

    def test_delete_rule_admin(self):
        """
        admin role should be able to delete
        """
        for user_role in [role.get_name() for role in everyone_user.get_roles()]:
            if user_role == 'admin':
                assert acl.is_delete_allowed(user_role, 'delete', 'admin_panel') == True
            else:
                assert acl.is_delete_allowed(user_role, 'delete', 'admin_panel') == False