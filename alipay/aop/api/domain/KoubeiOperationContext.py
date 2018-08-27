#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiOperationContext(object):

    def __init__(self):
        self._op_role = None

    @property
    def op_role(self):
        return self._op_role

    @op_role.setter
    def op_role(self, value):
        self._op_role = value


    def to_alipay_dict(self):
        params = dict()
        if self.op_role:
            if hasattr(self.op_role, 'to_alipay_dict'):
                params['op_role'] = self.op_role.to_alipay_dict()
            else:
                params['op_role'] = self.op_role
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiOperationContext()
        if 'op_role' in d:
            o.op_role = d['op_role']
        return o


