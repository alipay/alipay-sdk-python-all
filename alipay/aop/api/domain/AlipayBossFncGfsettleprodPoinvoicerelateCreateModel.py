#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InputInvoiceOrderRequest import InputInvoiceOrderRequest


class AlipayBossFncGfsettleprodPoinvoicerelateCreateModel(object):

    def __init__(self):
        self._input_invoice_order_request = None

    @property
    def input_invoice_order_request(self):
        return self._input_invoice_order_request

    @input_invoice_order_request.setter
    def input_invoice_order_request(self, value):
        if isinstance(value, InputInvoiceOrderRequest):
            self._input_invoice_order_request = value
        else:
            self._input_invoice_order_request = InputInvoiceOrderRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.input_invoice_order_request:
            if hasattr(self.input_invoice_order_request, 'to_alipay_dict'):
                params['input_invoice_order_request'] = self.input_invoice_order_request.to_alipay_dict()
            else:
                params['input_invoice_order_request'] = self.input_invoice_order_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodPoinvoicerelateCreateModel()
        if 'input_invoice_order_request' in d:
            o.input_invoice_order_request = d['input_invoice_order_request']
        return o


