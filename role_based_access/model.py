# @Author: Arjit Srivastava
# @https://github.com/arjitsrivastava007


class Role(object):
    """
    Roles which are associated to permissions to access resources
    """

    def __init__(self, name):
        """
        Initializes the a role with the permissions associated with it.
        """
        self.name = name

    def get_name(self):
        """
        returns the name of the role
        """
        return self.name

    def __repr__(self):
        return '<Role %s>' % self.name


class User(object):
    """
    Manages User
    """

    def __init__(self, name, roles=[]):
        """Initialises the roles assigned to the user when created or updated later
        :param roles: <list> object which holds the roles assigned to the user
        """
        self.roles = set(roles)
        self.name = name

    def get_name(self):
        """
        returns the name of the role
        """
        return self.name

    def add_role(self, role):
        """Adds the role to this user

        :param role: the role to be assigned to the user
        """
        self.roles.extend(role)

    def get_roles(self):
        """Returns a generator object for the roles held by the User
        """
        for role in self.roles.copy():
            yield role

    def remove_role(self, role_name):
        """Remove a role assigned to a User

        :param role_name: name of the role which needs to be removed
        """
        for role in self.get_roles():
            if role.get_name() == role_name:
                self.roles.remove(role)

    def __repr__(self):
        return '<User %s %s>' % (self.name, self.roles)
