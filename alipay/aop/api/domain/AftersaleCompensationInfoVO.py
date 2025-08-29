#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AftersaleCompensationInfoVO(object):

    def __init__(self):
        self._out_trade_no = None
        self._pay_notify_url = None

    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_notify_url(self):
        return self._pay_notify_url

    @pay_notify_url.setter
    def pay_notify_url(self, value):
        self._pay_notify_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_notify_url:
            if hasattr(self.pay_notify_url, 'to_alipay_dict'):
                params['pay_notify_url'] = self.pay_notify_url.to_alipay_dict()
            else:
                params['pay_notify_url'] = self.pay_notify_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AftersaleCompensationInfoVO()
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_notify_url' in d:
            o.pay_notify_url = d['pay_notify_url']
        return o


