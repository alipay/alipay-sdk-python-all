#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMembersCreateModel(object):

    def __init__(self):
        self._logon_id = None
        self._role = None

    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


    def to_alipay_dict(self):
        params = dict()
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.role:
            if hasattr(self.role, 'to_alipay_dict'):
                params['role'] = self.role.to_alipay_dict()
            else:
                params['role'] = self.role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppMembersCreateModel()
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'role' in d:
            o.role = d['role']
        return o


