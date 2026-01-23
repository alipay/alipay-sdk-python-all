#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpInteopOrderConfirmModel(object):

    def __init__(self):
        self._async_submit = None
        self._inteop_order_no = None

    @property
    def async_submit(self):
        return self._async_submit

    @async_submit.setter
    def async_submit(self, value):
        self._async_submit = value
    @property
    def inteop_order_no(self):
        return self._inteop_order_no

    @inteop_order_no.setter
    def inteop_order_no(self, value):
        self._inteop_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.async_submit:
            if hasattr(self.async_submit, 'to_alipay_dict'):
                params['async_submit'] = self.async_submit.to_alipay_dict()
            else:
                params['async_submit'] = self.async_submit
        if self.inteop_order_no:
            if hasattr(self.inteop_order_no, 'to_alipay_dict'):
                params['inteop_order_no'] = self.inteop_order_no.to_alipay_dict()
            else:
                params['inteop_order_no'] = self.inteop_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpInteopOrderConfirmModel()
        if 'async_submit' in d:
            o.async_submit = d['async_submit']
        if 'inteop_order_no' in d:
            o.inteop_order_no = d['inteop_order_no']
        return o


