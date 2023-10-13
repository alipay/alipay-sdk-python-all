#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiOutputInvoicePreviewedOrder import OpenApiOutputInvoicePreviewedOrder


class AlipayBossFncOutputinvoiceApplyModifyModel(object):

    def __init__(self):
        self._operator = None
        self._output_invoice_previewed_orders = None
        self._preview_order_id = None

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def output_invoice_previewed_orders(self):
        return self._output_invoice_previewed_orders

    @output_invoice_previewed_orders.setter
    def output_invoice_previewed_orders(self, value):
        if isinstance(value, list):
            self._output_invoice_previewed_orders = list()
            for i in value:
                if isinstance(i, OpenApiOutputInvoicePreviewedOrder):
                    self._output_invoice_previewed_orders.append(i)
                else:
                    self._output_invoice_previewed_orders.append(OpenApiOutputInvoicePreviewedOrder.from_alipay_dict(i))
    @property
    def preview_order_id(self):
        return self._preview_order_id

    @preview_order_id.setter
    def preview_order_id(self, value):
        self._preview_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.output_invoice_previewed_orders:
            if isinstance(self.output_invoice_previewed_orders, list):
                for i in range(0, len(self.output_invoice_previewed_orders)):
                    element = self.output_invoice_previewed_orders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.output_invoice_previewed_orders[i] = element.to_alipay_dict()
            if hasattr(self.output_invoice_previewed_orders, 'to_alipay_dict'):
                params['output_invoice_previewed_orders'] = self.output_invoice_previewed_orders.to_alipay_dict()
            else:
                params['output_invoice_previewed_orders'] = self.output_invoice_previewed_orders
        if self.preview_order_id:
            if hasattr(self.preview_order_id, 'to_alipay_dict'):
                params['preview_order_id'] = self.preview_order_id.to_alipay_dict()
            else:
                params['preview_order_id'] = self.preview_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncOutputinvoiceApplyModifyModel()
        if 'operator' in d:
            o.operator = d['operator']
        if 'output_invoice_previewed_orders' in d:
            o.output_invoice_previewed_orders = d['output_invoice_previewed_orders']
        if 'preview_order_id' in d:
            o.preview_order_id = d['preview_order_id']
        return o


