#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSaasInvoiceDownloadModel(object):

    def __init__(self):
        self._file_type = None
        self._saas_invoice_order_no = None

    @property
    def file_type(self):
        return self._file_type

    @file_type.setter
    def file_type(self, value):
        self._file_type = value
    @property
    def saas_invoice_order_no(self):
        return self._saas_invoice_order_no

    @saas_invoice_order_no.setter
    def saas_invoice_order_no(self, value):
        self._saas_invoice_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_type:
            if hasattr(self.file_type, 'to_alipay_dict'):
                params['file_type'] = self.file_type.to_alipay_dict()
            else:
                params['file_type'] = self.file_type
        if self.saas_invoice_order_no:
            if hasattr(self.saas_invoice_order_no, 'to_alipay_dict'):
                params['saas_invoice_order_no'] = self.saas_invoice_order_no.to_alipay_dict()
            else:
                params['saas_invoice_order_no'] = self.saas_invoice_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasInvoiceDownloadModel()
        if 'file_type' in d:
            o.file_type = d['file_type']
        if 'saas_invoice_order_no' in d:
            o.saas_invoice_order_no = d['saas_invoice_order_no']
        return o


