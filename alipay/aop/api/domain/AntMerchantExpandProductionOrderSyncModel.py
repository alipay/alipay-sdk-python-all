#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandProductionOrderSyncModel(object):

    def __init__(self):
        self._amount = None
        self._batch_no = None
        self._item_id = None
        self._project_no = None
        self._regional_warehouse = None
        self._value = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def project_no(self):
        return self._project_no

    @project_no.setter
    def project_no(self, value):
        self._project_no = value
    @property
    def regional_warehouse(self):
        return self._regional_warehouse

    @regional_warehouse.setter
    def regional_warehouse(self, value):
        self._regional_warehouse = value
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.project_no:
            if hasattr(self.project_no, 'to_alipay_dict'):
                params['project_no'] = self.project_no.to_alipay_dict()
            else:
                params['project_no'] = self.project_no
        if self.regional_warehouse:
            if hasattr(self.regional_warehouse, 'to_alipay_dict'):
                params['regional_warehouse'] = self.regional_warehouse.to_alipay_dict()
            else:
                params['regional_warehouse'] = self.regional_warehouse
        if self.value:
            if hasattr(self.value, 'to_alipay_dict'):
                params['value'] = self.value.to_alipay_dict()
            else:
                params['value'] = self.value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantExpandProductionOrderSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'project_no' in d:
            o.project_no = d['project_no']
        if 'regional_warehouse' in d:
            o.regional_warehouse = d['regional_warehouse']
        if 'value' in d:
            o.value = d['value']
        return o


