#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FQExtendParams(object):

    def __init__(self):
        self._fq_number = None
        self._fq_seller_percent = None

    @property
    def fq_number(self):
        return self._fq_number

    @fq_number.setter
    def fq_number(self, value):
        self._fq_number = value
    @property
    def fq_seller_percent(self):
        return self._fq_seller_percent

    @fq_seller_percent.setter
    def fq_seller_percent(self, value):
        self._fq_seller_percent = value


    def to_alipay_dict(self):
        params = dict()
        if self.fq_number:
            if hasattr(self.fq_number, 'to_alipay_dict'):
                params['fq_number'] = self.fq_number.to_alipay_dict()
            else:
                params['fq_number'] = self.fq_number
        if self.fq_seller_percent:
            if hasattr(self.fq_seller_percent, 'to_alipay_dict'):
                params['fq_seller_percent'] = self.fq_seller_percent.to_alipay_dict()
            else:
                params['fq_seller_percent'] = self.fq_seller_percent
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FQExtendParams()
        if 'fq_number' in d:
            o.fq_number = d['fq_number']
        if 'fq_seller_percent' in d:
            o.fq_seller_percent = d['fq_seller_percent']
        return o


