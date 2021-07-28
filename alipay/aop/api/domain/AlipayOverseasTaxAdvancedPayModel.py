#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxAdvancedPayModel(object):

    def __init__(self):
        self._out_request_no = None
        self._tax_refund_no = None

    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def tax_refund_no(self):
        return self._tax_refund_no

    @tax_refund_no.setter
    def tax_refund_no(self, value):
        self._tax_refund_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.tax_refund_no:
            if hasattr(self.tax_refund_no, 'to_alipay_dict'):
                params['tax_refund_no'] = self.tax_refund_no.to_alipay_dict()
            else:
                params['tax_refund_no'] = self.tax_refund_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTaxAdvancedPayModel()
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'tax_refund_no' in d:
            o.tax_refund_no = d['tax_refund_no']
        return o


