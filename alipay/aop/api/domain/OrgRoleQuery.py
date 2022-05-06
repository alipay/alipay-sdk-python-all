#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrgRoleQuery(object):

    def __init__(self):
        self._node_code = None
        self._node_type = None
        self._role = None
        self._tnt_inst_id = None

    @property
    def node_code(self):
        return self._node_code

    @node_code.setter
    def node_code(self, value):
        self._node_code = value
    @property
    def node_type(self):
        return self._node_type

    @node_type.setter
    def node_type(self, value):
        self._node_type = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.node_code:
            if hasattr(self.node_code, 'to_alipay_dict'):
                params['node_code'] = self.node_code.to_alipay_dict()
            else:
                params['node_code'] = self.node_code
        if self.node_type:
            if hasattr(self.node_type, 'to_alipay_dict'):
                params['node_type'] = self.node_type.to_alipay_dict()
            else:
                params['node_type'] = self.node_type
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrgRoleQuery()
        if 'node_code' in d:
            o.node_code = d['node_code']
        if 'node_type' in d:
            o.node_type = d['node_type']
        if 'role' in d:
            o.role = d['role']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


