#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GovernGoodsMerchantTrans(object):

    def __init__(self):
        self._error_transaction_id = None
        self._manual_trans_count = None
        self._merchant_id = None
        self._sub_merchant_id = None
        self._task_type = None
        self._trans_count = None

    @property
    def error_transaction_id(self):
        return self._error_transaction_id

    @error_transaction_id.setter
    def error_transaction_id(self, value):
        if isinstance(value, list):
            self._error_transaction_id = list()
            for i in value:
                self._error_transaction_id.append(i)
    @property
    def manual_trans_count(self):
        return self._manual_trans_count

    @manual_trans_count.setter
    def manual_trans_count(self, value):
        self._manual_trans_count = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def sub_merchant_id(self):
        return self._sub_merchant_id

    @sub_merchant_id.setter
    def sub_merchant_id(self, value):
        self._sub_merchant_id = value
    @property
    def task_type(self):
        return self._task_type

    @task_type.setter
    def task_type(self, value):
        self._task_type = value
    @property
    def trans_count(self):
        return self._trans_count

    @trans_count.setter
    def trans_count(self, value):
        self._trans_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_transaction_id:
            if isinstance(self.error_transaction_id, list):
                for i in range(0, len(self.error_transaction_id)):
                    element = self.error_transaction_id[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.error_transaction_id[i] = element.to_alipay_dict()
            if hasattr(self.error_transaction_id, 'to_alipay_dict'):
                params['error_transaction_id'] = self.error_transaction_id.to_alipay_dict()
            else:
                params['error_transaction_id'] = self.error_transaction_id
        if self.manual_trans_count:
            if hasattr(self.manual_trans_count, 'to_alipay_dict'):
                params['manual_trans_count'] = self.manual_trans_count.to_alipay_dict()
            else:
                params['manual_trans_count'] = self.manual_trans_count
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.sub_merchant_id:
            if hasattr(self.sub_merchant_id, 'to_alipay_dict'):
                params['sub_merchant_id'] = self.sub_merchant_id.to_alipay_dict()
            else:
                params['sub_merchant_id'] = self.sub_merchant_id
        if self.task_type:
            if hasattr(self.task_type, 'to_alipay_dict'):
                params['task_type'] = self.task_type.to_alipay_dict()
            else:
                params['task_type'] = self.task_type
        if self.trans_count:
            if hasattr(self.trans_count, 'to_alipay_dict'):
                params['trans_count'] = self.trans_count.to_alipay_dict()
            else:
                params['trans_count'] = self.trans_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GovernGoodsMerchantTrans()
        if 'error_transaction_id' in d:
            o.error_transaction_id = d['error_transaction_id']
        if 'manual_trans_count' in d:
            o.manual_trans_count = d['manual_trans_count']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'sub_merchant_id' in d:
            o.sub_merchant_id = d['sub_merchant_id']
        if 'task_type' in d:
            o.task_type = d['task_type']
        if 'trans_count' in d:
            o.trans_count = d['trans_count']
        return o


