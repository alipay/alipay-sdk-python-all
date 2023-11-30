#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplierProduceBatch(object):

    def __init__(self):
        self._amount = None
        self._batch_no = None
        self._expire_date = None
        self._produce_code = None
        self._produce_date = None

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
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def produce_code(self):
        return self._produce_code

    @produce_code.setter
    def produce_code(self, value):
        self._produce_code = value
    @property
    def produce_date(self):
        return self._produce_date

    @produce_date.setter
    def produce_date(self, value):
        self._produce_date = value


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
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.produce_code:
            if hasattr(self.produce_code, 'to_alipay_dict'):
                params['produce_code'] = self.produce_code.to_alipay_dict()
            else:
                params['produce_code'] = self.produce_code
        if self.produce_date:
            if hasattr(self.produce_date, 'to_alipay_dict'):
                params['produce_date'] = self.produce_date.to_alipay_dict()
            else:
                params['produce_date'] = self.produce_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplierProduceBatch()
        if 'amount' in d:
            o.amount = d['amount']
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'produce_code' in d:
            o.produce_code = d['produce_code']
        if 'produce_date' in d:
            o.produce_date = d['produce_date']
        return o


