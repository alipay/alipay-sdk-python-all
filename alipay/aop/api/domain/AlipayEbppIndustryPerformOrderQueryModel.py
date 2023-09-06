#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryPerformOrderQueryModel(object):

    def __init__(self):
        self._bill_no = None
        self._is_sub_merchant = None
        self._out_no = None
        self._trade_no = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def is_sub_merchant(self):
        return self._is_sub_merchant

    @is_sub_merchant.setter
    def is_sub_merchant(self, value):
        self._is_sub_merchant = value
    @property
    def out_no(self):
        return self._out_no

    @out_no.setter
    def out_no(self, value):
        self._out_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.is_sub_merchant:
            if hasattr(self.is_sub_merchant, 'to_alipay_dict'):
                params['is_sub_merchant'] = self.is_sub_merchant.to_alipay_dict()
            else:
                params['is_sub_merchant'] = self.is_sub_merchant
        if self.out_no:
            if hasattr(self.out_no, 'to_alipay_dict'):
                params['out_no'] = self.out_no.to_alipay_dict()
            else:
                params['out_no'] = self.out_no
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryPerformOrderQueryModel()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'is_sub_merchant' in d:
            o.is_sub_merchant = d['is_sub_merchant']
        if 'out_no' in d:
            o.out_no = d['out_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


