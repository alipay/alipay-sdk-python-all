#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayItemOperationContext(object):

    def __init__(self):
        self._creator = None
        self._op_role = None
        self._partner_id = None

    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def op_role(self):
        return self._op_role

    @op_role.setter
    def op_role(self, value):
        self._op_role = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.op_role:
            if hasattr(self.op_role, 'to_alipay_dict'):
                params['op_role'] = self.op_role.to_alipay_dict()
            else:
                params['op_role'] = self.op_role
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayItemOperationContext()
        if 'creator' in d:
            o.creator = d['creator']
        if 'op_role' in d:
            o.op_role = d['op_role']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


