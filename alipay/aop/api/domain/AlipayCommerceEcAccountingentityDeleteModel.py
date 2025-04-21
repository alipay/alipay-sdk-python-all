#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcAccountingentityDeleteModel(object):

    def __init__(self):
        self._accounting_entity_id = None
        self._enterprise_id = None

    @property
    def accounting_entity_id(self):
        return self._accounting_entity_id

    @accounting_entity_id.setter
    def accounting_entity_id(self, value):
        self._accounting_entity_id = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.accounting_entity_id:
            if hasattr(self.accounting_entity_id, 'to_alipay_dict'):
                params['accounting_entity_id'] = self.accounting_entity_id.to_alipay_dict()
            else:
                params['accounting_entity_id'] = self.accounting_entity_id
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcAccountingentityDeleteModel()
        if 'accounting_entity_id' in d:
            o.accounting_entity_id = d['accounting_entity_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        return o


