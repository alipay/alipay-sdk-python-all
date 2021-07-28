#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class WaybillInvoiceQueryIstd(object):

    def __init__(self):
        self._reason = None
        self._shop_no = None
        self._waybill_amount = None
        self._waybill_invoice_status = None
        self._waybill_no = None

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value
    @property
    def shop_no(self):
        return self._shop_no

    @shop_no.setter
    def shop_no(self, value):
        self._shop_no = value
    @property
    def waybill_amount(self):
        return self._waybill_amount

    @waybill_amount.setter
    def waybill_amount(self, value):
        self._waybill_amount = value
    @property
    def waybill_invoice_status(self):
        return self._waybill_invoice_status

    @waybill_invoice_status.setter
    def waybill_invoice_status(self, value):
        self._waybill_invoice_status = value
    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, value):
        self._waybill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        if self.shop_no:
            if hasattr(self.shop_no, 'to_alipay_dict'):
                params['shop_no'] = self.shop_no.to_alipay_dict()
            else:
                params['shop_no'] = self.shop_no
        if self.waybill_amount:
            if hasattr(self.waybill_amount, 'to_alipay_dict'):
                params['waybill_amount'] = self.waybill_amount.to_alipay_dict()
            else:
                params['waybill_amount'] = self.waybill_amount
        if self.waybill_invoice_status:
            if hasattr(self.waybill_invoice_status, 'to_alipay_dict'):
                params['waybill_invoice_status'] = self.waybill_invoice_status.to_alipay_dict()
            else:
                params['waybill_invoice_status'] = self.waybill_invoice_status
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
        o = WaybillInvoiceQueryIstd()
        if 'reason' in d:
            o.reason = d['reason']
        if 'shop_no' in d:
            o.shop_no = d['shop_no']
        if 'waybill_amount' in d:
            o.waybill_amount = d['waybill_amount']
        if 'waybill_invoice_status' in d:
            o.waybill_invoice_status = d['waybill_invoice_status']
        if 'waybill_no' in d:
            o.waybill_no = d['waybill_no']
        return o


