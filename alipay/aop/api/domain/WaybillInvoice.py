#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WaybillInvoice(object):

    def __init__(self):
        self._waybill_amount = None
        self._waybill_no = None

    @property
    def waybill_amount(self):
        return self._waybill_amount

    @waybill_amount.setter
    def waybill_amount(self, value):
        self._waybill_amount = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.waybill_amount:
            if hasattr(self.waybill_amount, 'to_alipay_dict'):
                params['waybill_amount'] = self.waybill_amount.to_alipay_dict()
            else:
                params['waybill_amount'] = self.waybill_amount
        if self.waybill_no:
            if hasattr(self.waybill_no, 'to_alipay_dict'):
                params['waybill_no'] = self.waybill_no.to_alipay_dict()
            else:
                params['waybill_no'] = self.waybill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = WaybillInvoice()
        if 'waybill_amount' in d:
            o.waybill_amount = d['waybill_amount']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


