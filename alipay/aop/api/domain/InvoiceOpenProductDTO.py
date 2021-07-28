#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceOpenProductDTO(object):

    def __init__(self):
        self._invoice_kind = None
        self._isv_code = None
        self._product_code = None
        self._serv_end_time = None
        self._serv_start_time = None

    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def isv_code(self):
        return self._isv_code

    @isv_code.setter
    def isv_code(self, value):
        self._isv_code = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def serv_end_time(self):
        return self._serv_end_time

    @serv_end_time.setter
    def serv_end_time(self, value):
        self._serv_end_time = value
    @property
    def serv_start_time(self):
        return self._serv_start_time

    @serv_start_time.setter
    def serv_start_time(self, value):
        self._serv_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.isv_code:
            if hasattr(self.isv_code, 'to_alipay_dict'):
                params['isv_code'] = self.isv_code.to_alipay_dict()
            else:
                params['isv_code'] = self.isv_code
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.serv_end_time:
            if hasattr(self.serv_end_time, 'to_alipay_dict'):
                params['serv_end_time'] = self.serv_end_time.to_alipay_dict()
            else:
                params['serv_end_time'] = self.serv_end_time
        if self.serv_start_time:
            if hasattr(self.serv_start_time, 'to_alipay_dict'):
                params['serv_start_time'] = self.serv_start_time.to_alipay_dict()
            else:
                params['serv_start_time'] = self.serv_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceOpenProductDTO()
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'isv_code' in d:
            o.isv_code = d['isv_code']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'serv_end_time' in d:
            o.serv_end_time = d['serv_end_time']
        if 'serv_start_time' in d:
            o.serv_start_time = d['serv_start_time']
        return o


