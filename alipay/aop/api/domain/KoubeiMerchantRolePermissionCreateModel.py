#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BusinessPermission import BusinessPermission
from alipay.aop.api.domain.BusinessPermission import BusinessPermission


class KoubeiMerchantRolePermissionCreateModel(object):

    def __init__(self):
        self._auth_code = None
        self._permissions_to_add = None
        self._permissions_to_delete = None
        self._principal_id = None
        self._principal_type = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def permissions_to_add(self):
        return self._permissions_to_add

    @permissions_to_add.setter
    def permissions_to_add(self, value):
        if isinstance(value, list):
            self._permissions_to_add = list()
            for i in value:
                if isinstance(i, BusinessPermission):
                    self._permissions_to_add.append(i)
                else:
                    self._permissions_to_add.append(BusinessPermission.from_alipay_dict(i))
    @property
    def permissions_to_delete(self):
        return self._permissions_to_delete

    @permissions_to_delete.setter
    def permissions_to_delete(self, value):
        if isinstance(value, list):
            self._permissions_to_delete = list()
            for i in value:
                if isinstance(i, BusinessPermission):
                    self._permissions_to_delete.append(i)
                else:
                    self._permissions_to_delete.append(BusinessPermission.from_alipay_dict(i))
    @property
    def principal_id(self):
        return self._principal_id

    @principal_id.setter
    def principal_id(self, value):
        self._principal_id = value
    @property
    def principal_type(self):
        return self._principal_type

    @principal_type.setter
    def principal_type(self, value):
        self._principal_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.permissions_to_add:
            if isinstance(self.permissions_to_add, list):
                for i in range(0, len(self.permissions_to_add)):
                    element = self.permissions_to_add[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.permissions_to_add[i] = element.to_alipay_dict()
            if hasattr(self.permissions_to_add, 'to_alipay_dict'):
                params['permissions_to_add'] = self.permissions_to_add.to_alipay_dict()
            else:
                params['permissions_to_add'] = self.permissions_to_add
        if self.permissions_to_delete:
            if isinstance(self.permissions_to_delete, list):
                for i in range(0, len(self.permissions_to_delete)):
                    element = self.permissions_to_delete[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.permissions_to_delete[i] = element.to_alipay_dict()
            if hasattr(self.permissions_to_delete, 'to_alipay_dict'):
                params['permissions_to_delete'] = self.permissions_to_delete.to_alipay_dict()
            else:
                params['permissions_to_delete'] = self.permissions_to_delete
        if self.principal_id:
            if hasattr(self.principal_id, 'to_alipay_dict'):
                params['principal_id'] = self.principal_id.to_alipay_dict()
            else:
                params['principal_id'] = self.principal_id
        if self.principal_type:
            if hasattr(self.principal_type, 'to_alipay_dict'):
                params['principal_type'] = self.principal_type.to_alipay_dict()
            else:
                params['principal_type'] = self.principal_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiMerchantRolePermissionCreateModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'permissions_to_add' in d:
            o.permissions_to_add = d['permissions_to_add']
        if 'permissions_to_delete' in d:
            o.permissions_to_delete = d['permissions_to_delete']
        if 'principal_id' in d:
            o.principal_id = d['principal_id']
        if 'principal_type' in d:
            o.principal_type = d['principal_type']
        return o


