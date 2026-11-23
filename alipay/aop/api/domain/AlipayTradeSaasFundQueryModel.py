#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSaasFundQueryModel(object):

    def __init__(self):
        self._customer_id = None
        self._fund_no = None

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def fund_no(self):
        return self._fund_no

    @fund_no.setter
    def fund_no(self, value):
        self._fund_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.fund_no:
            if hasattr(self.fund_no, 'to_alipay_dict'):
                params['fund_no'] = self.fund_no.to_alipay_dict()
            else:
                params['fund_no'] = self.fund_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasFundQueryModel()
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'fund_no' in d:
            o.fund_no = d['fund_no']
        return o


