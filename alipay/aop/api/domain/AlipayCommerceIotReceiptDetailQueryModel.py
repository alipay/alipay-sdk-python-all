#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotReceiptDetailQueryModel(object):

    def __init__(self):
        self._receipt_id = None

    @property
    def receipt_id(self):
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, value):
        self._receipt_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.receipt_id:
            if hasattr(self.receipt_id, 'to_alipay_dict'):
                params['receipt_id'] = self.receipt_id.to_alipay_dict()
            else:
                params['receipt_id'] = self.receipt_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotReceiptDetailQueryModel()
        if 'receipt_id' in d:
            o.receipt_id = d['receipt_id']
        return o


