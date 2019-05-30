#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeSettleConfirmCancelModel(object):

    def __init__(self):
        self._ori_request_no = None
        self._trade_no = None

    @property
    def ori_request_no(self):
        return self._ori_request_no

    @ori_request_no.setter
    def ori_request_no(self, value):
        self._ori_request_no = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ori_request_no:
            if hasattr(self.ori_request_no, 'to_alipay_dict'):
                params['ori_request_no'] = self.ori_request_no.to_alipay_dict()
            else:
                params['ori_request_no'] = self.ori_request_no
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
        o = AlipayTradeSettleConfirmCancelModel()
        if 'ori_request_no' in d:
            o.ori_request_no = d['ori_request_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


