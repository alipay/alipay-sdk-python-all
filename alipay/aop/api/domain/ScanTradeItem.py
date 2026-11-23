#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScanTradeItem(object):

    def __init__(self):
        self._encrypt_info = None
        self._trade_no = None

    @property
    def encrypt_info(self):
        return self._encrypt_info

    @encrypt_info.setter
    def encrypt_info(self, value):
        self._encrypt_info = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypt_info:
            if hasattr(self.encrypt_info, 'to_alipay_dict'):
                params['encrypt_info'] = self.encrypt_info.to_alipay_dict()
            else:
                params['encrypt_info'] = self.encrypt_info
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
        o = ScanTradeItem()
        if 'encrypt_info' in d:
            o.encrypt_info = d['encrypt_info']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


