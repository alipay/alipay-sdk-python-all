#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantSolcreditserviceprodDeductionorderQueryModel(object):

    def __init__(self):
        self._deduction_order_no = None
        self._order_no = None

    @property
    def deduction_order_no(self):
        return self._deduction_order_no

    @deduction_order_no.setter
    def deduction_order_no(self, value):
        self._deduction_order_no = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.deduction_order_no:
            if hasattr(self.deduction_order_no, 'to_alipay_dict'):
                params['deduction_order_no'] = self.deduction_order_no.to_alipay_dict()
            else:
                params['deduction_order_no'] = self.deduction_order_no
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantSolcreditserviceprodDeductionorderQueryModel()
        if 'deduction_order_no' in d:
            o.deduction_order_no = d['deduction_order_no']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


