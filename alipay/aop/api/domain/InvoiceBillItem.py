#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceBillItem(object):

    def __init__(self):
        self._invoice_mode = None
        self._out_biz_no = None
        self._out_biz_type = None

    @property
    def invoice_mode(self):
        return self._invoice_mode

    @invoice_mode.setter
    def invoice_mode(self, value):
        self._invoice_mode = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.invoice_mode:
            if hasattr(self.invoice_mode, 'to_alipay_dict'):
                params['invoice_mode'] = self.invoice_mode.to_alipay_dict()
            else:
                params['invoice_mode'] = self.invoice_mode
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceBillItem()
        if 'invoice_mode' in d:
            o.invoice_mode = d['invoice_mode']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        return o


