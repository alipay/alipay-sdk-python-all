#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemDeliveryDetail(object):

    def __init__(self):
        self._amount = None
        self._assign_item_id = None
        self._batch_no = None
        self._logistic_code = None
        self._logistics_name = None
        self._logistics_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assign_item_id(self):
        return self._assign_item_id

    @assign_item_id.setter
    def assign_item_id(self, value):
        self._assign_item_id = value
    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def logistic_code(self):
        return self._logistic_code

    @logistic_code.setter
    def logistic_code(self, value):
        self._logistic_code = value
    @property
    def logistics_name(self):
        return self._logistics_name

    @logistics_name.setter
    def logistics_name(self, value):
        self._logistics_name = value
    @property
    def logistics_no(self):
        return self._logistics_no

    @logistics_no.setter
    def logistics_no(self, value):
        self._logistics_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assign_item_id:
            if hasattr(self.assign_item_id, 'to_alipay_dict'):
                params['assign_item_id'] = self.assign_item_id.to_alipay_dict()
            else:
                params['assign_item_id'] = self.assign_item_id
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.logistic_code:
            if hasattr(self.logistic_code, 'to_alipay_dict'):
                params['logistic_code'] = self.logistic_code.to_alipay_dict()
            else:
                params['logistic_code'] = self.logistic_code
        if self.logistics_name:
            if hasattr(self.logistics_name, 'to_alipay_dict'):
                params['logistics_name'] = self.logistics_name.to_alipay_dict()
            else:
                params['logistics_name'] = self.logistics_name
        if self.logistics_no:
            if hasattr(self.logistics_no, 'to_alipay_dict'):
                params['logistics_no'] = self.logistics_no.to_alipay_dict()
            else:
                params['logistics_no'] = self.logistics_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemDeliveryDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assign_item_id' in d:
            o.assign_item_id = d['assign_item_id']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'logistic_code' in d:
            o.logistic_code = d['logistic_code']
        if 'logistics_name' in d:
            o.logistics_name = d['logistics_name']
        if 'logistics_no' in d:
            o.logistics_no = d['logistics_no']
        return o


