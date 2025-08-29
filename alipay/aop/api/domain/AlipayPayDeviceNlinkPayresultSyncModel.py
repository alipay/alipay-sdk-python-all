#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenPayResult import OpenPayResult


class AlipayPayDeviceNlinkPayresultSyncModel(object):

    def __init__(self):
        self._ntoken = None
        self._open_pay_result = None
        self._paycode = None
        self._trade_no = None

    @property
    def ntoken(self):
        return self._ntoken

    @ntoken.setter
    def ntoken(self, value):
        self._ntoken = value
    @property
    def open_pay_result(self):
        return self._open_pay_result

    @open_pay_result.setter
    def open_pay_result(self, value):
        if isinstance(value, OpenPayResult):
            self._open_pay_result = value
        else:
            self._open_pay_result = OpenPayResult.from_alipay_dict(value)
    @property
    def paycode(self):
        return self._paycode

    @paycode.setter
    def paycode(self, value):
        self._paycode = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ntoken:
            if hasattr(self.ntoken, 'to_alipay_dict'):
                params['ntoken'] = self.ntoken.to_alipay_dict()
            else:
                params['ntoken'] = self.ntoken
        if self.open_pay_result:
            if hasattr(self.open_pay_result, 'to_alipay_dict'):
                params['open_pay_result'] = self.open_pay_result.to_alipay_dict()
            else:
                params['open_pay_result'] = self.open_pay_result
        if self.paycode:
            if hasattr(self.paycode, 'to_alipay_dict'):
                params['paycode'] = self.paycode.to_alipay_dict()
            else:
                params['paycode'] = self.paycode
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
        o = AlipayPayDeviceNlinkPayresultSyncModel()
        if 'ntoken' in d:
            o.ntoken = d['ntoken']
        if 'open_pay_result' in d:
            o.open_pay_result = d['open_pay_result']
        if 'paycode' in d:
            o.paycode = d['paycode']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


