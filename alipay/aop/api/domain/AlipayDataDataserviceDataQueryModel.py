#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HelloHq import HelloHq


class AlipayDataDataserviceDataQueryModel(object):

    def __init__(self):
        self._hello_hq = None
        self._order_no = None

    @property
    def hello_hq(self):
        return self._hello_hq

    @hello_hq.setter
    def hello_hq(self, value):
        if isinstance(value, HelloHq):
            self._hello_hq = value
        else:
            self._hello_hq = HelloHq.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.hello_hq:
            if hasattr(self.hello_hq, 'to_alipay_dict'):
                params['hello_hq'] = self.hello_hq.to_alipay_dict()
            else:
                params['hello_hq'] = self.hello_hq
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
        o = AlipayDataDataserviceDataQueryModel()
        if 'hello_hq' in d:
            o.hello_hq = d['hello_hq']
        if 'order_no' in d:
            o.order_no = d['order_no']
        return o


