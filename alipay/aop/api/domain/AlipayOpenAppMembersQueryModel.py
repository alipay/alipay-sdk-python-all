#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppMembersQueryModel(object):

    def __init__(self):
        self._role = None

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayOpenAppMembersQueryModel()
        if 'role' in d:
            o.role = d['role']
        return o


