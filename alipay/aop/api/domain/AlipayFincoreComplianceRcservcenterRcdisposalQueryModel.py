#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreComplianceRcservcenterRcdisposalQueryModel(object):

    def __init__(self):
        self._demand_code = None
        self._entity_id = None

    @property
    def demand_code(self):
        return self._demand_code

    @demand_code.setter
    def demand_code(self, value):
        self._demand_code = value
    @property
    def entity_id(self):
        return self._entity_id

    @entity_id.setter
    def entity_id(self, value):
        self._entity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.demand_code:
            if hasattr(self.demand_code, 'to_alipay_dict'):
                params['demand_code'] = self.demand_code.to_alipay_dict()
            else:
                params['demand_code'] = self.demand_code
        if self.entity_id:
            if hasattr(self.entity_id, 'to_alipay_dict'):
                params['entity_id'] = self.entity_id.to_alipay_dict()
            else:
                params['entity_id'] = self.entity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreComplianceRcservcenterRcdisposalQueryModel()
        if 'demand_code' in d:
            o.demand_code = d['demand_code']
        if 'entity_id' in d:
            o.entity_id = d['entity_id']
        return o


