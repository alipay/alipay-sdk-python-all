#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcAccountingentityEmployeeidlistQueryModel(object):

    def __init__(self):
        self._accounting_entity_id = None
        self._enterprise_id = None
        self._page_num = None
        self._page_size = None

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
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


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
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcAccountingentityEmployeeidlistQueryModel()
        if 'accounting_entity_id' in d:
            o.accounting_entity_id = d['accounting_entity_id']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


