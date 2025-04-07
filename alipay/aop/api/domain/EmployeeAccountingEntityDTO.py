#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EmployeeAccountingEntityDTO(object):

    def __init__(self):
        self._accounting_entity_code = None
        self._accounting_entity_id = None
        self._accounting_entity_name = None

    @property
    def accounting_entity_code(self):
        return self._accounting_entity_code

    @accounting_entity_code.setter
    def accounting_entity_code(self, value):
        self._accounting_entity_code = value
    @property
    def accounting_entity_id(self):
        return self._accounting_entity_id

    @accounting_entity_id.setter
    def accounting_entity_id(self, value):
        self._accounting_entity_id = value
    @property
    def accounting_entity_name(self):
        return self._accounting_entity_name

    @accounting_entity_name.setter
    def accounting_entity_name(self, value):
        self._accounting_entity_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.accounting_entity_code:
            if hasattr(self.accounting_entity_code, 'to_alipay_dict'):
                params['accounting_entity_code'] = self.accounting_entity_code.to_alipay_dict()
            else:
                params['accounting_entity_code'] = self.accounting_entity_code
        if self.accounting_entity_id:
            if hasattr(self.accounting_entity_id, 'to_alipay_dict'):
                params['accounting_entity_id'] = self.accounting_entity_id.to_alipay_dict()
            else:
                params['accounting_entity_id'] = self.accounting_entity_id
        if self.accounting_entity_name:
            if hasattr(self.accounting_entity_name, 'to_alipay_dict'):
                params['accounting_entity_name'] = self.accounting_entity_name.to_alipay_dict()
            else:
                params['accounting_entity_name'] = self.accounting_entity_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EmployeeAccountingEntityDTO()
        if 'accounting_entity_code' in d:
            o.accounting_entity_code = d['accounting_entity_code']
        if 'accounting_entity_id' in d:
            o.accounting_entity_id = d['accounting_entity_id']
        if 'accounting_entity_name' in d:
            o.accounting_entity_name = d['accounting_entity_name']
        return o


