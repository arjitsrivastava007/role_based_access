import sys, getopt
from role_based_access import AccessControl, User, Role

"""
1. Ability to assign a role to a user.
2. Ability to remove a role from a user.
3. Given a user, action type and resource, the system should be able to tell whether user has access or not.
"""

selected_int_input = [1, 2, 3, 4]


def main():

    # Creating roles
    everyone_role = Role('everyone')
    admin_role = Role('admin')
    normal_role = Role('normal_role')

    # Creating user and assigning roles to user
    everyone_user = User(name='everyone_user', roles=[everyone_role])
    normal_user = User(name='normal_user', roles=[normal_role, everyone_role])
    admin_user = User(name='admin_user', roles=[admin_role, everyone_role])

    acl = AccessControl()

    # assign permission to everyone role
    acl.resource_read_rule(everyone_role, 'read', 'my_folder')

    # assign permission to normal role
    acl.resource_read_rule(normal_role, 'read', 'my_folder')
    acl.resource_write_rule(normal_role, 'write', 'my_folder')

    # assign permission to admin role
    acl.resource_read_rule(admin_role, 'read', 'document')
    acl.resource_write_rule(admin_role, 'write', 'document')
    acl.resource_delete_rule(admin_role, 'delete', 'document')

    acl.resource_read_rule(admin_role, 'read', 'users_list')
    acl.resource_write_rule(admin_role, 'write', 'users_list')
    acl.resource_delete_rule(admin_role, 'delete', 'users_list')

    acl.resource_read_rule(admin_role, 'read', 'my_folder')
    acl.resource_write_rule(admin_role, 'write', 'my_folder')
    acl.resource_delete_rule(admin_role, 'delete', 'my_folder')

    # checking READ operation on resource for user `everyone_user`
    for user_role in [role.get_name() for role in everyone_user.get_roles()]:
        assert acl.is_read_allowed(user_role, 'read', 'my_folder') == True

    # checking WRITE operation on resource for user `admin_user`
    for user_role in [role.get_name() for role in admin_user.get_roles()]:
        if acl.is_write_allowed(user_role, 'write', 'document'):
            assert True

    # checking WRITE operation on resource for user `everyone_user`
    # Since you have not defined the rule for the particular, it will disallow any such operation by default.
    for user_role in [role.get_name() for role in everyone_user.get_roles()]:
        assert acl.is_write_allowed(user_role, 'write', 'my_folder') == False


    # Remove role from user
    normal_user.remove_role(everyone_role.get_name())

    #print(user_input())

def user_input():

    try:
        inp = int(input())
    except Exception as err:
        print("Invalid input, enter only integer from above given options")
        inp = user_input()

    if not inp in selected_int_input:
        print("Invalid input, enter integer from above given options")
        inp = user_input()

    return inp




if __name__ == "__main__":
    main()
