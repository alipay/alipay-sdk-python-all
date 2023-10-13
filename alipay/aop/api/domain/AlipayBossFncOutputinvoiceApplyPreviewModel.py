#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiApplyInvoiceOrder import OpenApiApplyInvoiceOrder


class AlipayBossFncOutputinvoiceApplyPreviewModel(object):

    def __init__(self):
        self._open_api_apply_invoice_orders = None

    @property
    def open_api_apply_invoice_orders(self):
        return self._open_api_apply_invoice_orders

    @open_api_apply_invoice_orders.setter
    def open_api_apply_invoice_orders(self, value):
        if isinstance(value, list):
            self._open_api_apply_invoice_orders = list()
            for i in value:
                if isinstance(i, OpenApiApplyInvoiceOrder):
                    self._open_api_apply_invoice_orders.append(i)
                else:
                    self._open_api_apply_invoice_orders.append(OpenApiApplyInvoiceOrder.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.open_api_apply_invoice_orders:
            if isinstance(self.open_api_apply_invoice_orders, list):
                for i in range(0, len(self.open_api_apply_invoice_orders)):
                    element = self.open_api_apply_invoice_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.open_api_apply_invoice_orders[i] = element.to_alipay_dict()
            if hasattr(self.open_api_apply_invoice_orders, 'to_alipay_dict'):
                params['open_api_apply_invoice_orders'] = self.open_api_apply_invoice_orders.to_alipay_dict()
            else:
                params['open_api_apply_invoice_orders'] = self.open_api_apply_invoice_orders
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncOutputinvoiceApplyPreviewModel()
        if 'open_api_apply_invoice_orders' in d:
            o.open_api_apply_invoice_orders = d['open_api_apply_invoice_orders']
        return o


