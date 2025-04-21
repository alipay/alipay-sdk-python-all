#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateManagerDetailQueryModel(object):

    def __init__(self):
        self._inst_id = None
        self._manager_id = None

    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def manager_id(self):
        return self._manager_id

    @manager_id.setter
    def manager_id(self, value):
        self._manager_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.manager_id:
            if hasattr(self.manager_id, 'to_alipay_dict'):
                params['manager_id'] = self.manager_id.to_alipay_dict()
            else:
                params['manager_id'] = self.manager_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateManagerDetailQueryModel()
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'manager_id' in d:
            o.manager_id = d['manager_id']
        return o


