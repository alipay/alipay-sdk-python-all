#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeOrderSettleQueryModel(object):

    def __init__(self):
        self._settle_no = None

    @property
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.settle_no:
            if hasattr(self.settle_no, 'to_alipay_dict'):
                params['settle_no'] = self.settle_no.to_alipay_dict()
            else:
                params['settle_no'] = self.settle_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeOrderSettleQueryModel()
        if 'settle_no' in d:
            o.settle_no = d['settle_no']
        return o


