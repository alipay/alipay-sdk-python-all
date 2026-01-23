#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalAgentInfoQueryModel(object):

    def __init__(self):
        self._config_order_id = None
        self._org_id = None

    @property
    def config_order_id(self):
        return self._config_order_id

    @config_order_id.setter
    def config_order_id(self, value):
        self._config_order_id = value
    @property
    def org_id(self):
        return self._org_id

    @org_id.setter
    def org_id(self, value):
        self._org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.config_order_id:
            if hasattr(self.config_order_id, 'to_alipay_dict'):
                params['config_order_id'] = self.config_order_id.to_alipay_dict()
            else:
                params['config_order_id'] = self.config_order_id
        if self.org_id:
            if hasattr(self.org_id, 'to_alipay_dict'):
                params['org_id'] = self.org_id.to_alipay_dict()
            else:
                params['org_id'] = self.org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalAgentInfoQueryModel()
        if 'config_order_id' in d:
            o.config_order_id = d['config_order_id']
        if 'org_id' in d:
            o.org_id = d['org_id']
        return o


