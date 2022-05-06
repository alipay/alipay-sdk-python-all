#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrgNodeDTO import OrgNodeDTO
from alipay.aop.api.domain.UserDTO import UserDTO


class OrgRoleDTO(object):

    def __init__(self):
        self._node = None
        self._role = None
        self._user_list = None

    @property
    def node(self):
        return self._node

    @node.setter
    def node(self, value):
        if isinstance(value, OrgNodeDTO):
            self._node = value
        else:
            self._node = OrgNodeDTO.from_alipay_dict(value)
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def user_list(self):
        return self._user_list

    @user_list.setter
    def user_list(self, value):
        if isinstance(value, list):
            self._user_list = list()
            for i in value:
                if isinstance(i, UserDTO):
                    self._user_list.append(i)
                else:
                    self._user_list.append(UserDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.node:
            if hasattr(self.node, 'to_alipay_dict'):
                params['node'] = self.node.to_alipay_dict()
            else:
                params['node'] = self.node
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.user_list:
            if isinstance(self.user_list, list):
                for i in range(0, len(self.user_list)):
                    element = self.user_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_list[i] = element.to_alipay_dict()
            if hasattr(self.user_list, 'to_alipay_dict'):
                params['user_list'] = self.user_list.to_alipay_dict()
            else:
                params['user_list'] = self.user_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrgRoleDTO()
        if 'node' in d:
            o.node = d['node']
        if 'role' in d:
            o.role = d['role']
        if 'user_list' in d:
            o.user_list = d['user_list']
        return o


