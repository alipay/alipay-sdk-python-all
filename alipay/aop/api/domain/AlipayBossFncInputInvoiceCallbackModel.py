#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputInvoiceCallbackOpenApiOrder import InputInvoiceCallbackOpenApiOrder


class AlipayBossFncInputInvoiceCallbackModel(object):

    def __init__(self):
        self._input_invoice_callback_open_api_order = None

    @property
    def input_invoice_callback_open_api_order(self):
        return self._input_invoice_callback_open_api_order

    @input_invoice_callback_open_api_order.setter
    def input_invoice_callback_open_api_order(self, value):
        if isinstance(value, InputInvoiceCallbackOpenApiOrder):
            self._input_invoice_callback_open_api_order = value
        else:
            self._input_invoice_callback_open_api_order = InputInvoiceCallbackOpenApiOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.input_invoice_callback_open_api_order:
            if hasattr(self.input_invoice_callback_open_api_order, 'to_alipay_dict'):
                params['input_invoice_callback_open_api_order'] = self.input_invoice_callback_open_api_order.to_alipay_dict()
            else:
                params['input_invoice_callback_open_api_order'] = self.input_invoice_callback_open_api_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInputInvoiceCallbackModel()
        if 'input_invoice_callback_open_api_order' in d:
            o.input_invoice_callback_open_api_order = d['input_invoice_callback_open_api_order']
        return o


