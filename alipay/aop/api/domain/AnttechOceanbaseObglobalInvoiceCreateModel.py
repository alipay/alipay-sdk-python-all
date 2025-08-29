#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FxiaokeCreateInvoiceRequest import FxiaokeCreateInvoiceRequest


class AnttechOceanbaseObglobalInvoiceCreateModel(object):

    def __init__(self):
        self._fxiaoke_create_invoice_request = None

    @property
    def fxiaoke_create_invoice_request(self):
        return self._fxiaoke_create_invoice_request

    @fxiaoke_create_invoice_request.setter
    def fxiaoke_create_invoice_request(self, value):
        if isinstance(value, FxiaokeCreateInvoiceRequest):
            self._fxiaoke_create_invoice_request = value
        else:
            self._fxiaoke_create_invoice_request = FxiaokeCreateInvoiceRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.fxiaoke_create_invoice_request:
            if hasattr(self.fxiaoke_create_invoice_request, 'to_alipay_dict'):
                params['fxiaoke_create_invoice_request'] = self.fxiaoke_create_invoice_request.to_alipay_dict()
            else:
                params['fxiaoke_create_invoice_request'] = self.fxiaoke_create_invoice_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalInvoiceCreateModel()
        if 'fxiaoke_create_invoice_request' in d:
            o.fxiaoke_create_invoice_request = d['fxiaoke_create_invoice_request']
        return o


