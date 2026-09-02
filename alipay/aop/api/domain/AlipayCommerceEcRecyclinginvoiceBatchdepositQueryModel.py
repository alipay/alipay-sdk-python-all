#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceBatchdepositQueryModel(object):

    def __init__(self):
        self._batch_deposit_id = None
        self._tax_no = None

    @property
    def batch_deposit_id(self):
        return self._batch_deposit_id

    @batch_deposit_id.setter
    def batch_deposit_id(self, value):
        self._batch_deposit_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_deposit_id:
            if hasattr(self.batch_deposit_id, 'to_alipay_dict'):
                params['batch_deposit_id'] = self.batch_deposit_id.to_alipay_dict()
            else:
                params['batch_deposit_id'] = self.batch_deposit_id
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceBatchdepositQueryModel()
        if 'batch_deposit_id' in d:
            o.batch_deposit_id = d['batch_deposit_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


