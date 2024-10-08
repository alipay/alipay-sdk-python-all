#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BizSalaryOrder(object):

    def __init__(self):
        self._biz_order_no = None
        self._employer_name = None

    @property
    def biz_order_no(self):
        return self._biz_order_no

    @biz_order_no.setter
    def biz_order_no(self, value):
        self._biz_order_no = value
    @property
    def employer_name(self):
        return self._employer_name

    @employer_name.setter
    def employer_name(self, value):
        self._employer_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_order_no:
            if hasattr(self.biz_order_no, 'to_alipay_dict'):
                params['biz_order_no'] = self.biz_order_no.to_alipay_dict()
            else:
                params['biz_order_no'] = self.biz_order_no
        if self.employer_name:
            if hasattr(self.employer_name, 'to_alipay_dict'):
                params['employer_name'] = self.employer_name.to_alipay_dict()
            else:
                params['employer_name'] = self.employer_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BizSalaryOrder()
        if 'biz_order_no' in d:
            o.biz_order_no = d['biz_order_no']
        if 'employer_name' in d:
            o.employer_name = d['employer_name']
        return o


