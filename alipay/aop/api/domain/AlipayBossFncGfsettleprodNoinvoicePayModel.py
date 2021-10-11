#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NoInvoicePayOrder import NoInvoicePayOrder


class AlipayBossFncGfsettleprodNoinvoicePayModel(object):

    def __init__(self):
        self._no_invoice_pay_order = None

    @property
    def no_invoice_pay_order(self):
        return self._no_invoice_pay_order

    @no_invoice_pay_order.setter
    def no_invoice_pay_order(self, value):
        if isinstance(value, NoInvoicePayOrder):
            self._no_invoice_pay_order = value
        else:
            self._no_invoice_pay_order = NoInvoicePayOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.no_invoice_pay_order:
            if hasattr(self.no_invoice_pay_order, 'to_alipay_dict'):
                params['no_invoice_pay_order'] = self.no_invoice_pay_order.to_alipay_dict()
            else:
                params['no_invoice_pay_order'] = self.no_invoice_pay_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodNoinvoicePayModel()
        if 'no_invoice_pay_order' in d:
            o.no_invoice_pay_order = d['no_invoice_pay_order']
        return o


