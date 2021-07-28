#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxAdvancedStatusQueryModel(object):

    def __init__(self):
        self._out_tax_refund_no = None

    @property
    def out_tax_refund_no(self):
        return self._out_tax_refund_no

    @out_tax_refund_no.setter
    def out_tax_refund_no(self, value):
        self._out_tax_refund_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_tax_refund_no:
            if hasattr(self.out_tax_refund_no, 'to_alipay_dict'):
                params['out_tax_refund_no'] = self.out_tax_refund_no.to_alipay_dict()
            else:
                params['out_tax_refund_no'] = self.out_tax_refund_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTaxAdvancedStatusQueryModel()
        if 'out_tax_refund_no' in d:
            o.out_tax_refund_no = d['out_tax_refund_no']
        return o


