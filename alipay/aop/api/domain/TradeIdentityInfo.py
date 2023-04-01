#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeIdentityInfo(object):

    def __init__(self):
        self._trade_no = None
        self._trade_pid = None
        self._trade_shopid = None

    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_pid(self):
        return self._trade_pid

    @trade_pid.setter
    def trade_pid(self, value):
        self._trade_pid = value
    @property
    def trade_shopid(self):
        return self._trade_shopid

    @trade_shopid.setter
    def trade_shopid(self, value):
        self._trade_shopid = value


    def to_alipay_dict(self):
        params = dict()
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.trade_pid:
            if hasattr(self.trade_pid, 'to_alipay_dict'):
                params['trade_pid'] = self.trade_pid.to_alipay_dict()
            else:
                params['trade_pid'] = self.trade_pid
        if self.trade_shopid:
            if hasattr(self.trade_shopid, 'to_alipay_dict'):
                params['trade_shopid'] = self.trade_shopid.to_alipay_dict()
            else:
                params['trade_shopid'] = self.trade_shopid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeIdentityInfo()
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_pid' in d:
            o.trade_pid = d['trade_pid']
        if 'trade_shopid' in d:
            o.trade_shopid = d['trade_shopid']
        return o


