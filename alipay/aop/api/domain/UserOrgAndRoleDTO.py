#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserSubOrgAndRoleDTO import UserSubOrgAndRoleDTO


class UserOrgAndRoleDTO(object):

    def __init__(self):
        self._id = None
        self._org_id = None
        self._org_name = None
        self._passport_id = None
        self._role_type = None
        self._user_sub_org_and_role_list = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value
    @property
    def org_name(self):
        return self._org_name

    @org_name.setter
    def org_name(self, value):
        self._org_name = value
    @property
    def passport_id(self):
        return self._passport_id

    @passport_id.setter
    def passport_id(self, value):
        self._passport_id = value
    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, value):
        self._role_type = value
    @property
    def user_sub_org_and_role_list(self):
        return self._user_sub_org_and_role_list

    @user_sub_org_and_role_list.setter
    def user_sub_org_and_role_list(self, value):
        if isinstance(value, list):
            self._user_sub_org_and_role_list = list()
            for i in value:
                if isinstance(i, UserSubOrgAndRoleDTO):
                    self._user_sub_org_and_role_list.append(i)
                else:
                    self._user_sub_org_and_role_list.append(UserSubOrgAndRoleDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        if self.org_name:
            if hasattr(self.org_name, 'to_alipay_dict'):
                params['org_name'] = self.org_name.to_alipay_dict()
            else:
                params['org_name'] = self.org_name
        if self.passport_id:
            if hasattr(self.passport_id, 'to_alipay_dict'):
                params['passport_id'] = self.passport_id.to_alipay_dict()
            else:
                params['passport_id'] = self.passport_id
        if self.role_type:
            if hasattr(self.role_type, 'to_alipay_dict'):
                params['role_type'] = self.role_type.to_alipay_dict()
            else:
                params['role_type'] = self.role_type
        if self.user_sub_org_and_role_list:
            if isinstance(self.user_sub_org_and_role_list, list):
                for i in range(0, len(self.user_sub_org_and_role_list)):
                    element = self.user_sub_org_and_role_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_sub_org_and_role_list[i] = element.to_alipay_dict()
            if hasattr(self.user_sub_org_and_role_list, 'to_alipay_dict'):
                params['user_sub_org_and_role_list'] = self.user_sub_org_and_role_list.to_alipay_dict()
            else:
                params['user_sub_org_and_role_list'] = self.user_sub_org_and_role_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserOrgAndRoleDTO()
        if 'id' in d:
            o.id = d['id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        if 'org_name' in d:
            o.org_name = d['org_name']
        if 'passport_id' in d:
            o.passport_id = d['passport_id']
        if 'role_type' in d:
            o.role_type = d['role_type']
        if 'user_sub_org_and_role_list' in d:
            o.user_sub_org_and_role_list = d['user_sub_org_and_role_list']
        return o


