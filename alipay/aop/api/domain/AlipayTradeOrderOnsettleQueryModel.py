#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeOrderOnsettleQueryModel(object):

    def __init__(self):
        self._royalty_source = None
        self._trade_no = None

    @property
    def royalty_source(self):
        return self._royalty_source

    @royalty_source.setter
    def royalty_source(self, value):
        self._royalty_source = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.royalty_source:
            if hasattr(self.royalty_source, 'to_alipay_dict'):
                params['royalty_source'] = self.royalty_source.to_alipay_dict()
            else:
                params['royalty_source'] = self.royalty_source
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
        o = AlipayTradeOrderOnsettleQueryModel()
        if 'royalty_source' in d:
            o.royalty_source = d['royalty_source']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


