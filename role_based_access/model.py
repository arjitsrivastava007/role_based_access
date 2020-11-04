# -*- coding: utf-8 -*-
# @Author: Arjit Srivastava
# @https://github.com/arjitsrivastava007

import utils



class Role(object):
    """roles which are associated to permissions to access resources

    :param name: the name of the role
    """

    roles = {}

    def __init__(self, name=None):
        """
        Initializes the a role with the permissions associated with it.
        """
        self.name = name
        Role.roles[name] = self

    def add_role(self, role, access):
        """
        Add role along with its access type
        :param role:
        :param access:
        :return:
        """

        self.roles[role] = utils.ACCESS_TYPE[access]

    def get_role(self, role):
        """
        returns the access type of the role
        """
        return self.roles[role]

    def remove_role(self, role):
        """
        Removes a role
        :param role:
        :return:
        """

        self.roles.pop(role)


class Resource(object):
    """
    Adding Resources
    """

    def __init__(self):
        self.resources = []

    def add_resource(self, resource):
        """
        Adds the role to this user

        :param role: the role to be assigned to the user
        """
        self.resources.extend(resource)

    def get_resources(self):
        """
        Returns a list of all Resources
        """
        return self.resources

    def get_resource(self, resource):
        """
        Returns resource if present
        :param resource:
        :return:
        """
        if resource in self.resources:
            return resource
        else:
            raise Exception("{0} not present.".format(resource))

    def remove_resource(self, resource):
        """
        Removes resource if present
        :param resource:
        :return:
        """

        if resource in self.resources:
            self.resources.remove(resource)
        else:
            raise Exception("{0} not present.".format(resource))
