#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTaxAdvancedUnfreezeModel(object):

    def __init__(self):
        self._tax_refund_no = None

    @property
    def tax_refund_no(self):
        return self._tax_refund_no

    @tax_refund_no.setter
    def tax_refund_no(self, value):
        self._tax_refund_no = value


    def to_alipay_dict(self):
        params = dict()
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
        o = AlipayOverseasTaxAdvancedUnfreezeModel()
        if 'tax_refund_no' in d:
            o.tax_refund_no = d['tax_refund_no']
        return o


