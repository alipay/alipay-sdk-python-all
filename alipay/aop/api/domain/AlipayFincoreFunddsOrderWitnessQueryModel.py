#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayFincoreFunddsOrderWitnessQueryModel(object):

    def __init__(self):
        self._fds_no = None
        self._product_code = None

    @property
    def fds_no(self):
        return self._fds_no

    @fds_no.setter
    def fds_no(self, value):
        self._fds_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.fds_no:
            if hasattr(self.fds_no, 'to_alipay_dict'):
                params['fds_no'] = self.fds_no.to_alipay_dict()
            else:
                params['fds_no'] = self.fds_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayFincoreFunddsOrderWitnessQueryModel()
        if 'fds_no' in d:
            o.fds_no = d['fds_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


