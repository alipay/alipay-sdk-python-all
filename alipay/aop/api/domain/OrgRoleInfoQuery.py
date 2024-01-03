#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrgRoleInfoQuery(object):

    def __init__(self):
        self._node_types = None
        self._role_codes = None

    @property
    def node_types(self):
        return self._node_types

    @node_types.setter
    def node_types(self, value):
        if isinstance(value, list):
            self._node_types = list()
            for i in value:
                self._node_types.append(i)
    @property
    def role_codes(self):
        return self._role_codes

    @role_codes.setter
    def role_codes(self, value):
        if isinstance(value, list):
            self._role_codes = list()
            for i in value:
                self._role_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.node_types:
            if isinstance(self.node_types, list):
                for i in range(0, len(self.node_types)):
                    element = self.node_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.node_types[i] = element.to_alipay_dict()
            if hasattr(self.node_types, 'to_alipay_dict'):
                params['node_types'] = self.node_types.to_alipay_dict()
            else:
                params['node_types'] = self.node_types
        if self.role_codes:
            if isinstance(self.role_codes, list):
                for i in range(0, len(self.role_codes)):
                    element = self.role_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.role_codes[i] = element.to_alipay_dict()
            if hasattr(self.role_codes, 'to_alipay_dict'):
                params['role_codes'] = self.role_codes.to_alipay_dict()
            else:
                params['role_codes'] = self.role_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrgRoleInfoQuery()
        if 'node_types' in d:
            o.node_types = d['node_types']
        if 'role_codes' in d:
            o.role_codes = d['role_codes']
        return o


