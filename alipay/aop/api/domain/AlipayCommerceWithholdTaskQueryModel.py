#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceWithholdTaskQueryModel(object):

    def __init__(self):
        self._out_trade_no = None
        self._withhold_no = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def withhold_no(self):
        return self._withhold_no

    @withhold_no.setter
    def withhold_no(self, value):
        self._withhold_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.withhold_no:
            if hasattr(self.withhold_no, 'to_alipay_dict'):
                params['withhold_no'] = self.withhold_no.to_alipay_dict()
            else:
                params['withhold_no'] = self.withhold_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceWithholdTaskQueryModel()
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'withhold_no' in d:
            o.withhold_no = d['withhold_no']
        return o


